# 02 — CÂU LỆNH

## ★ Chế độ AUTO — gõ một câu, agent hỏi từng lượt

Không cần khai báo gì trước. Agent **đoán** nhánh, tự điền cái suy ra được, rồi hỏi **đúng 3 câu** kèm phương án `d) Để em chọn mặc định` và một thanh tiến độ.

```
chấm giúp tôi 10 cuộc của team Mũi tuần này
lọc khách còn gọi lại được trong đống cuộc không chốt này
soạn giáo án 15 phút cho NV-07
tháng này tỷ lệ hẹn tụt, truy giúp tôi
```

**Trả lời gộp một dòng:**
```
1c 2a 3a
```

⚠️ **Câu agent phải hỏi ở lượt một:** *"em có file ghi âm, hay chỉ có bản text?"* — câu đó quyết định cả nhóm **K6 ngữ điệu** chấm được hay phải ghi `[KHÔNG ĐỦ CĂN CỨ]`. Hỏi muộn là chấm lại từ đầu.

**Ba lối tắt**

| Gõ | Agent làm |
|---|---|
| `cứ chấm hết đi` | Chấm cả 6 nhóm bằng mặc định, in đậm khối **GIẢ ĐỊNH**, nhảy tới cổng B |
| `giống tuần trước` | Nhân bản cấu hình chấm kỳ trước, chỉ hỏi phần khác |
| `chỉ cần cơ hội thôi` | Chạy nhánh ①, ⛔ vẫn chạy cổng A trước |

⛔ **Không lối tắt nào bỏ được cổng B.**

---

## Theo từng bước

| Bước | Gõ |
|---|---|
| **★ AUTO** | `chấm giúp tôi 10 cuộc của team Mũi tuần này` |
| **B1–B2 bóc tách** | `Bóc tách bản ghi này thành hội thoại chuẩn: [mm:ss] NV/KH: nguyên văn.` |
| **B3 cổng A** | `Chạy cổng A. In đủ 8 ô, ô nào trượt nói rõ mất khả năng kết luận gì.` |
| **B4 chấm** | `Chấm theo bộ chỉ số. Mỗi ô ✗ phải có trích dẫn [mm:ss] hoặc phạm vi đã soát.` |
| **① cơ hội** | `Lọc cơ hội từ các cuộc không chốt. Chỉ C1–C4. Soát DNC trước.` |
| **② đào tạo** | `Chọn MỘT kỹ năng để dạy NV-xx tuần này, rồi soạn giáo án 15 phút.` |
| **Báo cáo** | `Dựng báo cáo tuần 7 mục. Mọi tỷ lệ phải có mẫu số.` |

Prompt đầy đủ cho từng bước nằm trong [`prompts/`](../prompts/).

---

## Câu hỏi vận hành hỏi thẳng được

```
Lỗi K2.1 xuất hiện ở mấy nhân viên — đây là lỗi kỹ năng hay lỗi kịch bản?
Tuần này có cờ đỏ nào không? Liệt kê từng cuộc, đừng gộp thành số.
Kỹ năng dạy tuần trước đã vào chưa? Chấm lại 5 cuộc sau đó.
Với cỡ mẫu hiện tại, tôi được kết luận tới đâu?
Chiến dịch nào có tỷ lệ sai số (C6) cao bất thường?
```

---

## Dòng lệnh

```bash
python tools/qc.py kiem   template/mau-5-cuoc.json          # cổng A 8 ô + cỡ mẫu
python tools/qc.py cham   template/mau-5-cuoc.json          # bảng chấm + soát lỗi chấm
python tools/qc.py cohoi  template/mau-5-cuoc.json          # nhánh ① cơ hội + DNC
python tools/qc.py giaoan template/mau-5-cuoc.json NV-07    # nhánh ② giáo án 15'
python tools/qc.py tuan   template/mau-5-cuoc.json          # báo cáo tuần

python tools/gop-tham-khao.py                               # gộp tri thức
python tools/trang-huong-dan.py                             # sinh lại trang hướng dẫn
```

---

## ⛔ Agent từ chối ở đâu — và nói gì

| Tình huống | Agent nói |
|---|---|
| Xin **xếp hạng nhân viên** | *"Em đưa tỷ lệ đạt theo từng nhóm kỹ năng để anh/chị biết dạy gì. Bảng xếp hạng thì em không dựng — nó làm hỏng chính dữ liệu mình đang đo."* |
| Chưa có **thông báo ghi âm** | *"Cuộc này chưa đủ điều kiện để em chấm. Cần xác nhận của người phụ trách dữ liệu trước."* |
| Kết luận từ **1–2 cuộc** | *"Hai cuộc thì em nhận xét được từng cuộc, chưa nói được về bạn ấy. Cần thêm 3 cuộc nữa trong 14 ngày."* |
| Chấm **ngữ điệu từ text** | *"Mẫu này chỉ có chữ. Em ghi [KHÔNG ĐỦ CĂN CỨ] cho nhóm giọng — có file ghi âm thì em chấm được ngay."* |
| Đưa khách **đã từ chối** vào danh sách gọi lại | *"Khách này đã yêu cầu dừng gọi ở [mm:ss]. Em đưa vào DNC. Gọi lại là cờ đỏ R6."* |
| Ép **ra quyết định** về nhân viên | *"Em đưa bằng chứng và phương án đào tạo. Đánh giá con người là của quản lý trực tiếp — bản chấm của máy không nên là căn cứ kỷ luật."* |

⛔ **Ba điều agent không bao giờ nói:** *"dữ liệu không có"* rồi dừng · *"cái này hỏi quản lý"* rồi dừng · **một con số không có trong dữ liệu**.
