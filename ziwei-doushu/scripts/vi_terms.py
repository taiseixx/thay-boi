"""Bảng thuật ngữ Hán → Việt và hàm chuyển ngữ output của script.

Phần tính toán bên trong script vẫn dùng chữ Hán (để giữ nguyên logic gốc và bộ test
đối chiếu với iztro). Hàm `translate()` chỉ chạy ở bước cuối, đổi mọi giá trị và key
có chữ Hán trong JSON output sang thuật ngữ huyền học tiếng Việt.

File này giống hệt nhau ở `ziwei-doushu/scripts/` và `qimen-dunjia/scripts/`
để mỗi skill tự chạy độc lập. Sửa một file thì chép sang file còn lại.
"""

from __future__ import annotations

import re
from typing import Any

# ---------------------------------------------------------------------------
# Can, Chi
# ---------------------------------------------------------------------------
STEMS_VI = {
    "甲": "Giáp", "乙": "Ất", "丙": "Bính", "丁": "Đinh", "戊": "Mậu",
    "己": "Kỷ", "庚": "Canh", "辛": "Tân", "壬": "Nhâm", "癸": "Quý",
}
BRANCHES_VI = {
    "子": "Tý", "丑": "Sửu", "寅": "Dần", "卯": "Mão", "辰": "Thìn", "巳": "Tỵ",
    "午": "Ngọ", "未": "Mùi", "申": "Thân", "酉": "Dậu", "戌": "Tuất", "亥": "Hợi",
}
GANZHI_VI = {**STEMS_VI, **BRANCHES_VI}

