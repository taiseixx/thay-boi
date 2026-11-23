# Quy tắc mặc định `mainline-cn-v1`

Việc lập bàn chính thức của skill này chỉ dùng một bộ quy tắc mặc định, không trộn cách nói khác vào phần tính chính thức.

## Phạm vi áp dụng

- Theo thói quen dùng Thời gia Chuyển bàn Kỳ môn phổ biến ở Trung Quốc đại lục
- Múi giờ mặc định của script: `Asia/Shanghai`
- Người dùng ở nước ngoài (kể cả Việt Nam) phải bổ sung thành phố hoặc múi giờ trước; người dùng ở Việt Nam dùng `Asia/Ho_Chi_Minh`

## Quy tắc cố định

### 1. Quy tắc thời gian

- Người dùng nói "bây giờ" thì khởi cục theo thời điểm tuyệt đối hiện tại.
- Không có múi giờ và ngữ cảnh là Trung Quốc đại lục thì mặc định giờ Bắc Kinh.
- Người dùng ở nước ngoài không có múi giờ thì hỏi thêm trước, không lập bàn ngay.

### 2. Quy tắc tiết khí

- Dùng 24 tiết khí (12 tiết + 12 trung khí) để chuyển Âm độn / Dương độn và định cục; tiết khí hiện tại lấy tiết khí gần nhất trước thời điểm khởi cục.
- Từ Đông Chí đến Mang Chủng: Dương độn
- Từ Hạ Chí đến Đại Tuyết: Âm độn
- Không được chỉ xem 12 tiết: các trung khí như Đông Chí, Xuân Phân, Hạ Chí mỗi cái ứng với một bộ số cục riêng. Chỉ lấy tiết sẽ làm nửa tháng sau trung khí dùng nhầm cục của tiết trước, sau Đông Chí, Hạ Chí còn lấy ngược Âm Dương độn.
- Trong vòng 24 giờ trước và sau ranh giới tiết khí, output phải ghi rõ "nhắc ranh giới".

### 3. Quy tắc tam nguyên

- Chia nhóm theo vị trí của can chi ngày trong Lục thập hoa giáp.
- Mỗi 5 ngày là một nguyên.
- Thứ tự cố định lặp vòng: Thượng nguyên -> Trung nguyên -> Hạ nguyên.

Đây là quy tắc cố định mang tính kỹ thuật mà phiên bản hiện tại dùng, để đảm bảo cùng một input luôn cho cùng một kết quả.

### 4. Quy tắc định cục

- Sau khi xác định Âm / Dương độn và tam nguyên, lấy số cục thẳng từ bảng định cục cố định.
- Không tạm chuyển sang phép Sách bổ hay biến thể khác khi lập bàn chính thức.

### 5. Quy tắc Trung cung

- Mọi phán đoán liên quan đến Trung cung đều xử lý theo ký Khôn.
- Nếu nghi mà tuần thủ ẩn vào hoặc can giờ rơi vào Trung cung, output chính thức phải nhắc "bàn này xử lý theo ký Khôn".
- Địa bàn: can địa bàn Trung ngũ ký ở Khôn nhị.
- Thiên bàn: Thiên Cầm ký Khôn và nhập vào Thiên Nhuế; Thiên Cầm và can địa bàn Trung ngũ cùng theo Thiên Nhuế mà chuyển, rơi vào cung Thiên Nhuế đến. Thiên bàn của cung đó đồng thời có hai can (can địa bàn Khôn nhị + can địa bàn Trung ngũ), output ở `sky_stems`, `hosted_sky_stem`, `hosted_star`; `chart.center_hosting.sky_palace` cho biết cung sau khi chuyển.
- Bản thân Trung ngũ không đặt tinh nữa: Thiên Cầm đã theo Thiên Nhuế chuyển ra.

### 6. Quy tắc điểm khởi thiên bàn

- Điểm tham chiếu để xếp kỳ nghi trên thiên bàn là nghi mà tuần thủ ẩn vào (đại diện vị trí của Giáp).
- Trường hợp thường: nghi đó nằm trong vòng tám cung thì lấy luôn làm điểm khởi thiên bàn.
- Trường hợp đặc biệt: nghi đó trên địa bàn rơi vào Trung cung (cung 5) thì ký sang cung Khôn (cung 2), thiên bàn khởi xếp từ can địa bàn của cung Khôn. Trung cung không nằm trong vòng chuyển bàn tám cung, sau khi ký Khôn thì "hình chiếu trên vòng" của nghi chính là can địa bàn cung Khôn.

### 7. Quy tắc Trực Phù, Trực Sử

