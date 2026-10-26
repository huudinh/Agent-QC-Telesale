# PROMPT — NHÁNH ① TÌM CƠ HỘI & TÁI KHAI THÁC

> Tri thức: `ts-C`.

---

## 1 · Lọc cơ hội từ một mẫu

```
Lọc cơ hội từ [n] cuộc không chốt được này.

Phân vào sáu nhóm C1–C6. Chỉ C1–C4 là cơ hội.

Mỗi dòng cơ hội phải đủ bảy thứ:
  mã KH · mã NV · ngày · nhóm C
  TÍN HIỆU   [mm:ss] nguyên văn câu khách nói
  LÝ DO THẬT (suy từ ngữ cảnh, không chép lại lời khách)
  GỌI LẠI    thời điểm đề xuất + căn cứ
  GÓC VÀO    mở đầu bằng gì, ⛔ không lặp kịch bản lần đầu
  ƯU TIÊN    cao / vừa / thấp

⛔ Không có TÍN HIỆU trích dẫn được thì KHÔNG đưa vào danh sách.
Soát DNC trước: khách nào đã yêu cầu dừng gọi thì gỡ ra ngay.
```

---

## 2 · Phân biệt lý do nói ra và lý do thật

```
Khách từ chối bằng câu "[dán nguyên văn]".

Đọc đoạn NGAY TRƯỚC câu đó và cho tôi biết:
- Khách vừa hỏi gì trước khi từ chối?
- Có hỏi trả góp, hỏi so sánh, hỏi thời gian hồi phục không?
- Lý do thật nhiều khả năng là gì — và dựa vào câu nào để nói thế?

⛔ Nếu không có câu nào đủ để suy, nói thẳng "chưa đủ căn cứ, xếp vào ưu tiên thấp".
```

> *"Để em suy nghĩ thêm"* hầu như không bao giờ là lý do thật. Gọi lại bằng đúng cái cớ khách đưa ra là cách bị từ chối lần hai nhanh hơn lần một.

---

## 3 · Soạn góc tiếp cận cho lần gọi lại

```
Khách KH-xxx thuộc nhóm [C1–C4], lý do thật là [...].

Soạn góc vào cho cuộc gọi lại:
- Câu mở đầu — bám đúng lý do thật, ⛔ KHÔNG mở đầu như lần trước
- Một câu nhắc lại điều khách đã quan tâm (lấy từ trích dẫn)
- Lời mời hẹn CỤ THỂ có ngày giờ
- Một đường lui nếu khách vẫn chưa sẵn sàng

⛔ Không hứa ưu đãi chưa có thật. Chưa biết chương trình hiện hành thì ghi [CHỜ XÁC NHẬN].
```

---

## 4 · Soát DNC

```
Soát [n] cuộc này, tìm mọi trường hợp phải đưa vào DNC:

- Khách nói đừng gọi nữa / bỏ số ra / làm phiền quá
- Khách yêu cầu xoá dữ liệu
- Khách gắt vì bị gọi nhiều lần
- Sai số nhưng người nghe yêu cầu không gọi lại

Mỗi dòng: 🚫 DNC · mã KH · [mm:ss] nguyên văn.
Rồi soạn tin báo người phụ trách CRM để gỡ trong 24h.

⛔ DNC không có ngoại lệ, kể cả khách trông rất tiềm năng.
```

---

## 5 · Bàn giao cho chiến dịch

```
Danh sách cơ hội đã duyệt. Soạn gói bàn giao cho Agent-CRM-Automation:

- Nhóm khách theo C1–C4, kèm lý do thật và góc tiếp cận
- Thời điểm gọi lại đề xuất của từng nhóm
- ⛔ KHÔNG kèm tên, SĐT — chỉ mã KH; bảng quy đổi do người phụ trách CRM giữ
- Ghi rõ danh sách DNC phải loại trừ

⛔ Agent này dừng ở đây. Dựng chuỗi tin, landing page, luồng tự động là việc của agent kia.
```

---

## 6 · Báo cáo cơ hội theo chiến dịch

```
Bóc tách [n] cuộc theo mã chiến dịch.

Với mỗi chiến dịch: số cuộc · tỷ lệ C6 (sai số) · tỷ lệ C1–C4 · tỷ lệ có hẹn.
Luôn kèm mẫu số.

⚠️ Chiến dịch nào tỷ lệ C6 cao bất thường → đó là vấn đề DATA, không phải vấn đề sale.
Chuyển người phụ trách nguồn data, ⛔ đừng đẩy sang đào tạo.
```
