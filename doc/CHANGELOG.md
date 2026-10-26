# CHANGELOG — Agent-QC-Telesale

## v1.0 — 2026-10-23 · Bản đầu

### Bài toán

Quản lý khối Telesale mất cả buổi nghe ghi âm mà vẫn chỉ nghe được vài cuộc. Nghe xong thì nhận xét theo cảm tính của người nghe — hai trưởng nhóm nghe cùng một cuộc ra hai kết luận khác nhau, và cả hai đều có lý vì họ đang chấm hai thứ khác nhau mà cùng gọi là *"cuộc gọi tốt"*.

Báo cáo hiện có chỉ nói **kết quả** (*"240 cuộc, 36 hẹn, 15%"*). Đọc xong không ai biết làm gì tiếp — tỷ lệ tụt vì nhân viên mới, vì data xấu, vì đổi kịch bản, hay vì mùa? Cuộc họp biến thành cuộc đoán.

### Ra cái gì

**Hai nhánh từ cùng một đống ghi âm** — vì chúng đọc hai thứ khác nhau:

| | Nhánh | Đọc | Ra |
|---|---|---|---|
| ① | **Tìm cơ hội** | lời của **khách** | Danh sách khách còn khai thác được + lý do thật + thời điểm gọi lại + góc tiếp cận |
| ② | **QC & đào tạo** | lời của **nhân viên** | Lỗi có trích dẫn + giáo án 15 phút cho đúng một kỹ năng + bài test + mốc đo lại |

### Các lớp logic

| Lớp | Nội dung |
|---|---|
| **Bộ chỉ số** | Sáu nhóm `K1`–`K6`, ba mức `✓ / ✗ / —`. ⛔ Không chấm thang điểm — điểm số đẻ ra xếp hạng. Chỉ số của khối là **tỷ lệ cuộc đạt từng nhóm**. |
| **Cờ đỏ** | `R1`–`R6` — trượt cả cuộc, chuyển quản lý ngay, ⛔ agent không đề xuất cách xử lý |
| **Luật trích dẫn** | Mọi nhận định phải có `[mm:ss]` nguyên văn |
| **Sáu kết cục** | `C1`–`C6`, chỉ bốn là cơ hội. `C3` thời điểm và `C4` giá là hai nhóm bị bỏ phí nhiều nhất |
| **DNC** | Không ngoại lệ, kể cả khách trông rất tiềm năng |
| **Cỡ mẫu** | 1 cuộc / **5 cuộc một nhân viên** / 30 cuộc một nhóm / 30 mỗi kỳ để nói xu hướng |
| **Hai cổng** | A verify 8 ô trước khi chấm · B quản lý trực tiếp duyệt trước khi dùng |

### Hai giới hạn cứng được mã hoá thành luật

**① Chỉ có text thì ⛔ không chấm ngữ điệu.** Cả nhóm `K6` ghi `[KHÔNG ĐỦ CĂN CỨ]`, không ghi `✗`. Đây là chỗ một agent nghe-thay dễ mất uy tín nhất: nó đoán cảm xúc rất trôi chảy, người đọc tin, rồi một hôm nhân viên mở lại file audio và cả bản chấm đổ — kể cả những phần đúng.

**② ⛔ Lọc và phân tích, không ra quyết định.** Agent không đề xuất kỷ luật, cắt thưởng, điều chuyển, và không dựng bảng xếp hạng nhân viên. Khoảnh khắc nhân viên tin rằng ghi âm được dùng để phạt, họ sẽ gọi để **không bị phạt** chứ không gọi để bán được hàng — chỉ số tiến trình đẹp lên, doanh số đứng yên, và dữ liệu đầu vào của chính agent này hỏng từ gốc.

### Quyết định thiết kế đáng ghi lại

**Chứng cứ phủ định cho tiêu chí dạng vắng mặt.** Luật ban đầu là *"mọi ô `✗` phải có trích dẫn"*. Nhưng công cụ `qc.py cham` chạy lần đầu trên mẫu mẫu thì báo ba lỗi ở `K2.2` · `K2.4` · `K5.2` — những tiêu chí trượt vì **một việc đã không xảy ra**, nên không có câu nào để trích.

Thay vì nới luật, thêm đường thứ hai: **phạm vi đã soát**.

```
✗ K2.4 — nghe và nhắc lại ý khách
  đã soát [00:00]–[06:52] tìm lượt lời NV nhắc lại ý khách — thấy 0 lần
```

Một ô `✗` phải có **trích dẫn hoặc phạm vi đã soát** — không được trống cả hai. Cả hai đều kiểm lại được; cái thứ hai chỉ là chứng cứ ở dạng phủ định.

**Báo cáo theo tiến trình, không theo kết quả.** Chỉ số tiến trình (tỷ lệ đạt từng nhóm K) đi trước chỉ số kết quả 1–2 tuần. Tới lúc tỷ lệ hẹn tụt thì ca đã mất rồi.

**Câu hỏi "lỗi người hay lỗi kịch bản" được đưa vào công cụ.** `qc.py giaoan` tự đếm bao nhiêu nhân viên trong mẫu cùng mắc lỗi đó, và dừng lại cảnh báo khi quá nửa nhóm. Đào tạo 12 người cho một lỗi mà kịch bản gây ra là tốn ba tiếng để tuần sau mắc lại y nguyên — và lần này thì mọi người đều tin rằng đào tạo không có tác dụng.

### Bàn giao sang agent khác

Nhánh ① dừng ở **danh sách cơ hội**. Dựng chuỗi tin Zalo, landing page, luồng tự động là việc của [`Agent-CRM-Automation`](../../Agent-CRM-Automation). Gọi khách là việc của sale.

### File

```
SYSTEM-PROMPT.md           14.060 ký tự
SYSTEM-PROMPT-NGAN.md       7.994 / 8.000
knowledge/                  7 module ts-A … ts-G
prompts/                    6 prompt mẫu
template/                   schema cuộc gọi + mẫu 5 cuộc chạy thử
tools/qc.py                 5 lệnh, chặn 4 thứ
```

### Việc đang chặn khi bàn giao

| | Việc | Ai cấp |
|---|---|---|
| 🔴 | Xác nhận **thông báo ghi âm hợp lệ** | Pháp chế + CNTT |
| 🔴 | **Kịch bản hiện hành** + **bảng giá / ưu đãi** | Trưởng khối + Phòng Giá |
| 🔴 | Chốt văn bản: **dữ liệu QC dùng để dạy, không dùng để xếp hạng** | Trưởng khối + Nhân sự |
| 🟠 | Gắn **mã nhân viên** và **kết quả cuộc gọi** từ tổng đài / CRM | CNTT + CRM |
| 🟠 | Lập **danh sách DNC** và quy trình gỡ số trong 24h | CRM |
| 🟠 | Chốt **mốc gọi lại** cho bốn nhóm C1–C4 | Trưởng khối |
| 🟡 | Chốt ngưỡng **K2.3** (≤45 giây) và **K6.4** (≥30%) | Trưởng khối |

Trang hướng dẫn: <https://claude.ai/artifact/1tQ9ySag7DwfpTE2L181gV>
