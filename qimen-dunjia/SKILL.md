---
name: qimen-dunjia
description: >
  Kỹ năng lập bàn, luận bàn Kỳ môn độn giáp, chọn giờ, phán đoán phương vị và dạy lý thuyết.
  Khi người dùng nhắc rõ đến Kỳ môn độn giáp, Thời gia Kỳ môn, lập bàn Kỳ môn, luận bàn Kỳ môn,
  chọn ngày giờ tốt theo Kỳ môn, chọn phương vị, tìm lành tránh dữ, hoặc yêu cầu "dùng Kỳ môn"
  để xem một việc cụ thể, bắt buộc dùng kỹ năng này. Trước khi lập bàn chính thức phải phỏng vấn
  có cấu trúc, sau đó gọi script để tính phần cố định, cuối cùng mới luận giải và đưa lời khuyên.
compatibility: Requires Python 3.11+, lunar_python, and tzdata; run scripts/qimen_cli.py for all fixed calculations.
---

# Kỹ năng Kỳ môn độn giáp

Kỹ năng này dành cho người hỏi việc bình thường, mặc định dùng bộ quy tắc `mainline-cn-v1`. Cách làm việc:

1. Phỏng vấn trước, xác nhận người dùng thực sự muốn xem gì, xem thời điểm nào, muốn phán đoán điều gì.
2. Dùng script để tính phần cố định, không lập bàn bằng tính nhẩm.
3. Cuối cùng mới dùng quy tắc Kỳ môn để luận giải, đưa lời khuyên và nhắc rủi ro.

Không bỏ qua bước phỏng vấn, không cố tính khi thông tin chưa đủ, và không đưa toàn bộ chuỗi suy luận nội bộ cho người dùng xem.

## Phạm vi kích hoạt

Các tình huống sau nên dùng kỹ năng này:

- Người dùng yêu cầu lập bàn hoặc luận bàn Kỳ môn chính thức.
- Người dùng yêu cầu dùng Kỳ môn để xem một việc cụ thể có thành không, khi nào nên động, đi hướng nào, tránh điều gì.
- Người dùng yêu cầu chọn giờ, chọn phương vị, lời khuyên tìm lành tránh dữ theo Kỳ môn.
- Người dùng yêu cầu giảng lý thuyết Kỳ môn, cách cục, dụng thần, ví dụ bàn.

Các tình huống sau không nên vào thẳng bước lập bàn chính thức:

- Người dùng chỉ đang tán gẫu về huyền học, chưa nói rõ muốn dùng Kỳ môn.
- Người dùng đưa quá ít thông tin, đến loại việc và thời gian cũng chưa có.
- Người dùng yêu cầu phái khác mà bộ quy tắc hiện tại không hỗ trợ.

## Nguyên tắc chung

- Bộ quy tắc mặc định cố định là `mainline-cn-v1`, không trộn phái khác vào đường lập bàn chính thức.
- Trước khi lập bàn chính thức bắt buộc phải phỏng vấn.
- Phần tính cố định luôn gọi `scripts/qimen_cli.py`.
- Không đưa toàn bộ chuỗi suy luận, chỉ đưa căn cứ then chốt và kết quả tính cần thiết.
- Chủ đề rủi ro cao như quyết định lớn, bệnh tật, pháp luật, đầu tư bắt buộc phải kèm lời khuyên thực tế.
- Không dùng lời dọa nạt, không nói "chắc chắn thất bại", "chắc chắn chết", "hết cứu".

## Quy tắc mặc định

Quy tắc dựng sẵn hiện tại cố định như sau:

- Hệ thống: Thời gia Chuyển bàn Kỳ môn
- Múi giờ mặc định của script: `Asia/Shanghai`. Với người dùng ở Việt Nam, luôn truyền `"timezone": "Asia/Ho_Chi_Minh"`.
- Khu vực áp dụng mặc định: ưu tiên Trung Quốc đại lục
- Định cục: phương pháp Trí nhuận, triển khai theo kiểu kỹ thuật
- Trung cung / ký cung: mọi phán đoán liên quan đến Trung cung đều xử lý theo ký Khôn

Quy tắc chi tiết xem `references/ruleset-mainline.md`.

Nếu người dùng yêu cầu rõ một phái khác:

