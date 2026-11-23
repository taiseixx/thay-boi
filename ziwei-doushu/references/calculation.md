# Tham chiếu tính toán lập lá số Tử vi đẩu số

## Giới thiệu

File này ghi quy ước lập lá số mặc định của skill. Nguyên tắc chính:

- An sao theo an tinh quyết trước, rồi mới luận giải.
- Nếu cách nói giản lược trong dân gian mâu thuẫn với an tinh quyết thì theo an tinh quyết.
- Các chi tiết như đổi ngày ở giờ Tý, tháng nhuận, Mệnh chủ và Thân chủ: nếu người dùng đã quen theo một phần mềm hoặc một thầy nào đó thì ưu tiên giữ quy ước ấy và nói rõ chỗ khác biệt.

## 1. Thiên can, địa chi và giờ

### Mười thiên can và mười hai địa chi

- Mười thiên can: Giáp, Ất, Bính, Đinh, Mậu, Kỷ, Canh, Tân, Nhâm, Quý
- Mười hai địa chi: Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi, Thân, Dậu, Tuất, Hợi
- Can năm dương: Giáp, Bính, Mậu, Canh, Nhâm
- Can năm âm: Ất, Đinh, Kỷ, Tân, Quý

### Vị trí cố định của 12 địa chi trên lá số

```text
      Tỵ    Ngọ   Mùi   Thân
      Thìn              Dậu
      Mão               Tuất
      Dần   Sửu   Tý    Hợi
```

### Bảng đối chiếu giờ

| Giờ | Địa chi | Thời gian |
|------|------|------|
| giờ Tý | Tý | 23:00-00:59 |
| giờ Sửu | Sửu | 01:00-02:59 |
| giờ Dần | Dần | 03:00-04:59 |
| giờ Mão | Mão | 05:00-06:59 |
| giờ Thìn | Thìn | 07:00-08:59 |
| giờ Tỵ | Tỵ | 09:00-10:59 |
| giờ Ngọ | Ngọ | 11:00-12:59 |
| giờ Mùi | Mùi | 13:00-14:59 |
| giờ Thân | Thân | 15:00-16:59 |
| giờ Dậu | Dậu | 17:00-18:59 |
| giờ Tuất | Tuất | 19:00-20:59 |
| giờ Hợi | Hợi | 21:00-22:59 |

Quy ước mặc định:

- Skill này mặc định coi sau `23:00` là giờ Tý của ngày hôm sau.
- Nếu người dùng đã có lá số sẵn hoặc chỉ định rõ giữ nguyên ngày dương lịch, thì giữ quy ước của họ và nói rõ nguồn gốc khác biệt.

## 2. Định cung Mệnh và cung Thân

### Cung Mệnh

Khẩu quyết:

- Khởi tháng Giêng ở Dần, đếm thuận đến tháng sinh, rồi đếm nghịch đến giờ sinh, đó là cung Mệnh.

Các bước:

1. Từ cung Dần khởi tháng Giêng, đếm thuận đến cung ứng với tháng sinh âm lịch.
2. Từ cung đó khởi giờ Tý, đếm ngược chiều kim đồng hồ đến giờ sinh, cung dừng lại là cung Mệnh.

Ví dụ:

- Tháng 3 âm lịch, giờ Ngọ
- Dần = tháng Giêng, Mão = tháng 2, Thìn = tháng 3
- Từ cung Thìn khởi giờ Tý đếm nghịch đến giờ Ngọ: Thìn = Tý, Mão = Sửu, Dần = Dần, Sửu = Mão, Tý = Thìn, Hợi = Tỵ, Tuất = Ngọ
- Vậy cung Mệnh ở Tuất

### Cung Thân

Khẩu quyết:

- Khởi tháng Giêng ở Dần, đếm thuận đến tháng sinh, rồi đếm thuận đến giờ sinh, đó là cung Thân.

Các bước:

1. Bước đầu giống cung Mệnh.
2. Từ cung đó khởi giờ Tý, đếm thuận chiều kim đồng hồ đến giờ sinh, cung dừng lại là cung Thân.

