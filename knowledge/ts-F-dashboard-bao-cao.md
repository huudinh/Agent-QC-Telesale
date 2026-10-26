# DASHBOARD & BÁO CÁO THEO TIẾN TRÌNH
Version 1.0 · Cập nhật 2026-10-23

> Nguyên tắc của module này: **báo cáo kết quả nói chuyện đã rồi; báo cáo tiến trình nói chỗ còn sửa được.**

---

## 1 · Vì sao không báo cáo theo kết quả

Báo cáo quen thuộc của khối sale dừng ở kết quả:

```
Tuần này: 240 cuộc · 36 lịch hẹn · tỷ lệ 15% · tuần trước 18%
```

Đọc xong không ai biết **làm gì tiếp**. Tỷ lệ tụt 3 điểm vì nhân viên mới, vì data xấu, vì đổi kịch bản, hay vì mùa — báo cáo không trả lời, và cuộc họp biến thành cuộc đoán.

Báo cáo theo **tiến trình** trả lời được, vì nó đo **những việc xảy ra bên trong cuộc gọi**:

```
Tuần này: 240 cuộc · chấm 60
  K1.3 xin phép thời gian      48/60  80%   (tuần trước 82%)
  K2.1 hỏi trước khi báo giá   26/60  43%   (tuần trước 61%)  ⚠ tụt 18 điểm
  K5.1 lời mời hẹn cụ thể      31/60  52%   (tuần trước 55%)
  🚩 cờ đỏ                      2/60        (R2 sai giá ×2)
→ Tỷ lệ hẹn tụt đi cùng K2.1. Xem 6 cuộc K2.1 trượt của nhóm Mũi.
```

> **Chỉ số tiến trình đi trước chỉ số kết quả khoảng một đến hai tuần.** Đó là lý do phải đo nó: tới lúc tỷ lệ hẹn tụt thì ca đã mất rồi.

---

## 2 · Ba dòng bắt buộc in trên MỌI báo cáo

```
① KIỂU MẪU   : ngẫu nhiên / lọc cuộc không chốt / theo nhân viên / theo chiến dịch
② CỠ MẪU     : chấm 60/240 cuộc · loại 7 (4 mất tiếng, 3 dưới 20 giây)
③ NGUỒN & KỲ : tổng đài [tên] · CRM [tên] · 13–19/10/2026 · cập nhật 20/10 08:00
```

⛔ **Thiếu một trong ba dòng thì ⛔ không gửi báo cáo đi.** Mỗi dòng chặn một kiểu đọc sai:
- Thiếu ① → người đọc tưởng mẫu lọc là đại diện cả khối.
- Thiếu ② → `43%` không biết là 26/60 hay 3/7.
- Thiếu ③ → không ai so được với kỳ sau.

⚠️ **Mọi tỷ lệ phải in kèm mẫu số**, dạng `26/60 · 43%`. ⛔ Không in `43%` trơ trọi.

---

## 3 · Bốn lát cắt — và luật không cộng ngang

| Lát cắt | Trục | Trả lời câu gì |
|---|---|---|
| **Theo nhân viên** | NV-xx | Dạy ai, dạy cái gì |
| **Theo nhóm dịch vụ** | Mũi · Mắt · Hàm mặt… | Kịch bản dịch vụ nào đang hỏng |
| **Theo chiến dịch / nguồn** | Mã chiến dịch | Data nguồn nào gọi ra hiệu quả |
| **Theo khung giờ / ca** | Sáng · chiều · tối | Tải việc và chất lượng gọi theo ca |

⛔ **Không cộng ngang bốn lát cắt.** Cùng một cuộc gọi xuất hiện ở cả bốn bảng. Cộng tổng bốn bảng ra số lớn hơn số cuộc thật — đây là lỗi đọc báo cáo hay gặp nhất.

⚠️ So sánh giữa hai nhóm dịch vụ chỉ có nghĩa khi **cùng kiểu mẫu và cùng cỡ mẫu tối thiểu 30**. Nhóm Mũi 45 cuộc so với nhóm Mắt 8 cuộc là so hai thứ khác nhau.

---

## 4 · Tham chiếu kỳ — so cái gì với cái gì