1. Nói thẳng rằng kỹ năng này mặc định dùng `mainline-cn-v1`.
2. Hỏi người dùng có chấp nhận lập bàn theo bộ quy tắc này trước không.
3. Nếu không chấp nhận thì không lập bàn chính thức, chỉ bàn lý thuyết hoặc nói rõ phiên bản hiện tại chưa hỗ trợ.

## Quy trình làm việc

### Bước 1: Phỏng vấn trước

Trước khi lập bàn chính thức, bắt buộc phỏng vấn hai vòng.

Vòng một hỏi các câu cốt lõi, ngôn ngữ thẳng thắn:

1. Bạn muốn xem việc gì? Nói gọn trong một câu.
2. Việc này ứng với thời điểm nào? Nếu là ngay bây giờ thì cứ nói "bây giờ".
3. Bạn đang ở thành phố nào? Nếu không ở Trung Quốc đại lục, nói luôn quốc gia / thành phố.
4. Bạn muốn phán đoán điều gì nhất? Ví dụ có thành không, khi nào nên động, chọn bên nào, cần tránh gì.
5. Việc này hiện đã tiến triển đến bước nào?
6. Bạn muốn "kết luận thẳng" hay "giải thích chi tiết"?

Vòng hai hỏi thêm theo điều kiện:

- Chỉ có ngày, không có giờ: hỏi thêm giờ cụ thể, ít nhất đến giờ âm lịch.
- Đưa ngày âm lịch: hỏi thêm có phải tháng nhuận không.
- Ở nước ngoài: hỏi thêm múi giờ hoặc thành phố.
- Câu hỏi quá chung: hỏi thêm "bạn muốn phán đoán kết quả nào nhất".
- Chủ đề rủi ro cao: hỏi thêm có cần lời khuyên thực tế không, và nhắc tìm bác sĩ, luật sư, cố vấn tài chính.

Mẫu phỏng vấn xem `references/interview.md`.

### Bước 2: Quyết định có lập bàn chính thức không

Chỉ lập bàn chính thức khi đã xác nhận đủ:

- Loại việc rõ ràng
- Thời gian rõ ràng
- Địa điểm hoặc múi giờ rõ đến mức tính được
- Mục tiêu phán đoán rõ ràng

Nếu chưa đủ thì chỉ tiếp tục hỏi, chưa lập bàn.

Nếu người dùng chỉ muốn học lý thuyết:

- Hỏi trước họ muốn học gì.
- Không vào thẳng bước lập bàn chính thức.
- Có thể dạy kèm `references/examples.md`.

### Bước 3: Gọi script tính phần cố định

**Chuẩn bị: kiểm tra đã cài thư viện**

Trước khi lập bàn chính thức, kiểm tra thư viện. Nếu chưa cài, chạy:

```bash
pip install "lunar_python>=1.4.8,<2" "tzdata>=2024.1"
```

**Chạy script**

Đường dẫn script tính từ thư mục gốc của repo:

```bash
python "qimen-dunjia/scripts/qimen_cli.py" \
  --input "tmp/qimen_input.json" \
  --output "tmp/qimen_output.json"
```

Ghi JSON input vào `tmp/qimen_input.json` trước, chạy lệnh trên, rồi đọc `tmp/qimen_output.json`. Có thể thay `tmp/` bằng bất kỳ thư mục tạm nào ghi được.

Các trường tối thiểu của JSON input:

```json
{
  "question_type": "",
  "question_goal": "",
  "time_input": "",
  "calendar_type": "solar|lunar|now",
  "location": {
    "country": "",
    "city": "",
    "timezone": ""
  },
  "ruleset": "mainline-cn-v1",
  "lang": "vi|zh"
}
```

- `time_input` dạng `YYYY-MM-DD HH:MM`; khi `calendar_type` là `now` thì script lấy giờ hiện tại theo múi giờ.
- `lang` không bắt buộc, mặc định `vi`: mọi thuật ngữ trong output (cửu tinh, bát môn, bát thần, cung, can chi, cách cục, cảnh báo) được chuyển sang tiếng Việt, kể cả key của `door_index` và `star_index`. Truyền `zh` nếu cần giữ chữ Hán như bản gốc.

Yêu cầu sử dụng:

- Bạn tự chuyển kết quả phỏng vấn thành JSON input.
- Phần tính cố định bắt buộc lấy theo output của script.
- Nếu script không dùng được, không tính tay thay thế; nói rõ với người dùng rằng phiên bản hiện tại cần script mới lập bàn chính thức được.