Ghi chú chung:

- Cung Mệnh xem khí chất bẩm sinh và trục chính của đời người.
- Cung Thân xem biểu hiện hậu thiên và hướng dồn sức.
- Cung Thân luôn trùng với một trong các cung quan trọng: Mệnh, Thiên Di, Tài Bạch, Quan Lộc, Phu Thê, Phúc Đức.

## 3. An 12 cung

Sau khi có cung Mệnh, 12 cung luôn xếp ngược chiều kim đồng hồ:

- Mệnh
- Huynh Đệ
- Phu Thê
- Tử Tức
- Tài Bạch
- Tật Ách
- Thiên Di
- Nô Bộc (Giao Hữu)
- Quan Lộc (Sự Nghiệp)
- Điền Trạch
- Phúc Đức
- Phụ Mẫu

Ví dụ: nếu cung Mệnh ở Ngọ thì

- Ngọ = Mệnh
- Tỵ = Huynh Đệ
- Thìn = Phu Thê
- Mão = Tử Tức
- Dần = Tài Bạch
- Sửu = Tật Ách
- Tý = Thiên Di
- Hợi = Nô Bộc
- Tuất = Quan Lộc
- Dậu = Điền Trạch
- Thân = Phúc Đức
- Mùi = Phụ Mẫu

## 4. Khởi can cung Dần và can các cung

Khởi can cung Dần dùng để định thiên can của từng cung, về sau cần cho ngũ hành cục và phi hóa theo can cung.

Khẩu quyết:

- Năm Giáp, Kỷ khởi Bính Dần
- Năm Ất, Canh khởi Mậu Dần
- Năm Bính, Tân khởi Canh Dần
- Năm Đinh, Nhâm khởi Nhâm Dần
- Năm Mậu, Quý khởi Giáp Dần

Các bước:

1. Theo can năm sinh, xác định cung Dần mang can gì.
2. Từ cung Dần, xếp thuận thiên can lần lượt cho 12 cung.
3. Xếp xong là có can chi của từng cung.

Ví dụ: người sinh năm Giáp

- Dần = Bính Dần
- Mão = Đinh Mão
- Thìn = Mậu Thìn
- Tỵ = Kỷ Tỵ
- Ngọ = Canh Ngọ
- Mùi = Tân Mùi
- Thân = Nhâm Thân
- Dậu = Quý Dậu
- Tuất = Giáp Tuất
- Hợi = Ất Hợi
- Tý = Bính Tý
- Sửu = Đinh Sửu

## 5. Định ngũ hành cục

Skill này mặc định dùng quyết định ngũ hành cục, không coi tra bảng nạp âm là cách duy nhất.

### Quy tắc lấy số

- Số của thiên can:
  - Giáp, Ất = 1
  - Bính, Đinh = 2
  - Mậu, Kỷ = 3
  - Canh, Tân = 4
  - Nhâm, Quý = 5
- Số của địa chi:
  - Tý, Ngọ, Sửu, Mùi = 1
  - Dần, Thân, Mão, Dậu = 2
  - Thìn, Tuất, Tỵ, Hợi = 3

### Cách tính

1. Cộng số của can và số của chi trong can chi cung Mệnh.
2. Nếu kết quả lớn hơn 5 thì trừ 5 cho đến khi không lớn hơn 5.
3. Số còn lại ứng với ngũ hành:
   - 1 = Mộc Tam Cục
   - 2 = Kim Tứ Cục
   - 3 = Thủy Nhị Cục
   - 4 = Hỏa Lục Cục
   - 5 = Thổ Ngũ Cục

Ví dụ:

- Bính Tý: 2+1=3 -> Thủy -> Thủy Nhị Cục
- Tân Mùi: 4+1=5 -> Thổ -> Thổ Ngũ Cục
- Canh Thân: 4+2=6 -> 6-5=1 -> Mộc -> Mộc Tam Cục

## 6. An sao Tử Vi

Sao Tử Vi được định bằng ngày sinh âm lịch và số cục. Trong thực hành, cách chắc nhất là tra bảng.

