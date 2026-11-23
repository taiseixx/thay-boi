# Numerologist Skills (Thầy mệnh lý trên mạng của bạn)

> Bản này được copy từ [FANzR-arch/Numerologist_skills](https://github.com/FANzR-arch/Numerologist_skills) (commit `53ab46e`) và chuyển ngữ sang tiếng Việt. Repo gốc **không có file LICENSE**, nên mặc định tác giả giữ toàn bộ bản quyền. Chỉ dùng để thử nghiệm nội bộ; muốn phát hành hoặc dùng thương mại thì cần xin phép tác giả gốc.

Dự án này tách các AI skill liên quan đến thuật số truyền thống thành các module kỹ thuật có thể kiểm tra, tái sử dụng và mở rộng dần. Mục tiêu không phải là bọc mô hình cho "giỏi huyền học hơn", mà là cố gắng giảm ảo giác của nó ở các khâu lập lá số, quy ước trường phái, thứ tự các bước và chuỗi luận giải.

## Các skill hiện có

| Thư mục | Hệ | Công dụng chính | Tính toán cố định / phụ thuộc |
|---|---|---|---|
| `qimen-dunjia/` | Kỳ môn độn giáp | Xem một việc cụ thể, chọn giờ, phương vị, tìm lành tránh dữ | Python CLI: `scripts/qimen_cli.py` |
| `ziwei-doushu/` | Tử vi đẩu số | Luận cấu trúc lá số bản mệnh, phân tích cung, đại hạn lưu niên | Python CLI: `scripts/ziwei_cli.py` |
| `bazi/` | Tứ trụ Bát tự | Nhật chủ mạnh yếu, cách cục, thập thần, đại vận lưu niên | Dựa vào quy tắc và references (chưa có script) |

## Cấu trúc repo

- `SKILL.md`: mô tả skill chính, điều kiện kích hoạt, quy trình, ràng buộc output
- `references/`: bộ quy tắc, bảng thuật ngữ, ví dụ, giải thích quy ước
- `scripts/`: script bên ngoài dùng khi cần tính toán cứng (hiện có ở Kỳ môn độn giáp và Tử vi đẩu số)
- `scripts/vi_terms.py`: bảng thuật ngữ Hán → Việt, dùng để chuyển ngữ output của script (thêm trong bản tiếng Việt)

## Nguyên tắc thiết kế

1. Hỏi trước, xuất kết quả sau: thông tin chưa đủ thì ưu tiên bổ sung tham số, không cố lập lá số.
2. Đẩy phần tính toán xác định ra ngoài: đổi lịch, lập lá số cố định, tính toán có cấu trúc thì ưu tiên giao cho script hoặc kết quả lập lá số đáng tin.
3. Nói rõ quy ước trước, kết luận sau: trường phái, quy tắc đổi ngày, cách tính tháng nhuận, quy tắc mặc định đều phải nói rõ.
4. Chỉ đưa tham khảo có cấu trúc: các tình huống rủi ro cao như sức khỏe, pháp luật, tài chính không thay cho lời khuyên chuyên môn thực tế.

## Bắt đầu nhanh

Chạy script tính toán cố định của Kỳ môn độn giáp:

```bash
pip install -r qimen-dunjia/scripts/requirements.txt
python qimen-dunjia/scripts/qimen_cli.py --input tmp/qimen_input.json --output tmp/qimen_output.json
```

Chạy script lập lá số Tử vi đẩu số:

```bash
pip install -r ziwei-doushu/scripts/requirements.txt
python ziwei-doushu/scripts/ziwei_cli.py --input tmp/ziwei_input.json --output tmp/ziwei_output.json
```

Ví dụ input Tử vi (`tmp/ziwei_input.json`):

```json
{"calendar_type": "solar", "birth_time": "1998-09-21 14:30", "gender": "male", "query_year": 2026}
```

Ví dụ input Kỳ môn (`tmp/qimen_input.json`), xem ngay bây giờ ở Hà Nội:

```json
{"question_type": "sự nghiệp", "question_goal": "có nên nhảy việc không", "calendar_type": "now",
 "location": {"country": "Vietnam", "city": "Hà Nội", "timezone": "Asia/Ho_Chi_Minh"}}
```

Output mặc định đã chuyển sang thuật ngữ tiếng Việt. Thêm `"lang": "zh"` vào input nếu muốn giữ chữ Hán như bản gốc.

Chạy test:

```bash
pip install pytest
python -m pytest ziwei-doushu/scripts/tests qimen-dunjia/scripts/tests
```

## Vì sao có repo này

Thay vì để LLM cố nói tiếp trong trạng thái "hiểu lơ mơ", tốt hơn là tách các bước then chốt ra:

- Dùng ràng buộc trong prompt để kiểm soát thứ tự hỏi và giới hạn output
- Dùng references để cố định thuật ngữ, quy ước và thứ tự phán đoán
- Dùng script bên ngoài để gánh phần tính toán cứng

Như vậy ít nhất quá trình minh bạch hơn, lỗi dễ lộ ra hơn, và ranh giới phiên bản cũng rõ hơn.

## Miễn trừ trách nhiệm

Nội dung repo này dùng cho việc diễn đạt thuật số truyền thống theo hướng kỹ thuật và thử nghiệm ràng buộc AI, không cấu thành lời khuyên về y tế, pháp luật, tài chính hay các quyết định thực tế khác.

## Ghi chú về bản chuyển ngữ

- Tài liệu (`README.md`, mọi `SKILL.md`, mọi file trong `references/`) đã chuyển sang tiếng Việt với thuật ngữ huyền học chuẩn (Hán Việt).
- Logic tính toán trong script giữ nguyên, bên trong vẫn dùng chữ Hán để không làm lệch kết quả và giữ bộ test đối chiếu với thư viện iztro. Chỉ có bước cuối chuyển output sang tiếng Việt qua `vi_terms.py`.
- Comment và docstring trong code Python, file fixture test và trang slide `20260325-AI术数工程化-可视化.html` vẫn giữ tiếng Trung như bản gốc.
- Trong Tử vi, cung 交友 dịch là **Nô Bộc** theo cách gọi phổ biến ở Việt Nam (có nơi gọi là Giao Hữu).

---
*Thuộc sáng kiến AI Engineering of Traditional Divination (Kỹ thuật hóa thuật số truyền thống bằng AI).*
