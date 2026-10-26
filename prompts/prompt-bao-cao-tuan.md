# PROMPT — BÁO CÁO TUẦN & DASHBOARD

> Tri thức: `ts-F`.

---

## 1 · Báo cáo tuần

```
Dựng báo cáo tuần từ bản chấm [n] cuộc.

Bảy mục, đúng thứ tự:
1. BA DÒNG BẮT BUỘC — kiểu mẫu · cỡ mẫu (+ số cuộc loại và lý do) · nguồn, kỳ, giờ cập nhật
2. CHỈ SỐ TIẾN TRÌNH — tỷ lệ đạt 6 nhóm K, kèm mẫu số và kỳ trước
3. 🚩 CỜ ĐỎ — từng cuộc, có trích dẫn, ⛔ không gộp thành số
4. NHÁNH ① CƠ HỘI — số dòng theo nhóm C1–C4 + danh sách
5. NHÁNH ② ĐÀO TẠO — lỗi ưu tiên tuần này, ai học, giáo án
6. ĐO LẠI KỲ TRƯỚC — kỹ năng đã dạy tuần trước: vào hay chưa
7. GIẢ ĐỊNH & [CHỜ XÁC NHẬN]

⛔ Mọi tỷ lệ phải có mẫu số. ⛔ Thiếu một trong ba dòng bắt buộc thì không gửi đi.
```

⚠️ **Mục 6 hay bị bỏ nhất và là mục duy nhất chứng minh cả quy trình này có tác dụng.** Không đo lại thì mỗi tuần dạy một thứ mới, và sau ba tháng không ai biết có gì đổi.

---

## 2 · Truy một chỉ số đang tụt

```
Tỷ lệ hẹn tháng này tụt từ [x]% xuống [y]%. Truy giúp tôi.

Đi theo thứ tự này, ⛔ đừng đoán nguyên nhân trước:
① Cơ cấu mẫu có đổi không — có nhân viên mới vào không?
② Nhóm K nào tụt cùng chiều với tỷ lệ hẹn?
③ Tụt ở toàn khối hay chỉ một nhóm dịch vụ / một chiến dịch?
④ Lọc riêng những cuộc trượt nhóm K đó, đọc trích dẫn
⑤ Sau đó mới kết luận: lỗi kỹ năng hay lỗi kịch bản

Mỗi bước in kèm mẫu số. Bước nào chưa đủ mẫu thì nói thẳng là chưa kết luận được.
```

> Chỉ số tiến trình đi trước chỉ số kết quả 1–2 tuần. Nếu K2.1 đã tụt từ hai tuần trước thì nguyên nhân nằm ở đó, không nằm ở tuần này.

---

## 3 · So hai kỳ

```
So kỳ [A] với kỳ [B].

Trước khi so, kiểm ba điều kiện:
- Cùng kiểu chọn mẫu không?
- Mỗi kỳ có đủ 30 cuộc không?
- Cơ cấu nhân sự trong mẫu có đổi không (người mới vào/ra)?

Điều kiện nào không thoả thì nói rõ, và ⛔ KHÔNG viết câu "tăng/giảm".
Có nhân viên mới thì tách riêng cũ / mới, ⛔ không gộp vào một tỷ lệ chung.
```

---

## 4 · Bóc tách theo chiến dịch

```
Bóc tách [n] cuộc theo mã chiến dịch.

Mỗi chiến dịch: số cuộc · tỷ lệ C6 sai số · tỷ lệ đạt từng nhóm K · tỷ lệ có hẹn.
Luôn kèm mẫu số. Chiến dịch dưới 30 cuộc thì ⛔ không so với chiến dịch khác.

Chỉ ra: nguồn nào cần kịch bản riêng · nguồn nào là vấn đề DATA chứ không phải sale.
```

---

## 5 · Đặc tả dashboard

```
Viết đặc tả ba màn dashboard cho khối:

① SỨC KHOẺ KHỐI   — trưởng khối: 6 chỉ số tiến trình + cờ đỏ + xu hướng 8 tuần
② THEO NHÓM        — trưởng nhóm: lát cắt dịch vụ + danh sách cuộc trượt
③ HỒ SƠ NHÂN VIÊN  — quản lý trực tiếp: 5 cuộc gần nhất · kỹ năng đang tập · kết quả đo lại

Mỗi chỉ số phải BẤM XUỐNG ĐƯỢC tới trích dẫn gốc.
⛔ KHÔNG làm màn bảng xếp hạng nhân viên.

Ghi rõ trường dữ liệu cần từ CRM và tổng đài cho từng màn.
```

⚠️ Số không trỏ về được bản ghi là số không ai dám dùng để nói chuyện với nhân viên.

---

## 6 · Khi bị yêu cầu xếp hạng

```
Trưởng khối muốn một bảng xếp hạng nhân viên theo điểm QC để xét thưởng.

Soạn giúp tôi câu trả lời:
- Nói rõ dữ liệu này dùng để DẠY, không dùng để XẾP
- Nêu hệ quả thật: xếp hạng công khai làm nhân viên chọn cuộc dễ, né cuộc khó
  → chỉ số đẹp lên, doanh số không đổi
- Đưa thứ thay thế: tỷ lệ đạt từng nhóm kỹ năng + kỹ năng đang tập của từng người,
  đủ để quản lý tự đánh giá
- Để họ quyết
```