### Bước 4: Đọc output của script

Tập trung đọc các trường sau:

| Trường | Công dụng |
|------|------|
| `normalized_input` | Xác nhận thời gian, múi giờ, sự việc được hiểu đúng |
| `calendar` | Đối chiếu dương lịch / âm lịch, tiết khí hiện tại (24 tiết khí, gồm trung khí) |
| `ganzhi` | Can chi năm tháng ngày giờ, tuần của ngày, tuần của giờ (để định tuần thủ / tuần không) |
| `chart.dun_type` | Âm độn / Dương độn |
| `chart.yuan` | Thượng nguyên / Trung nguyên / Hạ nguyên |
| `chart.ju_number` | Số cục (1-9) |
| `chart.xunshou` | Tuần thủ (ví dụ "Giáp Tý") |
| `chart.hidden_yi` | Nghi mà tuần thủ ẩn vào (can ẩn ở cung ký, ví dụ "Mậu"). **Không được bỏ sót** |
| `chart.kongwang` | Địa chi tuần không của giờ (ví dụ ["Dần", "Mão"]), ảnh hưởng giờ hiện tại |
| `chart.kongwang_palaces` | Số cung ứng với tuần không của giờ |
| `chart.day_kongwang` | Địa chi tuần không của ngày, ảnh hưởng đại cục cả ngày |
| `chart.day_kongwang_palaces` | Số cung ứng với tuần không của ngày |
| `chart.time_stem_visible` | Can giờ (đại diện cho việc được hỏi / động thái hiện tại, **căn cứ then chốt để lấy dụng thần**) |
| `chart.day_stem` | Cung của can ngày: `{ stem, palace, note }` (đại diện người hỏi) |
| `chart.year_stem` | Cung của can năm: `{ stem, palace, note }` (đại diện cấp trên / đại cục) |
| `chart.month_stem` | Cung của can tháng: `{ stem, palace, note }` (đại diện đồng nghiệp / đối thủ cùng lứa) |
| `chart.hour_yima` | Dịch Mã giờ: `{ branch, palace, source_branch }`, lấy theo chi giờ (câu hỏi về đi lại / biến động thì ưu tiên xem) |
| `chart.day_yima` | Dịch Mã ngày: `{ branch, palace, source_branch }`, lấy theo chi ngày (xem biến động cả ngày) |
| `chart.zhifu` | Trực Phù: `{ palace, star }`, theo can giờ mà rơi cung |
| `chart.zhishi` | Trực Sử: `{ palace, door, raw_palace, hours_from_xunshou }`, từ cung tuần thủ di cung theo từng giờ, **rơi cung riêng với Trực Phù** |
| `chart.center_hosting` | Trung cung chuyển theo: `{ hosted_star: Thiên Cầm, center_stem, earth_host_palace: 2, sky_palace, follows_star: Thiên Nhuế }` |
| `chart.door_index` | Từ điển tra ngược môn → cung, ví dụ `{"Khai Môn": 7, "Sinh Môn": 1, ...}`. **Định vị trực tiếp theo dụng thần** |
| `chart.star_index` | Từ điển tra ngược tinh → cung, ví dụ `{"Thiên Tâm": 7, "Thiên Nhuế": 9, "Thiên Cầm": 9, ...}` (Thiên Cầm cùng cung với Thiên Nhuế) |
| `chart.detected_patterns` | Kết quả tự phát hiện cách cục, mỗi mục gồm `name`, `palace`, `detail`, `nature` (Cát / Hung / Trung) |
| `chart.palaces` | Mảng đủ 9 cung (xem bên dưới) |
| `warnings` | Nhắc ranh giới, nhắc ký cung, v.v. |

**Các trường của mỗi cung trong `chart.palaces`:**

