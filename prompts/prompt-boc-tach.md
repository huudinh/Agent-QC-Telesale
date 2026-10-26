# PROMPT — B1–B2 NẠP & BÓC TÁCH HỘI THOẠI

> Tri thức: `ts-E` · `ts-A` §3.

---

## 1 · Nạp một mẫu để chấm

```
Nạp mẫu hội thoại để chấm.

PHẠM VI      : [team / nhóm dịch vụ / nhân viên] · [kỳ]
SỐ CUỘC      : [n]
KIỂU CHỌN MẪU: [ngẫu nhiên / lọc cuộc không chốt / theo nhân viên / theo chiến dịch]
DẠNG DỮ LIỆU : [có file ghi âm / chỉ có bản text / hỗn hợp]

Trước khi chấm:
- Chạy CỔNG A 8 ô, in rõ ô nào trượt và trượt thì mất khả năng kết luận gì.
- Nói rõ cỡ mẫu này cho phép kết luận tới đâu (từng cuộc / nhân viên / nhóm).
- Nếu chỉ có text: ghi [KHÔNG ĐỦ CĂN CỨ] cho cả nhóm K6, ⛔ đừng đoán ngữ điệu.
```

---

## 2 · Bóc tách một bản ghi

```
Bóc tách bản ghi này thành hội thoại chuẩn để chấm.

Yêu cầu:
- Mỗi lượt lời một dòng: [mm:ss] NV/KH: nguyên văn
- ⛔ KHÔNG sửa chính tả của khách, KHÔNG bỏ từ đệm, KHÔNG viết gọn lại
- Không rõ ai nói thì ghi [?], ⛔ đừng đoán
- Đánh dấu mất tiếng:  [02:10] [KHÔNG NGHE ĐƯỢC 14s]
- Đánh dấu im lặng dài: [03:40] [IM LẶNG 6s]
- Ẩn danh ngay khi bóc: tên → [tên], số → [số], nhưng GIỮ NGUYÊN cấu trúc câu

Cuối bản ghi, ghi ba dòng:
  tổng thời lượng · % thời lượng khách nói · số đoạn mất tiếng
```

> ⚠️ **Từ đệm và chỗ ngắt là dữ liệu, không phải rác.** *"Dạ… cái đó thì… chị để em hỏi lại"* khác hẳn *"Chị để em hỏi lại"*. Bóc cho sạch đẹp là làm mất đúng thứ cần chấm.

---

## 3 · Kiểm chất lượng bản ghi trước khi chấm

```
Soát 10 bản ghi này, loại ra những bản không chấm được.

Loại khi: mất > 10% thời lượng · cuộc dưới 20 giây · không nghe máy.
Giữ nhưng chấm một phần khi: mất 5–10% · khách cúp giữa chừng.

In ra: số cuộc chấm được / tổng · từng cuộc bị loại kèm LÝ DO.
⛔ Không giấu phần bị loại — nó làm tỷ lệ đạt đẹp lên mà không ai biết.
```

---

## 4 · Khi bản ghi có giọng vùng miền nặng

```
Bản ghi này giọng [vùng] khá nặng. Soát giúp tôi:

- Đánh dấu cuộc là ⚠ STT độ tin thấp
- ⛔ KHÔNG chấm K3.2 (thông tin đúng) từ bản text này
- Liệt kê những chỗ nghi sai: tên riêng · con số · tên dịch vụ
- Chỗ nào quyết định một kết luận CỜ ĐỎ thì đánh dấu "cần người nghe lại"
```

⚠️ STT sai nhiều nhất ở **tên riêng · con số · tiếng địa phương** — và cả ba đều là chỗ `K3.2` đang chấm. Một con số sai trong bản text có thể biến một cuộc gọi bình thường thành **cờ đỏ R2** oan.

---

## 5 · Xin trường dữ liệu còn thiếu

```
Để chấm đủ, tôi còn thiếu mấy trường. Soạn giúp tôi tin nhắn xin dữ liệu:

- Gửi ai: [người phụ trách CRM / tổng đài]
- Cần: mã nhân viên · kết quả cuộc gọi · lần gọi thứ mấy · nhóm dịch vụ · mã chiến dịch
- Nói rõ thiếu mỗi trường thì MẤT khả năng kết luận gì

Viết ngắn, như tin nhắn nội bộ, ⛔ không viết như email công ty.
```