# ---------------------------------------------------------------------------
# Thuật ngữ chung
# ---------------------------------------------------------------------------
TERMS: dict[str, str] = {
    # Ngũ hành, âm dương, giới tính
    "木": "Mộc", "火": "Hỏa", "土": "Thổ", "金": "Kim", "水": "Thủy",
    "阳": "Dương", "阴": "Âm", "男": "Nam", "女": "Nữ",
    # Phương vị
    "北": "Bắc", "南": "Nam", "东": "Đông", "西": "Tây",
    "东北": "Đông Bắc", "东南": "Đông Nam", "西北": "Tây Bắc", "西南": "Tây Nam", "中": "Trung",
    # Bát quái
    "坎": "Khảm", "坤": "Khôn", "震": "Chấn", "巽": "Tốn", "乾": "Càn",
    "兑": "Đoài", "艮": "Cấn", "离": "Ly",
    # 24 tiết khí
    "立春": "Lập Xuân", "雨水": "Vũ Thủy", "惊蛰": "Kinh Trập", "春分": "Xuân Phân",
    "清明": "Thanh Minh", "谷雨": "Cốc Vũ", "立夏": "Lập Hạ", "小满": "Tiểu Mãn",
    "芒种": "Mang Chủng", "夏至": "Hạ Chí", "小暑": "Tiểu Thử", "大暑": "Đại Thử",
    "立秋": "Lập Thu", "处暑": "Xử Thử", "白露": "Bạch Lộ", "秋分": "Thu Phân",
    "寒露": "Hàn Lộ", "霜降": "Sương Giáng", "立冬": "Lập Đông", "小雪": "Tiểu Tuyết",
    "大雪": "Đại Tuyết", "冬至": "Đông Chí", "小寒": "Tiểu Hàn", "大寒": "Đại Hàn",
    # --- Tử vi: 12 cung ---
    "命宫": "Mệnh", "兄弟": "Huynh Đệ", "夫妻": "Phu Thê", "子女": "Tử Tức",
    "财帛": "Tài Bạch", "疾厄": "Tật Ách", "迁移": "Thiên Di", "交友": "Nô Bộc",
    "官禄": "Quan Lộc", "田宅": "Điền Trạch", "福德": "Phúc Đức", "父母": "Phụ Mẫu",
    "身宫": "Thân",
    # --- Tử vi: 14 chính tinh ---
    "紫微": "Tử Vi", "天机": "Thiên Cơ", "太阳": "Thái Dương", "武曲": "Vũ Khúc",
    "天同": "Thiên Đồng", "廉贞": "Liêm Trinh", "天府": "Thiên Phủ", "太阴": "Thái Âm",
    "贪狼": "Tham Lang", "巨门": "Cự Môn", "天相": "Thiên Tướng", "天梁": "Thiên Lương",
    "七杀": "Thất Sát", "破军": "Phá Quân",
    # --- Tử vi: phụ tinh, sát tinh, tạp tinh ---
    "文昌": "Văn Xương", "文曲": "Văn Khúc", "左辅": "Tả Phù", "右弼": "Hữu Bật",
    "天魁": "Thiên Khôi", "天钺": "Thiên Việt", "禄存": "Lộc Tồn", "擎羊": "Kình Dương",
    "陀罗": "Đà La", "火星": "Hỏa Tinh", "铃星": "Linh Tinh", "地空": "Địa Không",
    "地劫": "Địa Kiếp", "天马": "Thiên Mã", "天刑": "Thiên Hình", "天姚": "Thiên Diêu",
    "红鸾": "Hồng Loan", "天喜": "Thiên Hỷ", "天哭": "Thiên Khốc", "天虚": "Thiên Hư",
    "孤辰": "Cô Thần", "寡宿": "Quả Tú",
    # --- Tử vi: tứ hóa ---
    "化禄": "Hóa Lộc", "化权": "Hóa Quyền", "化科": "Hóa Khoa", "化忌": "Hóa Kỵ",
    "禄": "Lộc", "权": "Quyền", "科": "Khoa", "忌": "Kỵ",
    # --- Tử vi: miếu vượng đắc hãm ---
    "庙": "Miếu", "旺": "Vượng", "得地": "Đắc địa", "利": "Lợi", "平": "Bình",
    "不得地": "Bất đắc địa", "落陷": "Hãm",
    # --- Tử vi: ngũ hành cục, chiều đại hạn ---
    "水二局": "Thủy Nhị Cục", "木三局": "Mộc Tam Cục", "金四局": "Kim Tứ Cục",
    "土五局": "Thổ Ngũ Cục", "火六局": "Hỏa Lục Cục",
    "顺行": "Thuận hành", "逆行": "Nghịch hành",
    "默认算法": "thuật toán mặc định", "调用方指定": "do bên gọi chỉ định",
    # --- Kỳ môn: cửu tinh ---
    "天蓬": "Thiên Bồng", "天任": "Thiên Nhậm", "天冲": "Thiên Xung", "天辅": "Thiên Phụ",
    "天英": "Thiên Anh", "天芮": "Thiên Nhuế", "天柱": "Thiên Trụ", "天心": "Thiên Tâm",
    "天禽": "Thiên Cầm",
    # --- Kỳ môn: bát môn ---
    "休门": "Hưu Môn", "生门": "Sinh Môn", "伤门": "Thương Môn", "杜门": "Đỗ Môn",
    "景门": "Cảnh Môn", "死门": "Tử Môn", "惊门": "Kinh Môn", "开门": "Khai Môn",
    # --- Kỳ môn: bát thần ---
    "值符": "Trực Phù", "螣蛇": "Đằng Xà", "腾蛇": "Đằng Xà", "六合": "Lục Hợp",
    "白虎": "Bạch Hổ", "玄武": "Huyền Vũ", "九地": "Cửu Địa", "九天": "Cửu Thiên",
    "值使": "Trực Sử",
    # --- Kỳ môn: cửu cung ---
    "坎宫": "cung Khảm", "坤宫": "cung Khôn", "震宫": "cung Chấn", "巽宫": "cung Tốn",
    "中宫": "Trung cung", "乾宫": "cung Càn", "兑宫": "cung Đoài", "艮宫": "cung Cấn",
    "离宫": "cung Ly",
    # --- Kỳ môn: độn, nguyên ---
    "阳遁": "Dương độn", "阴遁": "Âm độn",
    "上元": "Thượng nguyên", "中元": "Trung nguyên", "下元": "Hạ nguyên",
    # --- Kỳ môn: cách cục, quan hệ sinh khắc ---
    "三奇配吉门": "Tam Kỳ phối Cát Môn", "伏吟": "Phục Ngâm", "反吟": "Phản Ngâm",
    "门反吟": "Môn Phản Ngâm", "门迫": "Môn Bách", "门受制": "Môn Thụ Chế",
    "值符得位": "Trực Phù đắc vị",
    "吉": "Cát", "凶": "Hung",
    "比和": "Tỷ hòa", "天生地": "Thiên sinh Địa", "地生天": "Địa sinh Thiên",
    "天克地": "Thiên khắc Địa", "地克天": "Địa khắc Thiên",
    "生": "Sinh", "被生": "Được sinh", "克": "Khắc", "被克": "Bị khắc",
    # Từ đơn hay gặp trong câu
    "时": "giờ", "年": "năm", "月": "tháng", "日": "ngày", "宫": "cung",
}