| Trường | Ý nghĩa |
|------|------|
| `palace` | Số cung (1-9) |
| `name` / `direction` / `trigram` / `element` | Tên cung / phương vị / quẻ / ngũ hành |
| `earth_stem` / `sky_stem` | Can địa bàn / can thiên bàn |
| `sky_stems` | Mọi can thiên bàn của cung; cung có Thiên Nhuế sẽ có thêm can địa bàn Trung ngũ chuyển theo đến |
| `hosted_sky_stem` / `hosted_stem_relation` | Can địa bàn Trung ngũ theo Thiên Nhuế chuyển đến / quan hệ của nó với can địa bàn của cung |
| `stem_relation` | Quan hệ ngũ hành giữa can thiên bàn và can địa bàn: Tỷ hòa / Thiên sinh Địa / Địa sinh Thiên / Thiên khắc Địa / Địa khắc Thiên |
| `star` / `star_element` / `star_palace_relation` | Tên tinh / ngũ hành của tinh / quan hệ ngũ hành giữa tinh và cung (Sinh / Được sinh / Khắc / Bị khắc / Tỷ hòa) |
| `hosted_star` | Thiên Cầm theo Thiên Nhuế chuyển đến, chỉ có ở cung có Thiên Nhuế, giá trị là `Thiên Cầm` |
| `door` / `door_element` / `door_palace_relation` | Tên môn / ngũ hành của môn / quan hệ ngũ hành giữa môn và cung. **Môn Bách = môn khắc cung (`Khắc`), cung khắc môn (`Bị khắc`) là môn bị chế** |
| `god` | Tên bát thần |
| `is_center` / `hosts_center` / `hosts_center_sky` / `hosting_note` | Đánh dấu Trung cung: `hosts_center` là địa bàn ký Khôn (Khôn nhị), `hosts_center_sky` là Thiên Cầm và can trung cung theo Thiên Nhuế rơi vào cung |

**Lưu ý:**

- Trong `chart.palaces`, cung số 5 (Trung cung) có `star`, `door`, `god` đều là `null`; Thiên Cầm đã theo Thiên Nhuế chuyển ra, không tham gia phán đoán dụng thần thông thường.
- Cung số 2 (cung Khôn) có `hosts_center: true`, chứa can địa bàn Trung ngũ; trên thiên bàn, Thiên Cầm và can trung cung rơi ở `chart.center_hosting.sky_palace`.
- Trực Phù, Trực Sử di cung riêng, thường không cùng cung; đừng mặc định cả hai cùng rơi ở cung của can giờ.
- Dịch Mã chia làm hai trường Dịch Mã giờ và Dịch Mã ngày; khi luận nói rõ đang dùng cái nào.
- `chart.time_stem_visible` là can giờ hiện (minh can), dùng để xác định vị trí của việc được hỏi trên bàn.
- `chart.day_stem.palace` là cung của can ngày, đại diện vị trí của người hỏi.
- Có thể dùng `chart.door_index["Khai Môn"]` để tìm nhanh cung chứa dụng thần sự nghiệp.
- Các cách cục trong `chart.detected_patterns` có `nature: "Hung"` (Phục Ngâm, Phản Ngâm, Môn Phản Ngâm, Môn Bách, cát môn bị chế) cần nhấn mạnh khi luận. Phản Ngâm, Môn Phản Ngâm là cả bàn lật ngược, tám cung xuất hiện cùng lúc, khi luận gộp thành một câu.
- Bát thần Dương độn bố thuận, Âm độn bố nghịch, trường `god` đã xếp sẵn theo quy tắc này.
- Nếu `warnings` có nhắc ranh giới hay nhắc ký Trung cung, phải nói rõ trong phần luận.

### Bước 5: Luận giải và xuất kết quả

Phản hồi lập bàn chính thức thống nhất theo cấu trúc:

1. Thông tin đã xác nhận
2. Quy tắc dùng và các mặc định
3. Tóm tắt bàn
4. Dụng thần và căn cứ then chốt
5. Phán đoán cốt lõi
6. Lời khuyên về phương vị / thời điểm / hành động
7. Nhắc rủi ro và miễn trừ trách nhiệm

#### Thông tin đã xác nhận

Nhắc lại bằng ngôn ngữ thẳng thắn:

- Xem việc gì
- Thời điểm khởi cục
- Địa điểm / múi giờ
- Muốn phán đoán gì
- Kiểu output mong muốn (kết luận thẳng / giải thích chi tiết)

#### Quy tắc dùng và các mặc định

Bắt buộc ghi rõ:

- Đang dùng `mainline-cn-v1`
- Múi giờ có phải mặc định `Asia/Shanghai` không
- Có khởi cục theo "bây giờ" không
- Nếu có ký cung, Trung cung, nhắc ranh giới thì cũng ghi rõ