### Bảng an sao Tử Vi

**Thủy Nhị Cục**

| Ngày | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|------|---|---|---|---|---|---|---|---|---|----|
| Tử Vi | Sửu | Dần | Dần | Mão | Mão | Thìn | Thìn | Tỵ | Tỵ | Ngọ |

| Ngày | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|------|----|----|----|----|----|----|----|----|----|----|
| Tử Vi | Ngọ | Mùi | Mùi | Thân | Thân | Dậu | Dậu | Tuất | Tuất | Hợi |

| Ngày | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|------|----|----|----|----|----|----|----|----|----|----|
| Tử Vi | Hợi | Tý | Tý | Sửu | Sửu | Dần | Dần | Mão | Mão | Thìn |

**Mộc Tam Cục**

| Ngày | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|------|---|---|---|---|---|---|---|---|---|----|
| Tử Vi | Thìn | Sửu | Dần | Tỵ | Dần | Mão | Ngọ | Mão | Thìn | Mùi |

| Ngày | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|------|----|----|----|----|----|----|----|----|----|----|
| Tử Vi | Thìn | Tỵ | Thân | Tỵ | Ngọ | Dậu | Ngọ | Mùi | Tuất | Mùi |

| Ngày | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|------|----|----|----|----|----|----|----|----|----|----|
| Tử Vi | Thân | Hợi | Thân | Dậu | Tý | Dậu | Tuất | Sửu | Tuất | Hợi |

**Kim Tứ Cục**

| Ngày | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|------|---|---|---|---|---|---|---|---|---|----|
| Tử Vi | Hợi | Thìn | Sửu | Dần | Tý | Tỵ | Dần | Mão | Sửu | Ngọ |

| Ngày | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|------|----|----|----|----|----|----|----|----|----|----|
| Tử Vi | Mão | Thìn | Dần | Mùi | Thìn | Tỵ | Mão | Thân | Tỵ | Ngọ |

| Ngày | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|------|----|----|----|----|----|----|----|----|----|----|
| Tử Vi | Thìn | Dậu | Ngọ | Mùi | Tỵ | Tuất | Mùi | Thân | Ngọ | Hợi |

**Thổ Ngũ Cục**

| Ngày | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|------|---|---|---|---|---|---|---|---|---|----|
| Tử Vi | Ngọ | Hợi | Thìn | Sửu | Dần | Mùi | Tý | Tỵ | Dần | Mão |

| Ngày | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|------|----|----|----|----|----|----|----|----|----|----|
| Tử Vi | Thân | Sửu | Ngọ | Mão | Thìn | Dậu | Dần | Mùi | Thìn | Tỵ |

| Ngày | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|------|----|----|----|----|----|----|----|----|----|----|
| Tử Vi | Tuất | Mão | Thân | Tỵ | Ngọ | Hợi | Thìn | Dậu | Ngọ | Mùi |

**Hỏa Lục Cục**

| Ngày | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|------|---|---|---|---|---|---|---|---|---|----|
| Tử Vi | Dậu | Ngọ | Hợi | Thìn | Sửu | Dần | Tuất | Mùi | Tý | Tỵ |

| Ngày | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|------|----|----|----|----|----|----|----|----|----|----|
| Tử Vi | Dần | Mão | Hợi | Thân | Sửu | Ngọ | Mão | Thìn | Tý | Dậu |

| Ngày | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|------|----|----|----|----|----|----|----|----|----|----|
| Tử Vi | Dần | Mùi | Thìn | Tỵ | Sửu | Tuất | Mão | Thân | Tỵ | Ngọ |

## 7. An 14 chính tinh

### 7.1 Chòm Tử Vi

Ý nghĩa khẩu quyết:

- Từ Tử Vi đi nghịch đến Thiên Cơ
- Cách một cung là Thái Dương, Vũ Khúc
- Liền tiếp Thiên Đồng
- Bỏ trống hai cung rồi an Liêm Trinh

Cách an mặc định:

- Tử Vi ở cung gốc
- Lùi 1 cung an Thiên Cơ
- Lùi tiếp 2 cung an Thái Dương
- Lùi tiếp 1 cung an Vũ Khúc
- Lùi tiếp 1 cung an Thiên Đồng
- Lùi tiếp 3 cung an Liêm Trinh

### 7.2 Sao Thiên Phủ

Mặc định theo quyết an sao Thiên Phủ:

- Thiên Phủ lấy Tử Vi làm mốc, hai sao đối xứng qua trục Dần – Thân (khi Tử Vi ở Dần hoặc Thân thì Thiên Phủ đồng cung)
- Không được hiểu là "Thiên Phủ luôn ở cung đối với Tử Vi"

Có thể dùng thẳng bảng dưới:

| Tử Vi ở cung | Thiên Phủ ở cung |
|----------|----------|
| Dần | Dần |
| Mão | Sửu |
| Thìn | Tý |
| Tỵ | Hợi |
| Ngọ | Tuất |
| Mùi | Dậu |
| Thân | Thân |
| Dậu | Mùi |
| Tuất | Ngọ |
| Hợi | Tỵ |
| Tý | Thìn |
| Sửu | Mão |

### 7.3 Chòm Thiên Phủ

Ý nghĩa khẩu quyết:

- Từ Thiên Phủ đi thuận đến Thái Âm
- Tiếp tục thuận: Tham Lang, Cự Môn, Thiên Tướng, Thiên Lương, Thất Sát
- Sau Thất Sát bỏ trống ba cung, đến cung thứ tư an Phá Quân

Cách an mặc định:

- Thiên Phủ ở cung gốc
- Thuận 1 cung an Thái Âm
- Thuận 1 cung an Tham Lang
- Thuận 1 cung an Cự Môn
- Thuận 1 cung an Thiên Tướng
- Thuận 1 cung an Thiên Lương
- Thuận 1 cung an Thất Sát
- Thuận tiếp 4 cung an Phá Quân

### 7.4 Kiểm tra các tổ hợp chính tinh thường gặp

Nếu an xong 14 chính tinh mà các quan hệ dưới đây hoàn toàn không khớp, hãy kiểm tra lại cách khởi Thiên Phủ trước:

- Tử Vi – Thiên Phủ đồng cung thường ở Dần, Thân
- Tử Vi – Tham Lang đồng cung thường ở Mão, Dậu
- Tử Vi – Thiên Tướng đồng cung thường ở Thìn, Tuất
- Tử Vi – Thất Sát đồng cung thường ở Tỵ, Hợi
- Tử Vi – Phá Quân đồng cung thường ở Sửu, Mùi

## 8. Phụ tinh hạng giáp

### Văn Xương, Văn Khúc (theo giờ sinh)

| Giờ | Tý | Sửu | Dần | Mão | Thìn | Tỵ | Ngọ | Mùi | Thân | Dậu | Tuất | Hợi |
|------|----|----|----|----|----|----|----|----|----|----|----|----|
| Văn Xương | Tuất | Dậu | Thân | Mùi | Ngọ | Tỵ | Thìn | Mão | Dần | Sửu | Tý | Hợi |
| Văn Khúc | Thìn | Tỵ | Ngọ | Mùi | Thân | Dậu | Tuất | Hợi | Tý | Sửu | Dần | Mão |

### Tả Phù, Hữu Bật (theo tháng sinh)

| Tháng | Giêng | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | Chạp |
|------|------|------|------|------|------|------|------|------|------|------|--------|--------|
| Tả Phù | Thìn | Tỵ | Ngọ | Mùi | Thân | Dậu | Tuất | Hợi | Tý | Sửu | Dần | Mão |
| Hữu Bật | Tuất | Dậu | Thân | Mùi | Ngọ | Tỵ | Thìn | Mão | Dần | Sửu | Tý | Hợi |

### Thiên Khôi, Thiên Việt (theo can năm)