- Sao Trực Phù: là sao trong cửu tinh ở cung địa bàn nơi nghi của tuần thủ ẩn vào, theo thiên bàn chuyển đến cung của can giờ.
- Cửa Trực Sử: là cửa trong bát môn ở cung địa bàn nơi nghi của tuần thủ ẩn vào, **di cung riêng với Trực Phù**: khởi từ cung địa bàn của tuần thủ, giờ tuần thủ tính là bước 0, sau đó mỗi giờ đi một cung theo thứ tự số cửu cung, Dương độn đi thuận (1→2→…→9→1), Âm độn đi nghịch (9→8→…→1→9). Đi qua Trung ngũ vẫn đếm bình thường, cuối cùng rơi Trung ngũ thì ký Khôn nhị.
- Định xong cung của Trực Sử, bảy cửa còn lại xoay theo đúng thứ tự tương đối ban đầu. Trực Phù và Trực Sử chỉ cùng cung khi số giờ vừa khớp.
- Nếu tuần thủ rơi Trung cung thì lấy tinh và môn của cung Khôn sau khi ký Khôn (Thiên Cầm ký Khôn nhập vào Thiên Nhuế, Trung cung không có môn thì lấy Tử Môn); Trực Sử vẫn tính di cung từ Trung ngũ.
- Căn cứ: *Yên Ba Điếu Tẩu ca*: "Trực Phù thường khiến gia lên can giờ, Trực Sử thuận nghịch theo cung mà đi"; *Độn Giáp Diễn Nghĩa* quyển 1, "Bát môn cửu tinh trục thời di cung quyết": Dương nhất cục giờ Ất Sửu sao Bồng ở cung 9, Hưu Môn ở cung 2; giờ Bính Dần sao Bồng ở cung 8, Hưu Môn ở cung 3.

### 8. Quy tắc Môn Bách

- Môn khắc cung là Môn Bách, cung khắc môn là môn bị chế (Môn Thụ Chế), không được lẫn lộn. Căn cứ: *Độn Giáp Diễn Nghĩa*: "Cung chế môn không phải bách, môn chế cung mới là bách".
- Trong `detected_patterns`, Môn Bách đánh dấu `nature: "Hung"`; Môn Thụ Chế với cát môn đánh dấu `"Hung"` (cát môn bị khắc thì cát không thành), với các môn khác đánh dấu `"Trung"`.

### 9. Quy tắc Phản Ngâm

- Tinh rơi vào cung xung đối của cung gốc là Phản Ngâm (Khảm nhất ↔ Ly cửu, Cấn bát ↔ Khôn nhị, Chấn tam ↔ Đoài thất, Tốn tứ ↔ Càn lục); can thiên bàn chuyển cùng tinh, lúc này can thiên bàn cũng gia lên cung xung đối với vị trí gốc, như "Tý đến gia Ngọ". Căn cứ: *Độn Giáp Diễn Nghĩa*: "Phàm tinh phù đối xung đều là Phản Ngâm".
- Môn rơi vào cung xung đối của cung gốc là Môn Phản Ngâm. Bát môn và cửu tinh di cung riêng, mỗi cái phán đoán riêng.
- Không phán Phản Ngâm theo ngũ hành sinh khắc của can thiên bàn và địa bàn.

### 10. Quy tắc bát thần

- Thứ tự bát thần: Trực Phù, Đằng Xà, Thái Âm, Lục Hợp, Bạch Hổ, Huyền Vũ, Cửu Địa, Cửu Thiên. Thần Trực Phù theo sao Trực Phù rơi vào cung của can giờ.
- Dương độn từ Trực Phù bố thuận chiều kim đồng hồ (Khảm → Cấn → Chấn → Tốn → Ly → Khôn → Đoài → Càn), Âm độn từ Trực Phù bố ngược chiều kim đồng hồ.

### 11. Quy tắc Dịch Mã

- Xuất riêng Dịch Mã giờ và Dịch Mã ngày, không gộp thành một trường:
  - `hour_yima`: lấy Dịch Mã theo tam hợp cục của chi giờ (Thời gia Kỳ môn hay dùng).
  - `day_yima`: lấy Dịch Mã theo tam hợp cục của chi ngày.
- Cả hai đều có `source_branch` ghi rõ lấy từ địa chi nào. Thân Tý Thìn mã ở Dần, Dần Ngọ Tuất mã ở Thân, Hợi Mão Mùi mã ở Tỵ, Tỵ Dậu Sửu mã ở Hợi.

### 12. Quy tắc trình bày

- Không đưa toàn bộ chuỗi suy luận.
- Chỉ đưa kết quả tính then chốt và căn cứ cần thiết.
- Thứ người dùng chủ yếu thấy: Âm Dương độn, số cục, tuần thủ, tuần không, Trực Phù, Trực Sử, dụng thần then chốt.

## Các trường hợp không hỗ trợ

Các trường hợp sau không lập bàn chính thức:

- Người dùng yêu cầu rõ chuyển sang quy tắc khác và không chấp nhận quy tắc mặc định hiện tại
- Thiếu thông tin thời gian hoặc địa điểm
- Muốn mô hình bỏ qua script mà tính tay trực tiếp
