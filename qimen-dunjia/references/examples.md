# Ví dụ output

File này minh họa hai loại tình huống: lập bàn chính thức (có ánh xạ từ output script thật → luận giải) và chế độ học lý thuyết.

---

## Ví dụ 1: Lập bàn chính thức (nhảy việc)

### Thông tin đã xác nhận qua phỏng vấn

- Sự việc: nhảy việc / đổi công việc
- Thời điểm khởi cục: 2026-03-24 10:30 (dương lịch)
- Địa điểm: Thượng Hải (China/Asia/Shanghai)
- Mục tiêu: có nên động không, khi nào động thì chắc hơn
- Kiểu output: kết luận thẳng

### Output then chốt của script (tóm tắt)

Sau khi chạy script, lấy các trường then chốt sau từ JSON output (đã chuyển ngữ với `lang: vi`):

```
calendar.jieqi.active_jie: Xuân Phân   ← từ 2026-03-20, đã qua Xuân Phân, không được định cục theo Kinh Trập nữa

ganzhi:
  year:  Bính Ngọ
  month: Tân Mão
  day:   Đinh Dậu
  time:  Ất Tỵ
  time_xun:     Giáp Thìn
  time_xunkong: Dần Mão

chart:
  dun_type:          Dương độn
  yuan:              Thượng nguyên
  ju_number:         3
  xunshou:           Giáp Thìn
  hidden_yi:         Nhâm
  kongwang:          [Dần, Mão]
  kongwang_palaces:  [3, 8]  ← cung Chấn (Đông), cung Cấn (Đông Bắc) tuần không
  day_kongwang:      [Thìn, Tỵ]
  day_kongwang_palaces: [4]  ← tuần không của ngày ảnh hưởng cả ngày
  time_stem_visible: Ất      ← đại diện việc được hỏi
  day_stem:          { stem: Đinh, palace: 9 }  ← người hỏi
  year_stem:         { stem: Bính, palace: 1 }  ← cấp trên / đại cục
  month_stem:        { stem: Tân, palace: 6 }  ← đồng nghiệp / đối thủ
  hour_yima:         { branch: Hợi, palace: 6, source_branch: Tỵ }  ← Dịch Mã giờ ở cung Càn (Tây Bắc)
  day_yima:          { branch: Hợi, palace: 6, source_branch: Dậu }  ← Dịch Mã ngày cũng ở cung Càn

  zhifu:  { star: Thiên Trụ, palace: 2 }  ← theo can giờ Ất rơi cung Khôn (Tây Nam)
  zhishi: { door: Kinh Môn, palace: 8, raw_palace: 8, hours_from_xunshou: 1 }  ← từ Đoài thất (nơi có Nhâm của tuần thủ) đi thuận một cung, rơi cung Cấn (Đông Bắc)
  center_hosting: { hosted_star: Thiên Cầm, center_stem: Canh, earth_host_palace: 2, sky_palace: 9, follows_star: Thiên Nhuế }

  door_index: { Tử Môn: 1, Thương Môn: 2, Khai Môn: 3, Hưu Môn: 4, Cảnh Môn: 6, Đỗ Môn: 7, Kinh Môn: 8, Sinh Môn: 9 }
  star_index: { Thiên Nhậm: 1, Thiên Trụ: 2, Thiên Phụ: 3, Thiên Anh: 4, Thiên Bồng: 6, Thiên Tâm: 7, Thiên Xung: 8, Thiên Nhuế: 9, Thiên Cầm: 9 }

  detected_patterns:
    - { name: Môn Bách, palace: 1, detail: "Tử Môn (Thổ) khắc cung Khảm (Thủy)", nature: Hung }
    - { name: Môn Bách, palace: 2, detail: "Thương Môn (Mộc) khắc cung Khôn (Thổ)", nature: Hung }
    - { name: Môn Bách, palace: 3, detail: "Khai Môn (Kim) khắc cung Chấn (Mộc)", nature: Hung }
    - { name: Tam Kỳ phối Cát Môn, palace: 4, detail: "Đinh + Hưu Môn", nature: Cát }
    - { name: Môn Bách, palace: 6, detail: "Cảnh Môn (Hỏa) khắc cung Càn (Kim)", nature: Hung }
    - { name: Môn Thụ Chế, palace: 7, detail: "Đỗ Môn (Mộc) bị cung Đoài (Kim) khắc", nature: Trung }
    - { name: Tam Kỳ phối Cát Môn, palace: 9, detail: "Ất + Sinh Môn", nature: Cát }

palaces (một phần):
  Cung 2 cung Khôn / Tây Nam: địa bàn Ất / thiên bàn Nhâm / Thiên Trụ / Thương Môn (Mộc, Khắc) / Trực Phù / stem_relation: Thiên sinh Địa ← nơi có can giờ Ất, nơi có Trực Phù
  Cung 3 cung Chấn / Đông:    địa bàn Mậu / thiên bàn Kỷ / Thiên Phụ (Mộc, Tỷ hòa) / Khai Môn (Kim, Khắc) / Huyền Vũ / stem_relation: Tỷ hòa ← nơi có dụng thần chính Khai Môn, tuần không của giờ
  Cung 8 cung Cấn / Đông Bắc: địa bàn Quý / thiên bàn Mậu / Thiên Xung / Kinh Môn (Kim, Được sinh) / Bạch Hổ / stem_relation: Thiên khắc Địa ← nơi có Trực Sử, tuần không của giờ
  Cung 9 cung Ly / Nam:       địa bàn Đinh / thiên bàn Ất + Canh / Thiên Nhuế + Thiên Cầm (Thổ, Được sinh) / Sinh Môn (Thổ, Được sinh) / Cửu Thiên / stem_relation: Thiên sinh Địa ← nơi có can ngày Đinh
```