| Can năm | Giáp | Ất | Bính | Đinh | Mậu | Kỷ | Canh | Tân | Nhâm | Quý |
|------|----|----|----|----|----|----|----|----|----|----|
| Thiên Khôi | Sửu | Tý | Hợi | Hợi | Sửu | Tý | Sửu | Ngọ | Mão | Mão |
| Thiên Việt | Mùi | Thân | Dậu | Dậu | Mùi | Thân | Mùi | Dần | Tỵ | Tỵ |

Khẩu quyết: Giáp Mậu Canh ở Trâu Dê (Sửu, Mùi), Ất Kỷ ở Chuột Khỉ (Tý, Thân), Bính Đinh ở Lợn Gà (Hợi, Dậu), Nhâm Quý ở Mèo Rắn (Mão, Tỵ), sáu Tân gặp Ngựa Hổ (Ngọ, Dần). Năm Đinh giống năm Bính: Khôi ở Hợi, Việt ở Dậu (bảng bản cũ ghi năm Đinh là Khôi Dậu, Việt Mùi, đã sửa).

### Lộc Tồn, Kình Dương, Đà La (theo can năm)

| Can năm | Giáp | Ất | Bính/Mậu | Đinh/Kỷ | Canh | Tân | Nhâm | Quý |
|------|----|----|--------|--------|----|----|----|----|
| Lộc Tồn | Dần | Mão | Tỵ | Ngọ | Thân | Dậu | Hợi | Tý |
| Kình Dương | Mão | Thìn | Ngọ | Mùi | Dậu | Tuất | Tý | Sửu |
| Đà La | Sửu | Dần | Thìn | Tỵ | Mùi | Thân | Tuất | Hợi |

### Hỏa Tinh, Linh Tinh (theo chi năm và giờ sinh)

Bảng điểm khởi:

| Nhóm chi năm | Dần Ngọ Tuất | Thân Tý Thìn | Tỵ Dậu Sửu | Hợi Mão Mùi |
|--------|--------|--------|--------|--------|
| Khởi Hỏa Tinh | Sửu | Dần | Mão | Dậu |
| Khởi Linh Tinh | Mão | Tuất | Tuất | Tuất |

Quy tắc:

- Tìm cung khởi theo nhóm chi năm.
- Từ cung khởi đặt giờ Tý, đếm thuận chiều kim đồng hồ đến giờ sinh.
- Cung dừng lại là nơi an Hỏa Tinh hoặc Linh Tinh.

### Địa Không, Địa Kiếp (theo giờ sinh)

| Giờ | Tý | Sửu | Dần | Mão | Thìn | Tỵ | Ngọ | Mùi | Thân | Dậu | Tuất | Hợi |
|------|----|----|----|----|----|----|----|----|----|----|----|----|
| Địa Không | Hợi | Tuất | Dậu | Thân | Mùi | Ngọ | Tỵ | Thìn | Mão | Dần | Sửu | Tý |
| Địa Kiếp | Hợi | Tý | Sửu | Dần | Mão | Thìn | Tỵ | Ngọ | Mùi | Thân | Dậu | Tuất |

### Thiên Mã (theo chi năm)

| Nhóm chi năm | Dần Ngọ Tuất | Thân Tý Thìn | Tỵ Dậu Sửu | Hợi Mão Mùi |
|--------|--------|--------|--------|--------|
| Thiên Mã | Thân | Dần | Hợi | Tỵ |

## 9. Một số sao hạng ất thường dùng

Dùng khi cần:

- Thiên Hình: tháng Giêng khởi ở Dậu, đi thuận
- Thiên Diêu: tháng Giêng khởi ở Sửu, đi thuận
- Hồng Loan: từ cung Mão khởi Tý, đếm nghịch đến chi năm sinh
- Thiên Hỷ: ở cung đối của Hồng Loan
- Cô Thần, Quả Tú: an theo nhóm tam hợp của chi năm
- Thiên Khốc, Thiên Hư: từ cung Ngọ khởi Tý, Thiên Khốc đếm nghịch, Thiên Hư đếm thuận

Nếu người dùng chỉ cần lá số giản lược thì có thể chưa cần triển khai sao hạng ất.

## 10. Đại hạn

### Tuổi khởi hạn

