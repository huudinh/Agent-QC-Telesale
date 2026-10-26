# BẢN GHI · BÓC TÁCH · GIỚI HẠN NGỮ ĐIỆU
Version 1.0 · Cập nhật 2026-10-23

> Module này nói **dữ liệu đầu vào tới đâu thì agent được kết luận tới đó**. Đây là chỗ agent dễ nói chắc về thứ nó không biết nhất.

---

## 1 · B1 — Chọn mẫu

| Kiểu chọn | Dùng khi | Bẫy |
|---|---|---|
| **Ngẫu nhiên** trong kỳ | Chấm định kỳ, đo sức khoẻ cả khối | — |
| **Theo kết quả** (lọc cuộc không chốt) | Tìm cơ hội, tìm lỗi | ⚠️ Chỉ nghe cuộc hỏng thì mọi chỉ số đều xấu — ⛔ không suy ra tỷ lệ của cả khối |
| **Theo nhân viên** | Đo lại sau đào tạo | Phải **cùng nhóm dịch vụ** với lần trước, nếu không thì không so được |
| **Theo chiến dịch** | Bóc tách hiệu quả nguồn | Cần mã chiến dịch trong CRM |

⚠️ **Phải khai kiểu chọn mẫu lên đầu báo cáo.** Cùng một con số `40% đạt` đọc hoàn toàn khác nhau giữa *mẫu ngẫu nhiên* và *mẫu lọc cuộc không chốt*. Không khai là đánh lừa người đọc, kể cả khi không cố ý.

---

## 2 · B2 — Bóc tách: bản ghi phải có gì

```
[00:00] NV : Alo em chào chị, em [tên] gọi từ [đơn vị] ạ
[00:06] KH : Ừ em
[00:08] NV : Dạ chị cho em hỏi có phải chị [tên] không ạ?
...
```

Bắt buộc:
- **Nhãn người nói** — `NV` / `KH`. Không rõ ai nói thì `?` (⛔ không đoán).
- **Mốc `[mm:ss]`** mỗi lượt lời.
- **Nguyên văn** — ⛔ không sửa chính tả của khách, không bỏ từ đệm, không viết gọn lại.
- Đánh dấu **mất tiếng**: `[02:10] [KHÔNG NGHE ĐƯỢC 14s]`
- Đánh dấu **im lặng dài**: `[03:40] [IM LẶNG 6s]` — tín hiệu thật, đừng bỏ.

⚠️ **Từ đệm và chỗ ngắt là dữ liệu, không phải rác.** *"Dạ… cái đó thì… chị để em hỏi lại"* khác hẳn *"Chị để em hỏi lại"*. Bóc tách cho sạch đẹp là làm mất đúng thứ cần chấm.

---

## 3 · Công cụ chuyển voice → text

| Bước | Công cụ | Ghi chú |
|---|---|---|
| Chọn mẫu audio | Nguồn ghi âm của tổng đài | Giữ nguyên file gốc, ⛔ không cắt |
| Voice → text | Google AI Studio hoặc công cụ STT tương đương | Chọn model có **tách người nói** |
| Gán nhãn + mốc | Công cụ hoặc người soát | **Luôn cần người soát lại** nhãn NV/KH |

⚠️ **STT sai nhiều nhất ở ba chỗ:** tên riêng · con số · tiếng địa phương. Cả ba đều là chỗ `ts-B` K3.2 *(thông tin đúng)* đang chấm. Thấy một con số trong bản text mà nó quyết định một kết luận **cờ đỏ R2** → ⛔ phải nghe lại đoạn đó bằng tai người trước khi ghi.

### Tiếng địa phương
Bản ghi có giọng vùng miền nặng → tỷ lệ sai của STT tăng mạnh. Trong trường hợp đó:
- Đánh dấu cuộc gọi là `⚠ STT độ tin thấp`
- ⛔ Không chấm K3.2 từ text thuần
- Ưu tiên cho người soát nghe lại

---

## 4 · ⛔ GIỚI HẠN CỨNG — chỉ có text thì không chấm ngữ điệu

| Chỉ có TEXT thì đọc được | Chỉ có TEXT thì ⛔ KHÔNG đọc được |
|---|---|
| Có hỏi nhu cầu trước khi báo giá không | Giọng có gắt không |
| Có lời mời hẹn cụ thể không | Nói nhanh hay chậm |
| Có cắt lời không *(thấy qua lượt lời chồng nhau)* | Thái độ khi bị từ chối |
| Tỷ lệ thời lượng nói *(nếu có mốc đầy đủ)* | Khách có thật sự vui vẻ không |

**Chỉ có text → cả nhóm K6 chấm `—`.** Viết nguyên văn:

```
K6 · GIỌNG & NGỮ ĐIỆU — [KHÔNG ĐỦ CĂN CỨ]
     Mẫu này chỉ có bản text, không có audio. Cần file ghi âm để chấm nhóm này.
```

⛔ **Ba câu agent không bao giờ được viết khi chỉ có text:**
- *"Nhân viên tỏ ra thiếu kiên nhẫn"*
- *"Khách có vẻ hài lòng"*
- *"Giọng điệu chưa thân thiện"*

> Đây là chỗ một agent nghe-thay dễ mất uy tín nhất: nó đoán cảm xúc rất trôi chảy, người đọc tin, rồi một hôm nhân viên mở lại file audio và cả bản chấm đổ. Thà ghi `—` còn hơn đoán đúng chín lần và sai một lần.

---

## 5 · Chất lượng bản ghi — khi nào thì bỏ cuộc gọi khỏi mẫu

| Tình trạng | Xử |
|---|---|
| Mất > 10% thời lượng | ⛔ Loại khỏi mẫu, ghi lý do |
| Mất đoạn 5–10% | Giữ, chấm phần nghe được, các tiêu chí rơi vào đoạn mất chấm `—` |
| Cuộc gọi < 20 giây | ⛔ Loại — khách cúp ngay, không chấm được kỹ năng |
| Khách cúp giữa chừng | Giữ, chấm K1–K2, nhóm sau chấm `—` |
| Không nghe máy / máy bận | ⛔ Không phải hội thoại — đếm riêng, không vào mẫu chấm |

⚠️ **Số cuộc bị loại phải in trong báo cáo.** `Chấm 10/14 cuộc, loại 4 (2 mất tiếng, 2 dưới 20 giây)`. Giấu phần bị loại là cách làm cho tỷ lệ đạt đẹp lên mà không ai biết.

---

## 6 · Trường dữ liệu cần lấy từ CRM

| Trường | Dùng để | Thiếu thì |
|---|---|---|
| Mã nhân viên | Gộp theo người, đo lại sau đào tạo | ⛔ Cổng A ô A3 trượt |
| Kết quả cuộc gọi | Nối hành vi với kết quả | ⛔ Cổng A ô A7 trượt |
| Lần gọi thứ mấy | Chấm đúng kỳ vọng — lần 1 khác lần 4 | Chấm được, nhưng ghi rõ là không biết |
| Nhóm dịch vụ | Bóc tách theo dịch vụ | Không bóc tách được |
| Mã chiến dịch | Bóc tách theo nguồn | Không bóc tách được |
| Khung giờ gọi | Tìm mẫu theo ca | — |

⚠️ **Kết quả cuộc gọi phải lấy từ CRM, không suy từ bản ghi.** Khách nói *"ừ để chị qua"* không có nghĩa là có lịch hẹn. Chỉ CRM mới biết cuối cùng có hẹn hay không.