### Quá trình đọc bàn (nội bộ, không đưa cho người dùng)

1. **Dụng thần chính**: sự nghiệp / nhảy việc → lấy Khai Môn làm dụng thần chính, phụ xem Trực Phù, Trực Sử và can ngày (Đinh). Từ `door_index` biết Khai Môn ở cung 3.
2. **Cung của Khai Môn**: cung 3 Chấn (Đông), Khai Môn (Kim) khắc cung Chấn (Mộc) → Môn Bách; phối Thiên Phụ, Huyền Vũ, và cung 3 tuần không của giờ → ý muốn thúc đẩy đang đối đầu hoàn cảnh, thông tin có phần hư, điều kiện chưa thành hiện thực.
3. **Người hỏi (can ngày Đinh)**: `day_stem.palace` = cung 9 Ly (Nam), phối Sinh Môn, Thiên Nhuế + Thiên Cầm, Cửu Thiên, thiên bàn Ất với Sinh Môn thành "Tam Kỳ phối Cát Môn" → bản thân có nguồn lực và chỗ dựa, trạng thái không tệ.
4. **Việc được hỏi (can giờ Ất)**: rơi cung 2 Khôn (Tây Nam), cùng cung với Trực Phù Thiên Trụ, nhưng Thương Môn bị Môn Bách → bản thân việc này có trọng lượng, khi thúc đẩy dễ va chạm, có hao tổn.
5. **Trực Phù, Trực Sử**: Trực Phù Thiên Trụ ở Khôn nhị, Trực Sử Kinh Môn ở Cấn bát, rơi cung riêng. Cung Cấn bát nơi có Trực Sử bị tuần không của giờ, phối Bạch Hổ → kênh hành động hiện tại kèm kinh động, khẩu thiệt, mà lại rơi vào không.
6. **Nhắc cách cục**: Môn Bách tập trung ở cung 1, 2, 3, 6; cát cách ở cung 4 (Đinh + Hưu Môn, nhưng cung 4 tuần không của ngày) và cung 9 (Ất + Sinh Môn, cùng cung với bản thân).
7. **Dịch Mã**: Dịch Mã giờ, Dịch Mã ngày đều ở cung 6 Càn (Tây Bắc), nhưng cung 6 Cảnh Môn bị Môn Bách → có ý định thay đổi, nhưng hướng đi ra ngoài không thuận.
8. **Tuần không**: tuần không của giờ Dần Mão → cung 3 (Đông) + cung 8 (Đông Bắc), đè đúng lên Khai Môn và Trực Sử; tuần không của ngày Thìn Tỵ → cung 4 (Đông Nam) cả ngày thiên về hư.

### Output chính thức (cho người dùng)

---

**Thông tin đã xác nhận**

- Xem việc gì: nhảy việc, phán đoán có nên động không, khi nào động thì chắc hơn
- Thời điểm khởi cục: 2026-03-24 10:30, Thượng Hải (múi giờ châu Á / Thượng Hải)
- Kiểu output: kết luận thẳng

**Quy tắc dùng và các mặc định**

- Bộ quy tắc: `mainline-cn-v1` (Thời gia Chuyển bàn Kỳ môn)
- Múi giờ: `Asia/Shanghai` (mặc định)
- Tiết khí hiện tại: Xuân Phân

**Tóm tắt bàn**

- Dương độn cục 3
- Tuần thủ: Giáp Thìn, nghi của tuần thủ: Nhâm
- Tuần không: Dần, Mão (phương Đông và Đông Bắc sức lực thiên về hư)
- Trực Phù: Thiên Trụ · cung Khôn (Tây Nam)
- Trực Sử: Kinh Môn · cung Cấn (Đông Bắc)

