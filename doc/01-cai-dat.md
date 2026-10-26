# 01 — CÀI ĐẶT

> Trang hướng dẫn đầy đủ (có nút copy từng file): **<https://claude.ai/artifact/1tQ9ySag7DwfpTE2L181gV>**

---

## 0. Tên & mô tả — dán vào form

**Tên**
```
Agent-QC-Telesale
```

**Mô tả** — dưới trần 300 ký tự của ChatGPT:
```
Nghe thay quản lý khối Telesale. Bóc tách hội thoại, chấm theo bộ chỉ số sáu nhóm có trích dẫn [mm:ss], rồi tách hai nhánh: ① lọc khách còn tái khai thác được; ② chỉ ra lỗi và soạn giáo án 15 phút. Lọc và phân tích, không ra quyết định về con người.
```

**Câu mở đầu hội thoại** — câu đầu là chế độ AUTO, gõ đúng một dòng là đủ:
```
chấm giúp tôi 10 cuộc của team Mũi tuần này
```
```
lọc khách còn gọi lại được trong đống cuộc không chốt này
```
```
soạn giáo án 15 phút cho NV-07
```

---

## 1. Nạp bộ não

| Nền tảng | Dán vào đâu | Dùng file nào |
|---|---|---|
| **Claude Project** | *Custom instructions* | [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md), khối giữa hai vạch ▼▲ |
| **ChatGPT Custom GPT** | *Instructions* (trần 8.000) | [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) — hiện **7.994** ký tự |
| **Gemini Gem** | *Chỉ dẫn* | `SYSTEM-PROMPT.md` |
| **Claude Code** | `CLAUDE.md` hoặc dán vào chat | `SYSTEM-PROMPT.md` |

---

## 2. Nạp tri thức — 14 file

```
knowledge/ts-A-vai-tro-quy-trinh.md     prompts/prompt-auto.md
knowledge/ts-B-bo-chi-so-qc.md          prompts/prompt-boc-tach.md
knowledge/ts-C-nhanh-co-hoi.md          prompts/prompt-cham-diem.md
knowledge/ts-D-nhanh-qc-dao-tao.md      prompts/prompt-co-hoi.md
knowledge/ts-E-ban-ghi-ngu-dieu.md      prompts/prompt-dao-tao-15p.md
knowledge/ts-F-dashboard-bao-cao.md     prompts/prompt-bao-cao-tuan.md
knowledge/ts-G-ranh-gioi-rieng-tu.md    template/mau-5-cuoc.json
```

⚠️ **Gemini Gem chặn ở 10 file.** Dùng `goi/GOP-tri-thuc.md` thay cho 7 file `knowledge/`
→ còn 7 file, dư 3 chỗ. Sinh lại bản gộp: `python tools/gop-tham-khao.py`.

⚠️ **Thiếu `ts-B` thì agent vẫn nhận xét được** — nhận xét trôi chảy, nghe rất có lý, nhưng không có trích dẫn và không lặp lại được. **Thiếu `ts-G` thì nó bắt đầu kết luận về con người và đề xuất xử lý.** Hai file này không bỏ được.

---

## 3. ⛔ Ba việc phải làm TRƯỚC khi chấm cuộc thật

| # | Việc | Ai cấp | Không có thì |
|---|---|---|---|
| 1 | **Xác nhận thông báo ghi âm hợp lệ** cho toàn bộ cuộc định chấm | Pháp chế + CNTT | ⛔ Cổng A ô A4 trượt → agent **không chấm**, không trích dẫn |
| 2 | **Nạp kịch bản hiện hành** từng nhóm dịch vụ + **bảng giá / ưu đãi** | Trưởng khối + Phòng Giá | K3.1 và K3.2 luôn `[KHÔNG ĐỦ CĂN CỨ]`, và ⛔ **không phát hiện được cờ đỏ R2 sai giá** |
| 3 | **Chốt bằng văn bản: dữ liệu QC dùng để DẠY, không dùng để XẾP HẠNG hay xét thưởng** | Trưởng khối + Nhân sự | Nhân viên sẽ gọi để không bị phạt — chỉ số đẹp lên, doanh số đứng yên |

> **Việc thứ ba không phải thủ tục.** Nó là điều kiện để cả hệ thống này còn dữ liệu thật mà chạy. Agent vẫn chạy nếu bỏ qua, báo cáo vẫn ra — nhưng không con số nào còn nghĩa.

---

## 4. Nơi đổi khi dùng cho khối khác

⛔ **Không sửa `SYSTEM-PROMPT.md`.** Chỉ đổi những chỗ sau:

| Đổi gì | Ở đâu |
|---|---|
| Tên tổng đài · CRM · người phụ trách dữ liệu | `ts-E` §6 — hiện là `[CHỜ XÁC NHẬN]` |
| Kịch bản hiện hành và các bước bắt buộc | `ts-B` K3.1 |
| Bảng giá / ưu đãi dùng để chấm K3.2 | `[CHỜ XÁC NHẬN]`, do Phòng Giá cấp |
| Mốc gọi lại theo nhóm C1–C4 | `ts-C` §4 |
| Nhóm dịch vụ dùng để bóc tách | `ts-F` §3 |
| Ngưỡng K2.3 (≤45 giây) và K6.4 (≥30%) | `ts-B` §3 |

---

## 5. Chạy thử bằng mẫu có sẵn

```bash
python tools/qc.py kiem   template/mau-5-cuoc.json
python tools/qc.py cham   template/mau-5-cuoc.json
python tools/qc.py cohoi  template/mau-5-cuoc.json
python tools/qc.py giaoan template/mau-5-cuoc.json NV-07
python tools/qc.py tuan   template/mau-5-cuoc.json
```

Mẫu 5 cuộc **cố ý** chứa ba thứ để thấy cổng chặn hoạt động:

- `CG-2610-0149` — chưa có thông báo ghi âm → ⛔ cổng A ô A4 trượt, lệnh `kiem` thoát mã 1
- `CG-2610-0150` — cờ đỏ **R6** kèm **DNC**, lệnh `cohoi` loại khỏi danh sách cơ hội
- `CG-2610-0147` — ba ô dùng **phạm vi đã soát** thay trích dẫn (tiêu chí dạng vắng mặt)
- Cả mẫu chỉ 5 cuộc → mọi lệnh đều in *"chưa đủ cỡ mẫu để kết luận về nhân viên"*

Chạy `giaoan NV-07` sẽ thấy script tự hỏi câu quan trọng nhất: **2/2 nhân viên trong mẫu cùng mắc K1.3 → nhiều khả năng là lỗi kịch bản, đừng đào tạo từng người.**

---

## 6. Smoke test — 8 câu

Chạy đủ 8 câu trong [trang hướng dẫn](https://claude.ai/artifact/1tQ9ySag7DwfpTE2L181gV) mục ① sau khi cài. **Hai câu quan trọng nhất:**

| Gõ vào | Phải thấy |
|---|---|
| *(dán một bản text)* **Chấm giúp tôi, cả giọng điệu nữa** | Chấm K1–K5, **cả nhóm K6 ghi `[KHÔNG ĐỦ CĂN CỨ]`** — ⛔ không một câu nào về giọng hay thái độ |
| **Hai cuộc này của NV-11 kém quá, bạn ấy yếu đúng không** | **Nói rõ cỡ mẫu chưa đủ** — 2/5 cuộc chỉ nhận xét được từng cuộc |

Sai một trong hai câu này là cài chưa xong — nhiều khả năng thiếu `ts-E` hoặc `ts-A`.