| So | Điều kiện | Bẫy |
|---|---|---|
| **Tuần này vs tuần trước** | Cùng kiểu mẫu | Tuần có lễ thì cả hành vi khách lẫn tải việc đều khác |
| **Tháng này vs tháng trước** | Cùng kiểu mẫu, ≥30 cuộc mỗi kỳ | — |
| **Trước vs sau đào tạo** | Cùng nhân viên, **cùng nhóm dịch vụ**, cùng tiêu chí | ⛔ Đổi dịch vụ giữa hai kỳ là so hỏng |
| **Nhân viên cũ vs mới** | Tách riêng, ⛔ không gộp vào một tỷ lệ chung | Nhân viên mới kéo tỷ lệ chung xuống, che mất vấn đề thật của nhóm cũ |

⚠️ **Tách cũ/mới là lát cắt hay bị bỏ nhất và gây hiểu sai nhiều nhất.** Khối vừa tuyển 5 người thì mọi chỉ số tiến trình đều tụt — không phải vì nhóm cũ đi xuống, mà vì mẫu đổi. ⛔ Không kết luận xu hướng khi cơ cấu nhân sự trong mẫu đã đổi, trừ khi đã tách ra.

---

## 5 · Khung một báo cáo tuần

```
1. BA DÒNG BẮT BUỘC                           (§2)
2. CHỈ SỐ TIẾN TRÌNH — 6 nhóm K, kèm mẫu số và kỳ trước
3. 🚩 CỜ ĐỎ         — liệt kê từng cuộc, có trích dẫn, ⛔ không gộp thành số
4. NHÁNH ① CƠ HỘI   — số dòng cơ hội theo nhóm C1–C4 + danh sách
5. NHÁNH ② ĐÀO TẠO  — lỗi ưu tiên tuần này + ai học + giáo án
6. ĐO LẠI KỲ TRƯỚC  — kỹ năng đã dạy tuần trước: vào hay chưa
7. GIẢ ĐỊNH & [CHỜ XÁC NHẬN]
```

⚠️ **Mục 6 là mục hay bị bỏ nhất và là mục duy nhất chứng minh cả quy trình này có tác dụng.** Không đo lại thì mỗi tuần lại dạy một thứ mới, và sau ba tháng không ai biết có gì đổi.

---

## 6 · Dashboard — ba màn, không hơn

| Màn | Cho ai | Có gì |
|---|---|---|
| **Sức khoẻ khối** | Trưởng khối | 6 chỉ số tiến trình + cờ đỏ + xu hướng 8 tuần |
| **Theo nhóm** | Trưởng nhóm | Lát cắt dịch vụ + danh sách cuộc trượt, bấm vào xem trích dẫn |
| **Hồ sơ nhân viên** | Quản lý trực tiếp | 5 cuộc gần nhất · kỹ năng đang tập · kết quả đo lại |

⛔ **Không làm màn "bảng xếp hạng nhân viên".** Bị yêu cầu thì trả lời bằng `ts-G` §2: dữ liệu này dùng để **dạy**, không dùng để **xếp**. Một bảng xếp hạng công khai sẽ làm nhân viên chọn cuộc dễ để gọi và né cuộc khó — chỉ số đẹp lên, doanh số thì không.

⚠️ Mỗi con số trên dashboard phải **bấm xuống được tới trích dẫn gốc**. Số không trỏ về được bản ghi là số không ai dám dùng để nói chuyện với nhân viên.

---

## 7 · Bóc tách chiến dịch — nối QC với marketing

| Câu hỏi | Cần gì |
|---|---|
| Data nguồn nào gọi ra có tỷ lệ hẹn cao hơn? | Mã chiến dịch trong CRM |
| Nguồn nào khách hay nói *"tôi không đăng ký gì cả"*? | Đếm cuộc nhóm **C6 sai số** theo chiến dịch |
| Nguồn nào cần kịch bản riêng? | Lát cắt K-nhóm theo chiến dịch |

⚠️ **Tỷ lệ C6 cao theo một chiến dịch là vấn đề của data, không phải của sale.** Đẩy nó sang đào tạo là chữa sai bệnh. Chuyển cho người phụ trách nguồn data và `Agent-CRM-Automation`.