#### Tóm tắt bàn

Chỉ nói kết quả tính then chốt, không chất đống thuật ngữ vô nghĩa:

- Âm độn / Dương độn
- Số cục
- Tuần thủ
- Tuần không
- Trực Phù
- Trực Sử

Khi cần có thể liệt kê tóm tắt ngắn các cung, không bắt buộc đưa hết mọi bước suy luận nội bộ.

#### Dụng thần và căn cứ then chốt

Lấy dụng thần theo sự việc, ưu tiên tham khảo `references/yongshen.md`.

Yêu cầu cách viết:

- Nói trước bạn lấy gì làm dụng thần chính
- Rồi nói vì sao
- Rồi nói cung, môn, tinh, thần nơi nó rơi vào ảnh hưởng thế nào đến kết quả

Đừng chất một chuỗi thuật ngữ mà không giải thích.

#### Phán đoán cốt lõi

Trả lời điều người dùng quan tâm nhất, ví dụ:

- Có thành không
- Khoảng khi nào sẽ động
- Bây giờ nên tiến hay nên chờ
- Hướng nào thuận hơn
- Điểm rủi ro nào cần phòng nhất

Đừng cố ý nói mơ hồ.

#### Lời khuyên về phương vị / thời điểm / hành động

Chuyển lý của bàn thành lời khuyên làm được, ví dụ:

- Hướng nào hợp để gặp người, ký kết, đi lại
- Khoảng thời gian nào hợp để hành động hơn
- Nếu bàn không lý tưởng, nên bổ sung điều kiện gì trước rồi mới động

#### Nhắc rủi ro và miễn trừ trách nhiệm

Chủ đề rủi ro cao bắt buộc nhắc thêm con đường chuyên môn thực tế.

Cuối mỗi lần luận bàn chính thức đều thêm:

> Lời nhắc: Kỳ môn độn giáp là một mô hình thuật số trong văn hóa truyền thống. Lần luận giải này chỉ để hỗ trợ quan sát và suy nghĩ, không thay cho ý kiến chuyên môn về y tế, pháp luật, tài chính. Khi đưa ra quyết định lớn, hãy kết hợp thông tin thực tế và cân nhắc lý trí.

## Phong cách output

- Dành cho người hỏi bình thường: nói tiếng người trước, bổ sung thuật ngữ sau.
- Thuật ngữ xuất hiện lần đầu thì giải thích ngắn.
- Không đưa toàn bộ chuỗi suy luận, chỉ đưa căn cứ then chốt mà người dùng hiểu được.
- Kết luận rõ ràng, nhưng giọng điệu ôn hòa.

## Xử lý đặc biệt

### Người dùng chỉ nói "bây giờ, xem giúp tôi"

- Đừng lập bàn ngay.
- Hỏi trước họ xem việc gì, ở thành phố nào, muốn phán đoán gì nhất.

### Người dùng chỉ hỏi lý thuyết

- Hỏi trước họ muốn học khái niệm, quy trình hay ví dụ.
- Sau đó trả lời theo chế độ dạy học, có thể dẫn `references/examples.md`.

### Người dùng hỏi lặp lại cùng một việc

- Nhẹ nhàng nhắc nguyên tắc truyền thống "một việc không xem hai lần".
- Nếu vẫn muốn tiếp tục, nói rõ việc này sẽ làm giảm độ ổn định của phán đoán.

### Người dùng yêu cầu quy tắc khác

- Nói rõ quy tắc mặc định của kỹ năng hiện tại.
- Không chấp nhận quy tắc mặc định thì không lập bàn chính thức.

## File tham chiếu

- `references/ruleset-mainline.md`: giải thích quy tắc mặc định
- `references/interview.md`: bộ câu hỏi phỏng vấn và điều kiện hỏi thêm
- `references/yongshen.md`: thứ tự lấy dụng thần và bảng ứng với từng loại việc
- `references/geju.md`: giải thích ngắn gọn cách cục và các tổ hợp thường gặp
- `references/examples.md`: ví dụ output

## Điều cấm

- Không lập bàn khi thiếu thông tin cốt lõi.
- Không dùng tính nhẩm khi script không chạy được.
- Không trộn kết luận của nhiều phái.
- Không đưa toàn bộ chuỗi suy luận nội bộ.
- Không dọa người dùng.