**Dụng thần và căn cứ then chốt**

Chủ yếu xem Khai Môn (đại diện việc thúc đẩy sự nghiệp), phụ xem Trực Phù, Trực Sử và can ngày.

- Khai Môn rơi cung Chấn (Đông), môn khắc cung thành Môn Bách, lại gặp tuần không, phối Huyền Vũ: hướng bạn muốn đi hiện điều kiện chưa thật, thông tin phía bên kia đưa ra cũng có thể có phần "thổi phồng".
- Bản thân bạn (can ngày Đinh) rơi cung Ly (Nam), phối Sinh Môn, Cửu Thiên, Ất kỳ gia Sinh Môn: nguồn lực và chỗ dựa của bạn là đủ, không phải bị ép phải đi.
- Việc được hỏi (can giờ Ất) cùng ở cung Khôn với Trực Phù, nhưng Thương Môn bị Môn Bách: việc này không nhẹ, cố đẩy dễ va chạm, có hao tổn.
- Trực Sử Kinh Môn rơi cung Cấn, tuần không lại phối Bạch Hổ: hành động trước mắt phần nhiều là hoảng hão hoặc khẩu thiệt, không đi đến thực chất.

**Phán đoán cốt lõi**

- Có nên động không: có cơ sở để động, nhưng bây giờ chưa phải lúc chốt.
- Khi nào động thì chắc hơn: Khai Môn và Trực Sử đều rơi cung tuần không, trước mắt hợp để thăm dò kín (lương, đội nhóm, ranh giới trách nhiệm), đợi điều kiện có trên giấy rồi mới chính thức thúc đẩy.

**Lời khuyên về phương vị / thời điểm / hành động**

- Cơ hội ở phương Nam hợp với trạng thái của bạn hơn, có thể ưu tiên tiếp xúc.
- Cơ hội ở phương Đông, Đông Bắc thì kiểm chứng thông tin trước, chưa vội tỏ thái độ.
- Nếu đã có offer trong tay, đàm phán rõ các điều khoản then chốt trước, không cần nghỉ việc trong mấy ngày này.

**Nhắc rủi ro và miễn trừ trách nhiệm**

Quyết định kiểu này còn phải xét tổng hợp điều kiện offer thật, dòng tiền, rủi ro thời gian thử việc.

> Lời nhắc: Kỳ môn độn giáp là một mô hình thuật số trong văn hóa truyền thống. Lần luận giải này chỉ để hỗ trợ quan sát và suy nghĩ, không thay cho ý kiến chuyên môn về y tế, pháp luật, tài chính. Khi đưa ra quyết định lớn, hãy kết hợp thông tin thực tế và cân nhắc lý trí.

---

## Ví dụ 2: Chế độ học lý thuyết

### Tình huống

Người dùng hỏi: Trực Phù và Trực Sử nghĩa là gì?

### Cách xử lý

Không lập bàn chính thức. Xác nhận nhu cầu học trước, rồi giải thích:

---

**Trực Phù**: "tinh thần chủ đạo" của cục, đại diện hướng lực lượng có uy quyền, có sức chủ đạo nhất trong khoảng thời gian hiện tại. Cung nó rơi vào quyết định "ai nói là được" trên cả bàn, là căn cứ then chốt để phán quyền chủ động và nguồn hỗ trợ.

**Trực Sử**: "cửa thực thi" của cục, đại diện kênh hành động sôi nổi nhất hiện tại. Tên cửa của nó (Hưu / Sinh / Thương / Đỗ / Cảnh / Tử / Kinh / Khai) ảnh hưởng trực tiếp đến việc hiện tại nên làm gì.

**Quan hệ giữa hai cái:**

- Hai cái di cung riêng: Trực Phù theo can giờ, Trực Sử từ cung tuần thủ đi từng cung theo giờ, Dương độn đi thuận, Âm độn đi nghịch. Vì vậy phần lớn thời gian hai cái không cùng cung.
- Như ví dụ 1, Trực Phù (Thiên Trụ) ở cung Khôn, Trực Sử (Kinh Môn) ở cung Cấn: lực lượng chủ đạo và kênh hành động nằm ở hai chỗ, mà kênh hành động lại gặp tuần không, cho thấy có người quyết, nhưng hành động thực tế vẫn còn hư.
- Nếu ở một giờ nào đó hai cái vừa khéo cùng cung, nghĩa là "lực lượng chủ đạo" và "kênh hành động" tụ ở một chỗ, sức mạnh tập trung, các cung khác tương đối yếu.

**Muốn xem ví dụ bàn thực tế?** Có thể kể cho mình một việc cụ thể, mình sẽ đi theo quy trình lập bàn chính thức, tiện thể giảng từng bước lấy Trực Phù, Trực Sử thế nào.
