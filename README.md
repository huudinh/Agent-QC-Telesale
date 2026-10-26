# 🎧 AGENT-QC-TELESALE — Nghe thay khối Telesale

> Version 1.0 · AI **bóc tách hội thoại telesale** → chấm theo **bộ chỉ số có trích dẫn `[mm:ss]`** → tách **hai nhánh**: ① **lọc khách còn tái khai thác được** · ② **chỉ ra lỗi và soạn giáo án đào tạo 15 phút**.
>
> ⛔ **Lọc và phân tích — KHÔNG ra quyết định.** Agent đưa bằng chứng và phương án; người thật ký. Không đề xuất kỷ luật, không xếp hạng nhân viên, không gọi khách.

Kiến trúc **BRAIN brand-neutral** ([`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md)) + **module đơn vị tách riêng** ([`knowledge/ts-G-ranh-gioi-rieng-tu.md`](knowledge/ts-G-ranh-gioi-rieng-tu.md) §6) → đổi khối chỉ cần thay module đó.

**Phục vụ:** khối Telesale — HCI Group.

---

## 📘 Hướng dẫn sử dụng

> ### → **[Mở trang hướng dẫn](https://claude.ai/artifact/1tQ9ySag7DwfpTE2L181gV)**
>
> | Mục | Có gì ở đó |
> |---|---|
> | **① Cài đặt** | Tên &amp; mô tả dán sẵn · tab Claude/ChatGPT/Gemini · 3 thẻ copy bộ não · 14 file tri thức copy được từng file · **smoke test 8 câu** |
> | **② Prompt mẫu** | 26 prompt lọc theo nhóm: ★ AUTO một câu ngắn · bóc tách · chấm · ① cơ hội · ② đào tạo · báo cáo · dòng lệnh |
> | **③ Năm điều phải biết** | **hai nhánh cần hai thứ khác nhau** · **luật trích dẫn** · **hai chỗ agent sai tự tin nhất** · **lỗi người hay lỗi kịch bản** · hai cổng chặn |
> | **④ Việc đang chặn** | 7 mục 🔴🟠🟡 — ai cấp, chặn gì |
>
> Trang sinh thẳng từ nội dung repo bằng `python tools/trang-huong-dan.py`, nên **nút Copy luôn khớp file nguồn**.

**Người mới bắt đầu từ trang đó, không phải từ đây.**

## Nguyên tắc tối thượng

> ### Một cuộc gọi xấu không phải một nhân viên xấu. Quá nửa nhóm cùng mắc một lỗi thì đó là lỗi của **kịch bản**.

Khách đang bực, gọi sai giờ, sai số, nghe mưa ồn — đủ thứ làm hỏng một cuộc gọi. Nói chắc từ mẫu nhỏ là cách nhanh nhất để cả khối thôi hợp tác với QC, và khi họ đã thôi hợp tác thì dữ liệu đầu vào cũng hỏng theo.

> **Giá trị của agent nằm ở TRÍCH DẪN, không nằm ở NHẬN XÉT.**
> Nhân viên cãi được một lời nhận xét. Không ai cãi được chính câu mình đã nói ở giây thứ 72.

---

## Hai nhánh

| | Nhánh | Đọc gì | Ra cái gì | Ai nhận |
|---|---|---|---|---|
| **①** | **TÌM CƠ HỘI** | **lời của khách** | Danh sách khách còn khai thác được + **lý do thật** + thời điểm gọi lại + góc tiếp cận | Trưởng nhóm sale · bàn giao [`Agent-CRM-Automation`](../Agent-CRM-Automation) dựng chiến dịch |
| **②** | **QC & ĐÀO TẠO** | **lời của nhân viên** | Lỗi cụ thể có trích dẫn + **giáo án 15 phút** cho đúng một kỹ năng + bài test + **mốc đo lại** | Quản lý trực tiếp |

⚠️ **Một cuộc gọi có thể vào cả hai nhánh** — và đó là trường hợp tốt nhất: cùng một bản ghi trả lời được cả hai câu hỏi.

---

## Quy trình 6 bước

```
B1 NẠP HỘI THOẠI    → chọn mẫu, kiểm điều kiện nghe được
B2 BÓC TÁCH         → voice → text, gán nhãn người nói, đóng mốc [mm:ss]
B3 ⛔ CỔNG A        → dữ liệu đủ chuẩn để chấm chưa (8 ô)
B4 CHẤM BỘ CHỈ SỐ   ★ sáu nhóm K1–K6 + cờ đỏ — bước quyết định
B5 RẼ HAI NHÁNH     → ① cơ hội · ② QC & đào tạo 15 phút
B6 ⛔ CỔNG B DUYỆT  → quản lý trực tiếp ký trước khi dùng kết quả
```

| Cổng | Khi nào | Ô trượt nhiều nhất |
|---|---|---|
| **A — Verify** · 8 ô | Trước khi chấm | **A2** (nhãn + mốc) và **A6** (cỡ mẫu). **A4** (thông báo ghi âm) trượt → ⛔ **DỪNG**, không chấm |
| **B — Quản lý duyệt** | Trước khi dùng kết quả | Câu hỏi quan trọng nhất: *"lỗi kỹ năng hay lỗi quy trình?"* |

---

## Bộ chỉ số — sáu nhóm, ba mức, không chấm điểm

Mỗi tiêu chí chấm `✓` ĐẠT · `✗` CHƯA ĐẠT · `—` KHÔNG ĐỦ CĂN CỨ.
⛔ Không chấm thang 10, không tính trung bình — điểm số đẻ ra xếp hạng.

| Nhóm | Nội dung | Ghi chú |
|---|---|---|
| **K1** MỞ ĐẦU | chào + xưng danh · xác nhận đúng người · **xin phép thời gian** · nêu lý do | K1.3 bị bỏ nhiều nhất — không xin phép thì cuộc chết ở phút thứ hai |
| **K2** KHAI THÁC | **hỏi nhu cầu TRƯỚC khi báo giá** · ≥2 câu hỏi mở · không độc thoại · nhắc lại ý khách | K2.1 trượt là lỗi đắt nhất: báo giá trước biến tư vấn thành hỏi giá |
| **K3** TƯ VẤN ĐÚNG | bám kịch bản · thông tin đúng · ⛔ không cam kết kết quả · không nói quá về bác sĩ | Nhóm tuân thủ |
| **K4** TỪ CHỐI | hỏi lý do thật · xử đúng tầng · không tranh cãi · giữ cửa mở | Chấm *có hỏi thêm một câu không*, không chấm *có thuyết phục được không* |
| **K5** CHỐT | **lời mời hẹn CỤ THỂ có ngày giờ** · mời ≥2 lần · xác nhận lại · chốt bước tiếp | K5.1 nối thẳng với doanh số |
| **K6** NGỮ ĐIỆU | tốc độ · không cắt lời · giữ thái độ · khách nói ≥30% | ⚠️ **Cần audio.** Chỉ có text → cả nhóm ghi `—` |

**⛔ Cờ đỏ — trượt cả cuộc, chuyển quản lý ngay:**
`R1` cam kết chắc chắn kết quả · `R2` sai giá/ưu đãi · `R3` gắt, mỉa, tranh cãi · `R4` lộ thông tin khách khác · `R5` bịa bằng cấp bác sĩ · `R6` gọi lại người đã vào DNC.

⛔ Agent nêu sự việc + trích dẫn. **Không đề xuất hình thức xử lý.**

---

## Cỡ mẫu — được kết luận tới đâu

| Kết luận về | Tối thiểu |
|---|---|
| Một cuộc gọi | 1 cuộc |
| **Một nhân viên** | **5 cuộc / 14 ngày** |
| Một nhóm, một dịch vụ | **30 cuộc** |
| Xu hướng giữa hai kỳ | **30 cuộc mỗi kỳ** |

---

## Bảy module tri thức

| File | Nội dung |
|---|---|
| [`ts-A-vai-tro-quy-trinh`](knowledge/ts-A-vai-tro-quy-trinh.md) | Vai trò · ★ **chế độ AUTO** · 6 bước · **cổng A 8 ô** · cổng B · cỡ mẫu · ba loại yêu cầu |
| [`ts-B-bo-chi-so-qc`](knowledge/ts-B-bo-chi-so-qc.md) | ★ **Cổng chặn** — sáu nhóm K · cờ đỏ R1–R6 · **luật trích dẫn** + chứng cứ phủ định |
| [`ts-C-nhanh-co-hoi`](knowledge/ts-C-nhanh-co-hoi.md) | Nhánh ① — sáu kết cục C1–C6 · lý do thật · thời điểm gọi lại · **DNC** |
| [`ts-D-nhanh-qc-dao-tao`](knowledge/ts-D-nhanh-qc-dao-tao.md) | Nhánh ② — một buổi một kỹ năng · giáo án 15' · đóng vòng lặp · lỗi người hay lỗi kịch bản |
| [`ts-E-ban-ghi-ngu-dieu`](knowledge/ts-E-ban-ghi-ngu-dieu.md) | Chọn mẫu · bóc tách · **giới hạn ngữ điệu** · loại cuộc khỏi mẫu · trường cần từ CRM |
| [`ts-F-dashboard-bao-cao`](knowledge/ts-F-dashboard-bao-cao.md) | **Báo cáo theo tiến trình** · ba dòng bắt buộc · bốn lát cắt · tham chiếu kỳ · dashboard |
| [`ts-G-ranh-gioi-rieng-tu`](knowledge/ts-G-ranh-gioi-rieng-tu.md) | ⛔ **Không ngoại lệ** — riêng tư · không ra quyết định · không bịa · giọng |

---

## Quick start (4 bước)

1. Tạo 1 Project / GPT / Gem mới. Tên và mô tả: [`doc/01-cai-dat.md`](doc/01-cai-dat.md) §0.
2. **Instructions:** dán khối ▼▲ trong [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) — riêng **ChatGPT** dùng [`SYSTEM-PROMPT-NGAN.md`](SYSTEM-PROMPT-NGAN.md) (7.994/8.000 ký tự).
3. **Knowledge:** upload 7 file [`knowledge/`](knowledge/) + 6 file [`prompts/`](prompts/) + [`template/mau-5-cuoc.json`](template/mau-5-cuoc.json).
4. Gõ **một câu ngắn** — chế độ AUTO sẽ dẫn tiếp.

**Câu lệnh mẫu — một dòng là đủ:**
```
chấm giúp tôi 10 cuộc của team Mũi tuần này
```
Agent đoán nhánh, tự điền cái suy ra được, rồi hỏi **3 câu**: cần nhánh nào · **có audio hay chỉ có text** · ai duyệt. Trả lời gộp `1c 2a 3a` một dòng là xong lượt.

---

## Nửa tay — `tools/qc.py`

```bash
python tools/qc.py kiem   template/mau-5-cuoc.json          # cổng A 8 ô + cỡ mẫu
python tools/qc.py cham   template/mau-5-cuoc.json          # bảng chấm K1-K6 + soát lỗi chấm
python tools/qc.py cohoi  template/mau-5-cuoc.json          # nhánh ① cơ hội + DNC
python tools/qc.py giaoan template/mau-5-cuoc.json NV-07    # nhánh ② chọn 1 lỗi + giáo án 15'
python tools/qc.py tuan   template/mau-5-cuoc.json          # báo cáo tuần theo tiến trình

python tools/gop-tham-khao.py                               # gộp tri thức cho Gemini
python tools/trang-huong-dan.py                             # sinh lại trang hướng dẫn
```

**Script chặn bốn thứ, không chỉ in:**
① cuộc chưa có thông báo ghi âm → loại khỏi mọi lệnh chấm ·
② ô `✗` không trích dẫn **và** không phạm vi đã soát → báo lỗi ·
③ mẫu chỉ có text mà chấm K6 → báo lỗi ·
④ cỡ mẫu chưa đủ → in thẳng *"chấm được từng cuộc, ⛔ chưa kết luận về người"*.

Mẫu 5 cuộc **cố ý** có một cuộc trượt cổng A ô A4 và một cờ đỏ R6 kèm DNC — để thấy cổng chặn hoạt động ngay lần chạy đầu.

---

## ⛔ Ranh giới cứng

Một bản ghi telesale thẩm mỹ chứa cùng lúc **dữ liệu cá nhân + thông tin sức khoẻ + dữ liệu lao động**.

1. ⛔ **Không đưa tên · SĐT · email · địa chỉ · tình trạng sức khoẻ khách** vào bất kỳ đầu ra nào → `KH-001` · `NV-07`.
2. ⛔ **Không commit, không upload** file audio hay bản bóc tách — `out/`, `*.mp3`, `*.wav`, `ghi-am/`, `ban-boc-tach/` đã chặn sẵn trong [`.gitignore`](.gitignore). **Không gỡ.**
3. ⛔ **Không chấm cuộc chưa có thông báo ghi âm hợp lệ.**
4. ⛔ **Không đề xuất kỷ luật, cắt thưởng, điều chuyển. Không dựng bảng xếp hạng nhân viên.**

> **Vì sao điều 4 đáng giữ ngay cả khi bất tiện:** khoảnh khắc nhân viên tin rằng ghi âm được dùng để phạt, họ sẽ gọi để **không bị phạt** chứ không gọi để bán được hàng — nói đủ câu trong checklist, né khách khó, tránh câu hỏi khó. Chỉ số tiến trình đẹp lên, doanh số đứng yên, và dữ liệu đầu vào của chính agent này hỏng từ gốc.

---

## Cấu trúc

```
Agent-QC-Telesale/
├─ SYSTEM-PROMPT.md          bộ não đầy đủ (14.060 ký tự)
├─ SYSTEM-PROMPT-NGAN.md     bản ngắn cho ChatGPT (7.994/8.000)
├─ knowledge/                7 module ts-A … ts-G
├─ prompts/                  6 prompt mẫu
├─ template/                 schema cuộc gọi + mẫu 5 cuộc chạy thử
├─ tools/                    qc.py · gop-tham-khao.py · trang-huong-dan.py
├─ goi/GOP-tri-thuc.md       bản gộp cho Gemini (trần 10 file)
├─ doc/                      01-cai-dat · 02-cau-lenh · CHANGELOG
└─ out/                      ⛔ gitignored — không bao giờ commit
```

---

**Agent chấm và trình bằng chứng. Quản lý trực tiếp duyệt. Người thật quyết định về con người.**
Ba vai, không ai làm thay ai.
"# Agent-QC-Telesale" 