# ---------------------------------------------------------------------------
# Âm lịch: tháng, ngày viết bằng chữ Hán (lunar_python)
# ---------------------------------------------------------------------------
_CN_NUM = {"〇": 0, "零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
           "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}
_MONTH_VI = {"正": "Giêng", "冬": "Mười Một", "腊": "Chạp"}


def lunar_month_vi(text: str) -> str:
    leap = text.startswith("闰")
    core = text[1:] if leap else text
    if core in _MONTH_VI:
        out = _MONTH_VI[core]
    elif core == "十一":
        out = "Mười Một"
    elif core == "十二":
        out = "Chạp"
    elif core in _CN_NUM:
        out = str(_CN_NUM[core])
    else:
        out = core
    return f"nhuận {out}" if leap else out


def lunar_day_vi(text: str) -> str | None:
    if text.startswith("初") and len(text) == 2:
        n = _CN_NUM.get(text[1])
        return None if n is None else f"mùng {n}"
    if text == "十":
        return "10"
    if text.startswith("十") and len(text) == 2:
        return str(10 + _CN_NUM.get(text[1], 0))
    if text.startswith("廿") and len(text) == 2:
        return str(20 + _CN_NUM.get(text[1], 0))
    if text == "三十":
        return "30"
    if text.startswith("卅"):
        return str(30 + (_CN_NUM.get(text[1], 0) if len(text) > 1 else 0))
    return None


# ---------------------------------------------------------------------------
# Câu thông báo (warnings, error, ruleset) có trong hai script
# ---------------------------------------------------------------------------
def _g(m: re.Match, name: str) -> str:
    return translate_text(m.group(name))


SENTENCES: list[tuple[re.Pattern, Any]] = [
    # --- ziwei_cli.py ---
    (re.compile(r"^闰月整月按本月$"), "Cả tháng nhuận tính theo tháng hiện tại"),
    (re.compile(r"^闰月整月按下月$"), "Cả tháng nhuận tính theo tháng sau"),
    (re.compile(r"^闰月十五日及以前按本月，十六日起按下月$"),
     "Tháng nhuận: từ ngày 15 trở về trước tính theo tháng hiện tại, từ ngày 16 tính theo tháng sau"),
    (re.compile(r"^23:00 起视为次日子时，农历日期按次日计算（calculation.md 默认口径）$"),
     "Từ 23:00 coi là giờ Tý của ngày hôm sau, ngày âm lịch tính theo ngày hôm sau (quy ước mặc định trong calculation.md)"),
    (re.compile(r"^23:00 起取子时，但农历日期仍按当天（沿用用户既定口径时使用）$"),
     "Từ 23:00 lấy giờ Tý nhưng ngày âm lịch vẫn giữ ngày hôm đó (dùng khi theo quy ước sẵn có của người dùng)"),
    (re.compile(r"^日期格式需为 YYYY-MM-DD$"), "Ngày phải có định dạng YYYY-MM-DD"),
    (re.compile(r"^缺少出生时间：紫微排盘需要出生时辰，请先向用户确认$"),
     "Thiếu giờ sinh: lập lá số Tử vi cần giờ sinh, hãy xác nhận với người dùng trước"),
    (re.compile(r"^出生时间格式需为 HH:MM$"), "Giờ sinh phải có định dạng HH:MM"),
    (re.compile(r"^农历 (?P<y>\d+) 年没有闰(?P<m>\d+)月$"),
     lambda m: f"Năm âm lịch {m['y']} không có tháng nhuận {m['m']}"),
    (re.compile(r"^出生时间超出范围，小时应为 0-23，分钟 0-59$"),
     "Giờ sinh ngoài phạm vi: giờ phải từ 0-23, phút từ 0-59"),
    (re.compile(r"^不支持的 calendar_type: (?P<v>.*)（只接受 solar 或 lunar）$"),
     lambda m: f"calendar_type không hỗ trợ: {m['v']} (chỉ nhận solar hoặc lunar)"),
    (re.compile(r"^缺少或无法识别 gender（男/女）：性别决定大限顺逆，请先向用户确认$"),
     "Thiếu hoặc không nhận ra gender (男/女 hoặc male/female): giới tính quyết định chiều đại hạn, hãy xác nhận với người dùng trước"),
    (re.compile(r"^出生时间距时辰交界不足 15 分钟，时辰有误差时盘面会整体改变，建议按相邻两个时辰各排一盘对照。$"),
     "Giờ sinh cách ranh giới giữa hai giờ âm lịch chưa tới 15 phút. Nếu giờ sinh lệch, cả lá số sẽ thay đổi, nên lập lá số cho cả hai giờ liền kề để so sánh."),
    (re.compile(r"^十四主星不完整$"), "Thiếu sao trong 14 chính tinh"),
    (re.compile(r"^紫微(?P<p>\S+?)同宫出现在(?P<b>\S)，违反 calculation.md §7.4$"),
     lambda m: f"Tử Vi đồng cung {_g(m, 'p')} xuất hiện ở {_g(m, 'b')}, trái với calculation.md §7.4"),
    (re.compile(r"^四化星 (?P<s>\S+) 不在盘上$"),
     lambda m: f"Sao tứ hóa {_g(m, 's')} không có trên lá số"),
    (re.compile(r"^出生于 23 点后，已按次日子时排盘（农历日期取次日）；若用户既定口径不换日，请改用 late_zi_rule=same_day 重排。$"),
     "Sinh sau 23 giờ nên đã lập lá số theo giờ Tý ngày hôm sau (ngày âm lịch lấy ngày hôm sau). Nếu quy ước của người dùng là không đổi ngày, hãy chạy lại với late_zi_rule=same_day."),
    (re.compile(r"^出生于农历闰(?P<m>\d+)月(?P<d>\d+)日，闰月按 (?P<rule>\w+)（(?P<origin>[^：]+)：(?P<desc>[^）]+)）定为(?P<cm>\d+)月；若用户既定口径不同，请改 leap_month_rule 重排。$"),
     lambda m: (f"Sinh ngày {m['d']} tháng nhuận {m['m']} âm lịch, tháng nhuận tính theo {m['rule']} "
                f"({_g(m, 'origin')}: {_g(m, 'desc')}) nên định là tháng {m['cm']}. "
                f"Nếu quy ước của người dùng khác, hãy đổi leap_month_rule và chạy lại.")),
    (re.compile(r"^以农历正月初一换年，年干支取农历年。$"),
     "Đổi năm vào mùng 1 tháng Giêng âm lịch, can chi năm lấy theo năm âm lịch."),
    (re.compile(r"^大限年龄为虚岁。$"), "Tuổi đại hạn tính theo tuổi mụ."),
    (re.compile(r"^(?P<gz>\S{2})年(?P<mo>闰?\S{1,2})月(?P<d>\S{1,2})$"),
     lambda m: (f"Năm {translate_text(m['gz'])}, tháng {lunar_month_vi(m['mo'])}, "
                f"ngày {lunar_day_vi(m['d']) or m['d']}")
     if all(c in GANZHI_VI for c in m["gz"]) else None),
    (re.compile(r"^(?P<b>\S)时$"),
     lambda m: f"giờ {BRANCHES_VI[m['b']]}" if m["b"] in BRANCHES_VI else None),
    # --- qimen_cli.py ---
    (re.compile(r"^未提供海外时区，脚本暂按 (?P<tz>\S+) 计算，请在访谈中先补齐时区。$"),
     lambda m: f"Chưa có múi giờ ở nước ngoài, script tạm tính theo {m['tz']}. Hãy hỏi người dùng múi giờ trước khi lập bàn."),
    (re.compile(r"^已收到海外城市 (?P<c>.+)，但仍缺少明确时区。$"),
     lambda m: f"Đã nhận thành phố ở nước ngoài {m['c']} nhưng vẫn thiếu múi giờ rõ ràng."),
    (re.compile(r"^无法识别时区 (?P<tz>\S+): (?P<e>.*)$"),
     lambda m: f"Không nhận ra múi giờ {m['tz']}: {m['e']}"),
    (re.compile(r"^无法确定当前节气$"), "Không xác định được tiết khí hiện tại"),
    (re.compile(r"^time_input 不能为空$"), "time_input không được để trống"),
    (re.compile(r"^birth_time 不能为空$"), "birth_time không được để trống"),
    (re.compile(r"^缺少 birth_time$"), "Thiếu birth_time"),
    (re.compile(r"^(?P<k>late_zi_rule|leap_month_rule) 只接受 (?P<v>.*)$"),
     lambda m: f"{m['k']} chỉ nhận {m['v']}"),
    (re.compile(r"^不支持的 calendar_type: (?P<v>.*)$"),
     lambda m: f"calendar_type không hỗ trợ: {m['v']}"),
    (re.compile(r"^地盘中未找到天干 (?P<s>\S)$"),
     lambda m: f"Không tìm thấy thiên can {_g(m, 's')} trên địa bàn"),
    (re.compile(r"^中宫地盘(?P<s>\S)寄坤，天禽随天芮转出$"),
     lambda m: f"Can địa bàn {_g(m, 's')} của Trung cung ký ở Khôn, Thiên Cầm theo Thiên Nhuế chuyển ra ngoài"),
    (re.compile(r"^地盘寄坤：承载中五地盘干$"), "Địa bàn ký Khôn: chứa can địa bàn của Trung ngũ"),
    (re.compile(r"^天盘随转：天禽与中干(?P<s>\S)随天芮落此宫$"),
     lambda m: f"Thiên bàn chuyển theo: Thiên Cầm và can trung cung {_g(m, 's')} theo Thiên Nhuế rơi vào cung này"),
    (re.compile(r"^(?P<st>\S+?)本宫在(?P<h>\d)，落对冲(?P<p>\d)宫；天盘(?P<sk>\S+)加地盘(?P<e>\S+)$"),
     lambda m: (f"{_g(m, 'st')} vốn ở cung {m['h']}, rơi vào cung xung đối {m['p']}; "
                f"can thiên bàn {_g(m, 'sk')} gia lên can địa bàn {_g(m, 'e')}")),
    (re.compile(r"^(?P<d>\S+?)本宫在(?P<h>\d)，落对冲(?P<p>\d)宫$"),
     lambda m: f"{_g(m, 'd')} vốn ở cung {m['h']}, rơi vào cung xung đối {m['p']}"),
    (re.compile(r"^天地盘同为(?P<s>\S)$"),
     lambda m: f"Thiên bàn và địa bàn cùng là {_g(m, 's')}"),
    (re.compile(r"^(?P<d>\S+?)\((?P<de>\S)\)克(?P<p>\S+?)\((?P<pe>\S)\)$"),
     lambda m: f"{_g(m, 'd')} ({_g(m, 'de')}) khắc {_g(m, 'p')} ({_g(m, 'pe')})"),
    (re.compile(r"^(?P<d>\S+?)\((?P<de>\S)\)受(?P<p>\S+?)\((?P<pe>\S)\)克$"),
     lambda m: f"{_g(m, 'd')} ({_g(m, 'de')}) bị {_g(m, 'p')} ({_g(m, 'pe')}) khắc"),
    (re.compile(r"^(?P<s>\S)\+(?P<d>\S+)$"),
     lambda m: f"{_g(m, 's')} + {_g(m, 'd')}"),
    (re.compile(r"^(?P<s>\S+?)回归本宫$"),
     lambda m: f"{_g(m, 's')} trở về cung gốc"),
    (re.compile(r"^时干为甲，按旬首所遁之仪 (?P<y>\S) 入盘。$"),
     lambda m: f"Can giờ là Giáp, nhập bàn theo nghi mà tuần thủ ẩn vào: {_g(m, 'y')}."),
    (re.compile(r"^本规则集中宫相关判断一律寄坤处理。$"),
     "Trong bộ quy tắc này, mọi phán đoán liên quan đến Trung cung đều xử lý theo ký Khôn."),
    (re.compile(r"^值使移宫落中五，按寄坤处理。$"),
     "Trực Sử di cung rơi vào Trung ngũ, xử lý theo ký Khôn."),
    (re.compile(r"^当前时间距离节令起点较近，属于节气边界附近。$"),
     "Thời điểm hiện tại gần lúc bắt đầu tiết khí, thuộc vùng ranh giới tiết khí."),
    (re.compile(r"^当前时间距离下一个节令较近，属于节气边界附近。$"),
     "Thời điểm hiện tại gần tiết khí kế tiếp, thuộc vùng ranh giới tiết khí."),
    (re.compile(r"^日干为甲，取日旬首\((?P<x>\S+)\)所遁之仪 (?P<y>\S) 入盘$"),
     lambda m: f"Can ngày là Giáp, nhập bàn theo nghi mà tuần thủ ngày ({_g(m, 'x')}) ẩn vào: {_g(m, 'y')}"),
    (re.compile(r"^年干为甲，取戊代入$"), "Can năm là Giáp, lấy Mậu thay vào"),
    (re.compile(r"^月干为甲，取戊代入$"), "Can tháng là Giáp, lấy Mậu thay vào"),
    (re.compile(r"^时家转盘奇门（大陆默认）$"), "Thời gia Chuyển bàn Kỳ môn (mặc định Trung Quốc đại lục)"),
    (re.compile(r"^冬至到芒种用阳遁，夏至到大雪用阴遁，按当前所处二十四节气（含中气）判定。$"),
     "Từ Đông Chí đến Mang Chủng dùng Dương độn, từ Hạ Chí đến Đại Tuyết dùng Âm độn, xác định theo tiết khí hiện tại trong 24 tiết khí (gồm cả trung khí)."),
    (re.compile(r"^按日干支所在六十甲子序列，每 5 日一元，循环上元/中元/下元。$"),
     "Theo vị trí can chi ngày trong Lục thập hoa giáp, mỗi 5 ngày là một nguyên, lặp vòng Thượng nguyên / Trung nguyên / Hạ nguyên."),
    (re.compile(r"^按当前节气和三元，从固定定局表取局数。$"),
     "Theo tiết khí hiện tại và tam nguyên, lấy số cục từ bảng định cục cố định."),
    (re.compile(r"^值符随时干落宫；值使从旬首地盘宫起逐时沿九宫数序移宫（阳顺阴逆，中五寄坤），二者分别移宫。$"),
     "Trực Phù theo can giờ mà rơi cung; Trực Sử khởi từ cung địa bàn của tuần thủ, mỗi giờ đi một cung theo thứ tự số cửu cung (Dương thuận, Âm nghịch, Trung ngũ ký Khôn). Hai cái di cung riêng."),
    (re.compile(r"^中宫地盘干寄坤；天禽与中干随天芮转到天芮所落之宫。$"),
     "Can địa bàn Trung cung ký Khôn; Thiên Cầm và can trung cung theo Thiên Nhuế chuyển đến cung Thiên Nhuế rơi vào."),
    (re.compile(r"^hour_yima 取时支三合局驿马，day_yima 取日支三合局驿马，分别输出。$"),
     "hour_yima lấy Dịch Mã theo tam hợp cục của chi giờ, day_yima lấy Dịch Mã theo tam hợp cục của chi ngày, xuất riêng."),
]

_HAN = re.compile(r"[㐀-鿿]")
_KEYS_BY_LEN = sorted(TERMS, key=len, reverse=True)


def _has_han(s: str) -> bool:
    return bool(_HAN.search(s))


def translate_text(s: str) -> str:
    """Chuyển một chuỗi sang tiếng Việt. Chuỗi không có chữ Hán giữ nguyên."""
    if not isinstance(s, str) or not _has_han(s):
        return s
    if s in TERMS:
        return TERMS[s]
    # Can chi ghép, ví dụ 甲子, 申子辰, 丙/戊
    pieces = re.split(r"(/)", s)
    if all(p == "/" or (p and all(c in GANZHI_VI for c in p)) for p in pieces):
        return "".join(p if p == "/" else " ".join(GANZHI_VI[c] for c in p) for p in pieces)
    for pattern, repl in SENTENCES:
        m = pattern.match(s)
        if m:
            out = repl(m) if callable(repl) else repl
            if out is not None:
                return out
    if lunar_day_vi(s):
        return lunar_day_vi(s)  # type: ignore[return-value]
    if re.fullmatch(r"闰?(正|冬|腊|十一|十二|[一二三四五六七八九十])", s):
        return lunar_month_vi(s)
    return _greedy(s)


def _greedy(s: str) -> str:
    """Dự phòng: thay từng cụm thuật ngữ dài nhất, can chi lẻ thay từng chữ."""
    out: list[str] = []
    i = 0
    while i < len(s):
        for key in _KEYS_BY_LEN:
            if s.startswith(key, i):
                out.append(f" {TERMS[key]} ")
                i += len(key)
                break
        else:
            c = s[i]
            out.append(f" {GANZHI_VI[c]} " if c in GANZHI_VI else c)
            i += 1
    return re.sub(r" {2,}", " ", "".join(out)).strip()


def translate(obj: Any) -> Any:
    """Chuyển ngữ đệ quy toàn bộ output JSON (cả key lẫn value)."""
    if isinstance(obj, dict):
        return {translate_text(k) if isinstance(k, str) else k: translate(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [translate(v) for v in obj]
    if isinstance(obj, str):
        return translate_text(obj)
    return obj


# Bảng ngược Việt → Hán, dùng cho test đối chiếu bảng trong tài liệu tiếng Việt.
VI_TO_ZH: dict[str, str] = {}
for _zh, _vi in {**TERMS, **GANZHI_VI}.items():
    VI_TO_ZH.setdefault(_vi, _zh)
# Một số từ tiếng Việt trùng nghĩa: ưu tiên nghĩa dùng trong bảng
VI_TO_ZH.update({"Nam": "男", "Thân": "申", "Trung": "中", "Thái Âm": "太阴", "Đằng Xà": "螣蛇"})


def to_zh(text: str) -> str:
    """Đổi ô bảng tiếng Việt về chữ Hán: 'Tý', 'Giáp Tý', 'Bính/Mậu', 'Thân Tý Thìn'."""
    text = text.strip()
    if text in VI_TO_ZH:
        return VI_TO_ZH[text]
    if "/" in text:
        return "/".join(to_zh(p) for p in text.split("/"))
    words = text.split()
    if words and all(w in GANZHI_VI.values() for w in words):
        rev = {v: k for k, v in GANZHI_VI.items()}
        return "".join(rev[w] for w in words)
    return text