- Thủy Nhị Cục: 2 tuổi
- Mộc Tam Cục: 3 tuổi
- Kim Tứ Cục: 4 tuổi
- Thổ Ngũ Cục: 5 tuổi
- Hỏa Lục Cục: 6 tuổi

### Quy tắc thuận nghịch

- Dương nam, âm nữ: từ cung Mệnh đi thuận
- Âm nam, dương nữ: từ cung Mệnh đi nghịch

### Ghi chú

- Mỗi cung quản 10 năm.
- Đại hạn đầu tiên bắt đầu từ tuổi khởi hạn và kết thúc ở tuổi khởi hạn cộng 9.
- Khi người dùng hỏi lưu niên, xác định đại hạn hiện tại trước, rồi mới chồng tứ hóa lưu niên lên.

## 11. Mệnh chủ và Thân chủ

Skill này mặc định dùng quy ước thường gặp dưới đây:

### Sao Mệnh chủ (theo địa chi cung Mệnh)

| Địa chi cung Mệnh | Tý | Sửu | Dần | Mão | Thìn | Tỵ | Ngọ | Mùi | Thân | Dậu | Tuất | Hợi |
|----------|----|----|----|----|----|----|----|----|----|----|----|----|
| Mệnh chủ | Tham Lang | Cự Môn | Lộc Tồn | Văn Khúc | Liêm Trinh | Vũ Khúc | Phá Quân | Vũ Khúc | Liêm Trinh | Văn Khúc | Lộc Tồn | Cự Môn |

### Sao Thân chủ (theo chi năm sinh)

| Chi năm | Tý | Sửu | Dần | Mão | Thìn | Tỵ | Ngọ | Mùi | Thân | Dậu | Tuất | Hợi |
|------|----|----|----|----|----|----|----|----|----|----|----|----|
| Thân chủ | Hỏa Tinh | Thiên Tướng | Thiên Lương | Thiên Đồng | Văn Xương | Thiên Cơ | Hỏa Tinh | Thiên Tướng | Thiên Lương | Thiên Đồng | Văn Xương | Thiên Cơ |

## 12. Danh sách tự kiểm tra lá số

Lập xong lá số, rà lại theo danh sách sau:

- Cung Mệnh, cung Thân và thứ tự 12 cung có đúng không
- Can các cung sau khi khởi can cung Dần có liên tục, không sai không
- Ngũ hành cục có khớp với can chi cung Mệnh không
- Cách khởi Tử Vi và Thiên Phủ có dùng cùng một bộ khẩu quyết không
- 14 chính tinh đã an đủ, không trùng, không sót
- Tứ hóa có gắn vào sao thật sự có trên lá số không
- Chiều đại hạn có khớp với giới tính và âm dương của can năm không

Nếu thấy bất thường rõ, ưu tiên kiểm tra lại:

1. Giờ Tý có đổi ngày không
2. Tháng âm lịch có phải tháng nhuận không
3. Can cung Mệnh có tính sai không
4. Cách khởi Thiên Phủ có lỡ dùng "cách nói giản lược đối xứng trục" không

## 13. Quy ước lập lá số của script

Lá số chính thức do `scripts/ziwei_cli.py` lập. Các bảng trong file này chính là quy ước của script, và `scripts/tests/` sẽ đối chiếu từng ô giữa hằng số trong script với các bảng của file này, `sihua.md` và `stars.md`. Các quy ước chi tiết ngoài file này:

| Hạng mục | Quy ước của script | Trường input |
|---|---|---|
| Ranh giới năm | Đổi năm vào mùng 1 tháng Giêng âm lịch, can chi năm lấy theo năm âm lịch (không đổi năm theo Lập Xuân) | — |
| Tháng, ngày | Dùng tháng, ngày âm lịch; ngày sinh dương lịch sẽ được `lunar_python` quy đổi | `calendar_type` |
| Đổi ngày ở giờ Tý | Mặc định từ 23:00 coi là giờ Tý của ngày hôm sau, ngày âm lịch tính theo hôm sau (xem §1). Nếu quy ước của người dùng là không đổi ngày thì truyền `same_day`: vẫn lấy giờ Tý nhưng giữ nguyên ngày | `late_zi_rule`: `next_day` (mặc định) / `same_day` |
| Tháng nhuận | Mặc định `split_15`: tháng nhuận từ ngày 15 trở về trước tính theo tháng hiện tại, từ ngày 16 tính theo tháng sau (ví dụ ngày 16 tháng 2 nhuận tính là tháng 3). Nếu người dùng có quy ước riêng thì truyền `current` (cả tháng theo tháng hiện tại) hoặc `next` (cả tháng theo tháng sau). Output `normalized_input.leap_month_rule` và `ruleset.leap_month_rule` ghi rõ thuật toán đã dùng, `source` là `default` (không truyền, dùng mặc định) hoặc `explicit` (bên gọi chỉ định); sinh tháng nhuận thì `warnings` cũng ghi chú | `leap_month_rule`: `split_15` (mặc định) / `current` / `next` |
| Phạm vi ảnh hưởng của tháng nhuận | Chỉ trực tiếp ảnh hưởng các sao an theo tháng: cung Mệnh, cung Thân, Tả Phù, Hữu Bật, Thiên Hình, Thiên Diêu; năm và ngày không đổi. Cung Mệnh đổi thì can cung, ngũ hành cục và chòm Tử Vi (an theo cục) cũng đổi theo | — |
| Tuổi đại hạn | Tuổi mụ | — |
| Lưu niên | Cung Mệnh lưu niên ở cung mang địa chi của năm xem; tứ hóa lưu niên lấy theo can năm xem; tứ hóa đại hạn lấy theo can cung của đại hạn hiện tại (xem phần "Tứ hóa vận hạn" trong `sihua.md`) | `query_year` (năm âm lịch, không bắt buộc) |
| Giờ sinh | Lấy giờ âm lịch thẳng từ giờ đồng hồ người dùng xác nhận, không tự hiệu chỉnh giờ mặt trời thật hay giờ mùa hè; cần hiệu chỉnh thì tự quy đổi trước rồi mới truyền vào | `birth_time` |
| Sao hạng ất | Chỉ an các sao ở §9 có quy tắc đầy đủ: Thiên Hình, Thiên Diêu, Hồng Loan, Thiên Hỷ, Thiên Khốc, Thiên Hư. Cô Thần, Quả Tú chưa có bảng trong file này nên script không an | — |
| Miếu vượng lợi hãm | 14 chính tinh xuất theo bảng miếu vượng hãm trong `stars.md` (bảng tổng ở quyển 2 sách *Tử Vi Đẩu Số Toàn Thư*, nguồn và dị bản xem chú thích dưới bảng) | — |
| Ngôn ngữ output | Mặc định chuyển toàn bộ thuật ngữ trong output sang tiếng Việt (`vi_terms.py`). Truyền `"lang": "zh"` nếu muốn giữ chữ Hán như bản gốc | `lang`: `vi` (mặc định) / `zh` |

Lập xong script sẽ tự kiểm tra: 14 chính tinh đủ và không trùng; tổ hợp Tử Vi đồng cung chỉ rơi vào các cung liệt kê ở §7.4 (ví dụ Tử Vi – Thất Sát chỉ ở Tỵ, Hợi); các sao tứ hóa đều có trên lá số. Không qua kiểm tra thì báo lỗi ngay, không xuất lá số.

Nguồn giá trị kỳ vọng cho test hồi quy: các bảng và ví dụ trong file này, suy ra từ an tinh quyết (duyệt hết 5 cục × 30 ngày để kiểm tra cung của các tổ hợp sao đôi với Tử Vi), bảng nạp âm Lục thập hoa giáp của `lunar_python` (để đối chiếu ngũ hành cục), và 120 lá số mẫu của thư viện lập lá số mã nguồn mở iztro 2.6.2 (đối chiếu từng sao, gồm cả miếu vượng lợi hãm của chính tinh; có thể tạo lại bằng `scripts/tests/fixtures/gen_iztro_cases.cjs`).
