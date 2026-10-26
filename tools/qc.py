# -*- coding: utf-8 -*-
"""qc.py — nửa tay của Agent-QC-Telesale.

    python tools/qc.py kiem   <mau.json>   # cổng A 8 ô cho từng cuộc + cỡ mẫu
    python tools/qc.py cham   <mau.json>   # bảng chấm K1-K6 có trích dẫn
    python tools/qc.py cohoi  <mau.json>   # nhánh ① danh sách cơ hội + DNC
    python tools/qc.py giaoan <mau.json> <NV-xx>   # nhánh ② chọn 1 lỗi + giáo án 15'
    python tools/qc.py tuan   <mau.json>   # báo cáo tuần theo tiến trình

Không cần thư viện ngoài. Công cụ CHẶN, không chỉ in:
  - cuộc chưa có thông báo ghi âm  -> ⛔ không chấm, không trích dẫn
  - ô 'chua_dat' không trích dẫn và không phạm vi đã soát -> ⛔ báo lỗi
  - mẫu chỉ có text mà chấm K6      -> ⛔ báo lỗi
  - cỡ mẫu chưa đủ                  -> ⛔ chặn câu kết luận về nhân viên / nhóm
"""
import json
import sys
from collections import defaultdict

# ───────────────────────────────────────────────────────── bộ chỉ số (ts-B §3)
NHOM = {
    "K1": ("MỞ ĐẦU", {
        "K1.1": "chào + xưng tên + xưng đơn vị",
        "K1.2": "xác nhận đúng người cần gặp",
        "K1.3": "xin phép thời gian",
        "K1.4": "nêu lý do gọi rõ ràng",
    }),
    "K2": ("KHAI THÁC", {
        "K2.1": "hỏi nhu cầu TRƯỚC khi báo giá",
        "K2.2": "có ≥2 câu hỏi mở",
        "K2.3": "không độc thoại",
        "K2.4": "nghe và nhắc lại ý khách",
    }),
    "K3": ("TƯ VẤN ĐÚNG", {
        "K3.1": "bám kịch bản các bước",
        "K3.2": "thông tin đúng (giá, ưu đãi, thời gian)",
        "K3.3": "không cam kết kết quả",
        "K3.4": "không nói quá về bác sĩ / chứng chỉ",
    }),
    "K4": ("XỬ LÝ TỪ CHỐI", {
        "K4.1": "hỏi lại lý do thật",
        "K4.2": "xử đúng tầng",
        "K4.3": "không tranh cãi",
        "K4.4": "giữ cửa mở",
    }),
    "K5": ("CHỐT", {
        "K5.1": "lời mời hẹn CỤ THỂ có ngày giờ",
        "K5.2": "mời ít nhất 2 lần",
        "K5.3": "xác nhận lại lịch",
        "K5.4": "chốt bước tiếp theo khi chưa hẹn được",
    }),
    "K6": ("GIỌNG & NGỮ ĐIỆU", {
        "K6.1": "tốc độ nói vừa",
        "K6.2": "không cắt lời khách",
        "K6.3": "giữ thái độ khi bị từ chối",
        "K6.4": "có khoảng lặng cho khách nói",
    }),
}

CO_DO = {
    "R1": "cam kết chắc chắn kết quả điều trị",
    "R2": "nói sai giá / sai ưu đãi",
    "R3": "gắt, mỉa, tranh cãi với khách",
    "R4": "tiết lộ thông tin khách khác",
    "R5": "bịa bằng cấp bác sĩ / giải thưởng / số ca",
    "R6": "gọi lại khách đã yêu cầu đừng gọi nữa",
}

# ts-D §1 — thứ tự ưu tiên chọn lỗi để dạy
UU_TIEN_DAY = ["K1.3", "K2.1", "K5.1", "K4.1", "K2.2", "K5.4", "K2.4", "K4.2"]

# ts-C §1 — chỉ bốn nhóm là cơ hội
KET_CUC = {
    "C1": ("quan tâm, chưa đặt lịch", True),
    "C2": ("có hẹn nhưng hoãn / không đến", True),
    "C3": ("từ chối vì THỜI ĐIỂM", True),
    "C4": ("từ chối vì GIÁ", True),
    "C5": ("không có nhu cầu / đã làm nơi khác", False),
    "C6": ("sai số · sai người · trùng data", False),
}

# ts-A §5 — cỡ mẫu
MAU_NHAN_VIEN = 5
MAU_NHOM = 30

MUC = {"dat": "✓", "chua_dat": "✗", "khong_du_can_cu": "—"}


def nap(duong_dan):
    with open(duong_dan, encoding="utf-8") as f:
        return json.load(f)


def vach(ky_tu="─", n=74):
    return ky_tu * n


# ───────────────────────────────────────────────────────── cổng A (ts-A §3)
def cong_a(cg, so_cuoc_nv):
    """Trả về list (mã, nhãn, đạt, ghi chú)."""
    ra = []
    mat = cg.get("mat_tieng_giay", 0)
    tl = cg.get("thoi_luong_giay", 0) or 1
    ty_le_mat = mat / tl
    ra.append(("A1", "bản ghi nghe được (mất ≤10%)", ty_le_mat <= 0.10,
               "mất %.0f%% thời lượng" % (ty_le_mat * 100) if ty_le_mat > 0.10 else ""))

    ht = cg.get("hoi_thoai") or []
    co_nhan = bool(ht) and all(l.get("ai") in ("NV", "KH", "?") and l.get("moc") for l in ht)
    khong_ro = sum(1 for l in ht if l.get("ai") == "?")
    ra.append(("A2", "có nhãn NV/KH + mốc [mm:ss]", co_nhan,
               "%d lượt lời chưa rõ ai nói" % khong_ro if khong_ro else
               ("chưa gán nhãn hoặc thiếu mốc" if not co_nhan else "")))

    ra.append(("A3", "có mã NV + mã KH đã ẩn danh",
               bool(cg.get("ma_nv")) and bool(cg.get("ma_kh")), ""))

    co_tb = bool(cg.get("thong_bao_ghi_am"))
    ra.append(("A4", "có thông báo ghi âm hợp lệ", co_tb,
               "⛔ DỪNG — không chấm, không trích dẫn, chuyển người phụ trách dữ liệu"
               if not co_tb else ""))

    ra.append(("A5", "biết loại cuộc gọi", bool(cg.get("loai_cuoc")), ""))

    du_mau = so_cuoc_nv >= MAU_NHAN_VIEN
    ra.append(("A6", "đủ cỡ mẫu cho kết luận về nhân viên", du_mau,
               "%s mới có %d/%d cuộc — chấm được từng cuộc, ⛔ chưa kết luận về người"
               % (cg.get("ma_nv"), so_cuoc_nv, MAU_NHAN_VIEN) if not du_mau else ""))

    co_kq = cg.get("ket_qua_crm") is not None
    ra.append(("A7", "có kết quả cuộc gọi từ CRM", co_kq,
               "⛔ không nối được hành vi với kết quả" if not co_kq else ""))

    ra.append(("A8", "biết ai duyệt ở cổng B", True, ""))
    return ra


def lenh_kiem(d):
    mau = d.get("mau") or {}
    cgs = d.get("cuoc_goi") or []
    dem_nv = defaultdict(int)
    for cg in cgs:
        dem_nv[cg.get("ma_nv")] += 1

    print()
    print("CỔNG A — %s" % mau.get("ten", "(mẫu chưa đặt tên)"))
    print(vach())
    chan = []
    for cg in cgs:
        o = cong_a(cg, dem_nv[cg.get("ma_nv")])
        dat = sum(1 for _, _, ok, _ in o if ok)
        co_a4 = all(ok for ma, _, ok, _ in o if ma == "A4")
        trang = "⛔ KHÔNG CHẤM" if not co_a4 else ("%d/8" % dat)
        print("  %s · %s · %s" % (cg["ma_cuoc"], cg.get("ma_nv"), trang))
        for ma, nhan, ok, note in o:
            if not ok:
                print("      ✗ %s %s%s" % (ma, nhan, ("  → " + note) if note else ""))
        if not co_a4:
            chan.append(cg["ma_cuoc"])
    print(vach())

    # cỡ mẫu tổng
    n = len(cgs)
    print("  CỠ MẪU — kết luận tới đâu (ts-A §5)")
    print("    từng cuộc        : ✓ được")
    for nv, c in sorted(dem_nv.items()):
        print("    %-16s : %s (%d/%d cuộc)"
              % (nv, "✓ được" if c >= MAU_NHAN_VIEN else "⛔ chưa đủ", c, MAU_NHAN_VIEN))
    print("    cả nhóm          : %s (%d/%d cuộc)"
          % ("✓ được" if n >= MAU_NHOM else "⛔ chưa đủ", n, MAU_NHOM))

    loai = mau.get("loai_bo") or []
    if loai:
        print()
        print("  LOẠI KHỎI MẪU — %d cuộc (ts-E §5, phải in trong báo cáo)" % len(loai))
        for it in loai:
            print("    · %s — %s" % (it.get("ma_cuoc"), it.get("ly_do")))

    if chan:
        print()
        print("⛔ %d cuộc KHÔNG được chấm (cổng A ô A4): %s" % (len(chan), ", ".join(chan)))
    print()
    return 1 if chan else 0


# ───────────────────────────────────────────────────────── chấm (ts-B)
def soat_loi_cham(cg):
    """Những vi phạm luật chấm — công cụ chặn, không chỉ nhắc."""
    loi = []
    cham = cg.get("cham") or {}
    chi_text = cg.get("dang_du_lieu") == "chi_text"
    for ma, o in cham.items():
        muc = o.get("muc")
        if muc == "chua_dat" and not (o.get("trich_dan") or []) and not o.get("pham_vi_soat"):
            loi.append("%s ghi CHƯA ĐẠT nhưng không có trích dẫn, cũng không có phạm vi đã soát"
                       " — ⛔ coi như chưa chấm (ts-B §5)" % ma)
        if chi_text and ma.startswith("K6") and muc in ("dat", "chua_dat"):
            loi.append("%s chấm từ bản TEXT — ⛔ nhóm K6 phải ghi KHÔNG ĐỦ CĂN CỨ (ts-E §4)" % ma)
        if cg.get("stt_do_tin_thap") and ma == "K3.2" and muc in ("dat", "chua_dat"):
            loi.append("K3.2 chấm khi STT độ tin thấp — ⛔ cần người nghe lại (ts-E §3)")
    for cd in (cg.get("co_do") or []):
        if not cd.get("loi"):
            loi.append("Cờ đỏ %s không có trích dẫn nguyên văn" % cd.get("ma"))
    return loi


def lenh_cham(d):
    cgs = [c for c in (d.get("cuoc_goi") or []) if c.get("thong_bao_ghi_am")]
    bo = [c["ma_cuoc"] for c in (d.get("cuoc_goi") or []) if not c.get("thong_bao_ghi_am")]
    print()
    print("BẢNG CHẤM — %s" % (d.get("mau", {}).get("ten", "")))
    print(vach())

    tong_loi = 0
    for cg in cgs:
        print()
        print("  %s · %s · %s · %s · %s"
              % (cg["ma_cuoc"], cg.get("ma_nv"), cg.get("ma_kh"),
                 cg.get("ngay"), cg.get("dang_du_lieu")))
        cham = cg.get("cham") or {}
        for nhom, (ten, tcs) in NHOM.items():
            dong = []
            for ma in tcs:
                o = cham.get(ma)
                dong.append("%s%s" % (ma.split(".")[1], MUC.get(o["muc"], "?") if o else "·"))
            print("     %-3s %-16s %s" % (nhom, ten, "  ".join(dong)))

        for ma in sorted(cham):
            o = cham[ma]
            if o.get("muc") != "chua_dat":
                continue
            ten = None
            for _, tcs in NHOM.values():
                if ma in tcs:
                    ten = tcs[ma]
            print("     ✗ %s — %s" % (ma, ten or ""))
            for t in (o.get("trich_dan") or []):
                print('        [%s] %s: "%s"' % (t["moc"], t["ai"], t["loi"]))
            pv = o.get("pham_vi_soat")
            if pv:
                print("        đã soát [%s]–[%s] tìm %s — thấy %s lần"
                      % (pv["tu"], pv["den"], pv["da_tim"], pv.get("so_lan_thay", 0)))
            if o.get("giai_thich"):
                print("        → %s" % o["giai_thich"])

        for cd in (cg.get("co_do") or []):
            print("     🚩 %s — %s" % (cd["ma"], CO_DO.get(cd["ma"], "")))
            print('        [%s] "%s"' % (cd["moc"], cd["loi"]))
            print("        → cả cuộc CHƯA ĐẠT · chuyển quản lý NGAY · ⛔ agent không đề xuất cách xử lý")

        loi = soat_loi_cham(cg)
        tong_loi += len(loi)
        for l in loi:
            print("     ⚠ LỖI CHẤM: %s" % l)

    print()
    print(vach())
    print("  TỶ LỆ ĐẠT TỪNG NHÓM — luôn kèm mẫu số (ts-F §2)")
    for nhom, (ten, tcs) in NHOM.items():
        dat = cham_duoc = 0
        for cg in cgs:
            for ma in tcs:
                o = (cg.get("cham") or {}).get(ma)
                if not o or o["muc"] == "khong_du_can_cu":
                    continue
                cham_duoc += 1
                if o["muc"] == "dat":
                    dat += 1
        if cham_duoc:
            print("    %-3s %-16s %3d/%-3d · %3.0f%%" % (nhom, ten, dat, cham_duoc, dat * 100.0 / cham_duoc))
        else:
            print("    %-3s %-16s   —  KHÔNG ĐỦ CĂN CỨ trên toàn mẫu" % (nhom, ten))

    if bo:
        print()
        print("⛔ %d cuộc không chấm (cổng A ô A4): %s" % (len(bo), ", ".join(bo)))
    if tong_loi:
        print()
        print("⛔ %d lỗi chấm phải sửa trước khi trình cổng B." % tong_loi)
    print()
    return 1 if tong_loi else 0


# ───────────────────────────────────────────────────────── nhánh ① (ts-C)
def lenh_cohoi(d):
    cgs = d.get("cuoc_goi") or []
    print()
    print("NHÁNH ① — CƠ HỘI & TÁI KHAI THÁC")
    print(vach())

    dnc = [c for c in cgs if c.get("dnc")]
    if dnc:
        print()
        print("  🚫 DNC — gỡ khỏi MỌI danh sách, báo CRM trong 24h (ts-C §5)")
        for c in dnc:
            print('    %s · %s   [%s] "%s"'
                  % (c["ma_cuoc"], c["ma_kh"], c["dnc"]["moc"], c["dnc"]["loi"]))
        print("    ⛔ Không ngoại lệ. Gọi lại là cờ đỏ R6.")

    print()
    dem = defaultdict(int)
    for c in cgs:
        if c.get("ket_cuc"):
            dem[c["ket_cuc"]] += 1
    print("  PHÂN NHÓM KẾT CỤC")
    for ma, (ten, la_ch) in KET_CUC.items():
        print("    %s %-36s %2d %s" % (ma, ten, dem.get(ma, 0), "✅ cơ hội" if la_ch else "⛔ không"))

    print()
    print("  DÒNG CƠ HỘI")
    n = 0
    for c in cgs:
        ch = c.get("co_hoi")
        if not ch:
            continue
        if c.get("dnc"):
            print("    ⛔ %s có cơ hội nhưng đã vào DNC — LOẠI." % c["ma_cuoc"])
            continue
        if not (ch.get("tin_hieu") or {}).get("loi"):
            print("    ⛔ %s thiếu TÍN HIỆU trích dẫn — ⛔ không phải một dòng cơ hội." % c["ma_cuoc"])
            continue
        n += 1
        print()
        print("    %s · %s · %s · nhóm %s (%s)"
              % (c["ma_kh"], c["ma_nv"], c["ngay"], c.get("ket_cuc"),
                 KET_CUC.get(c.get("ket_cuc"), ("", ""))[0]))
        print('      TÍN HIỆU   [%s] KH: "%s"' % (ch["tin_hieu"]["moc"], ch["tin_hieu"]["loi"]))
        print("      LÝ DO THẬT %s" % ch["ly_do_that"])
        print("      GỌI LẠI    %s" % ch["goi_lai"])
        print("      GÓC VÀO    %s" % ch["goc_vao"])
        print("      ƯU TIÊN    %s" % ch["uu_tien"])
        if ch.get("luu_y"):
            print("      LƯU Ý      %s" % ch["luu_y"])
    print()
    print(vach())
    print("  %d dòng cơ hội · %d DNC" % (n, len(dnc)))
    print("  → Bàn giao Agent-CRM-Automation dựng chiến dịch. ⛔ Agent này dừng ở đây.")
    print()
    return 0


# ───────────────────────────────────────────────────────── nhánh ② (ts-D)
def lenh_giaoan(d, ma_nv):
    cgs = [c for c in (d.get("cuoc_goi") or [])
           if c.get("ma_nv") == ma_nv and c.get("thong_bao_ghi_am")]
    if not cgs:
        print("⛔ Không có cuộc nào chấm được của %s." % ma_nv)
        return 1

    print()
    print("NHÁNH ② — CHỌN MỘT KỸ NĂNG ĐỂ DẠY · %s" % ma_nv)
    print(vach())

    co_do = [(c, cd) for c in cgs for cd in (c.get("co_do") or [])]
    if co_do:
        print()
        print("  🚩 CÓ CỜ ĐỎ — xử NGAY, không chờ buổi đào tạo (ts-D §1)")
        for c, cd in co_do:
            print('    %s · %s  [%s] "%s"' % (c["ma_cuoc"], cd["ma"], cd["moc"], cd["loi"]))
        print("    ⛔ Agent nêu sự việc. Quyết định xử lý là của quản lý trực tiếp.")

    # đếm lỗi
    dem = defaultdict(list)
    for c in cgs:
        for ma, o in (c.get("cham") or {}).items():
            if o.get("muc") == "chua_dat":
                dem[ma].append(c)

    n = len(cgs)
    print()
    print("  LỖI LẶP LẠI (trên %d cuộc chấm được)" % n)
    for ma in sorted(dem, key=lambda m: (-len(dem[m]), UU_TIEN_DAY.index(m) if m in UU_TIEN_DAY else 99)):
        ten = next((tcs[ma] for _, tcs in NHOM.values() if ma in tcs), "")
        print("    %-6s %d/%d  %s" % (ma, len(dem[ma]), n, ten))

    chon = None
    for ma in UU_TIEN_DAY:
        if ma in dem:
            chon = ma
            break
    if not chon and dem:
        chon = max(dem, key=lambda m: len(dem[m]))
    if not chon:
        print("\n  Không có lỗi nào — ⛔ không cần dựng buổi đào tạo tuần này.\n")
        return 0

    ten = next((tcs[chon] for _, tcs in NHOM.values() if chon in tcs), "")
    de = dem[chon][0]
    tds = (de["cham"][chon].get("trich_dan") or [])

    print()
    print(vach())
    print("  GIÁO ÁN 15 PHÚT · %s · kỹ năng %s — %s" % (ma_nv, chon, ten))
    print("  Người dạy: [trưởng nhóm]   ·   Duyệt: [chờ ký]")
    print(vach("·"))
    print("  ① NGHE LẠI (3')")
    print("     Cuộc %s" % de["ma_cuoc"])
    for t in tds:
        print('     [%s] %s: "%s"' % (t["moc"], t["ai"], t["loi"]))
    print()
    print("  ② CHỈ RA (4')")
    print("     Lỗi    : %s" % (de["cham"][chon].get("giai_thich") or ten))
    print("     Hậu quả: %d/%d cuộc tuần này mắc lỗi này" % (len(dem[chon]), n))
    kq = [c for c in dem[chon] if c.get("ket_qua_crm") == "co_hen"]
    print("              trong đó %d cuộc có lịch hẹn" % len(kq))
    print("     Mẫu đúng: [lấy từ kịch bản hiện hành, hoặc cuộc ĐẠT của đồng nghiệp cùng dịch vụ]")
    print("               ⚠ Chưa có kịch bản trong tri thức → [CHỜ XÁC NHẬN]")
    print()
    print("  ③ TẬP LẠI (5')   role-play 2 lượt, quản lý đóng vai khách")
    print("  ④ TEST (3')      3 tình huống, chấm Đạt/Chưa ngay tại chỗ")
    print()
    print("  ĐO LẠI : %d cuộc tiếp theo của %s" % (MAU_NHAN_VIEN, ma_nv))
    print("  ĐẠT KHI: ≥4/%d cuộc đạt tiêu chí %s" % (MAU_NHAN_VIEN, chon))
    print(vach("·"))

    # lỗi kỹ năng hay lỗi quy trình (ts-D §6)
    tat_ca = [c for c in (d.get("cuoc_goi") or []) if c.get("thong_bao_ghi_am")]
    nv_mac = {c["ma_nv"] for c in tat_ca
              if (c.get("cham") or {}).get(chon, {}).get("muc") == "chua_dat"}
    nv_het = {c["ma_nv"] for c in tat_ca}
    print("  KỸ NĂNG HAY QUY TRÌNH? — %d/%d nhân viên trong mẫu cùng mắc %s"
          % (len(nv_mac), len(nv_het), chon))
    if len(nv_het) and len(nv_mac) > len(nv_het) / 2:
        print("  ⚠ QUÁ NỬA NHÓM cùng mắc → nhiều khả năng là LỖI KỊCH BẢN.")
        print("  ⛔ Đừng đào tạo từng người. Soát lại bước này trong kịch bản trước (ts-D §6).")
    else:
        print("  → Ít người mắc → nhiều khả năng là lỗi kỹ năng. Đào tạo 15' như trên.")
    print()
    print("  ⛔ Những lỗi CỐ Ý để lại tuần sau: %s"
          % ", ".join(m for m in dem if m != chon) or "(không có)")
    print()
    return 0


# ───────────────────────────────────────────────────────── báo cáo tuần (ts-F)
def lenh_tuan(d):
    mau = d.get("mau") or {}
    cgs = [c for c in (d.get("cuoc_goi") or []) if c.get("thong_bao_ghi_am")]
    tat_ca = d.get("cuoc_goi") or []
    loai = mau.get("loai_bo") or []

    print()
    print("BÁO CÁO TUẦN — %s" % mau.get("ten", ""))
    print(vach("═"))
    print("① KIỂU MẪU   : %s" % mau.get("kieu_chon", "⚠ CHƯA KHAI — ⛔ không gửi báo cáo"))
    print("② CỠ MẪU     : chấm %d/%d cuộc · loại %d (%s)"
          % (len(cgs), mau.get("tong_cuoc_trong_ky", len(tat_ca)), len(loai),
             "; ".join(it.get("ly_do", "") for it in loai) or "không"))
    kt = len(tat_ca) - len(cgs)
    if kt:
        print("               ⛔ %d cuộc không chấm được vì cổng A ô A4 (thông báo ghi âm)" % kt)
    print("③ NGUỒN & KỲ : %s · %s · cập nhật %s"
          % (mau.get("nguon", "⚠ chưa khai"), mau.get("ky", "⚠ chưa khai"),
             mau.get("cap_nhat", "⚠ chưa khai")))
    print(vach("═"))

    print()
    print("CHỈ SỐ TIẾN TRÌNH")
    for nhom, (ten, tcs) in NHOM.items():
        dat = duoc = 0
        for cg in cgs:
            for ma in tcs:
                o = (cg.get("cham") or {}).get(ma)
                if not o or o["muc"] == "khong_du_can_cu":
                    continue
                duoc += 1
                if o["muc"] == "dat":
                    dat += 1
        if duoc:
            print("  %-3s %-18s %3d/%-3d · %3.0f%%" % (nhom, ten, dat, duoc, dat * 100.0 / duoc))
        else:
            print("  %-3s %-18s   — KHÔNG ĐỦ CĂN CỨ" % (nhom, ten))

    print()
    print("BA TIÊU CHÍ ĐẮT NHẤT")
    for ma in ("K1.3", "K2.1", "K5.1"):
        dat = duoc = 0
        for cg in cgs:
            o = (cg.get("cham") or {}).get(ma)
            if not o or o["muc"] == "khong_du_can_cu":
                continue
            duoc += 1
            if o["muc"] == "dat":
                dat += 1
        ten = next((tcs[ma] for _, tcs in NHOM.values() if ma in tcs), "")
        print("  %-6s %-34s %d/%d" % (ma, ten, dat, duoc))

    cd = [(c, x) for c in tat_ca for x in (c.get("co_do") or [])]
    print()
    print("🚩 CỜ ĐỎ — %d cuộc (⛔ không gộp thành một con số)" % len(cd))
    for c, x in cd:
        print('  %s · %s · %s — %s' % (c["ma_cuoc"], c["ma_nv"], x["ma"], CO_DO.get(x["ma"], "")))
        print('     [%s] "%s"' % (x["moc"], x["loi"]))

    ch = [c for c in tat_ca if c.get("co_hoi") and not c.get("dnc")]
    dn = [c for c in tat_ca if c.get("dnc")]
    print()
    print("NHÁNH ① — %d dòng cơ hội · %d DNC" % (len(ch), len(dn)))
    for c in ch:
        print("  %s · nhóm %s · ưu tiên %s · gọi lại: %s"
              % (c["ma_kh"], c.get("ket_cuc"), c["co_hoi"]["uu_tien"], c["co_hoi"]["goi_lai"]))

    print()
    print("NHÁNH ② — chạy `qc.py giaoan <mau.json> <NV-xx>` cho từng người")
    dem_nv = defaultdict(int)
    for c in cgs:
        dem_nv[c["ma_nv"]] += 1
    for nv, n in sorted(dem_nv.items()):
        print("  %-8s %d cuộc %s" % (nv, n, "" if n >= MAU_NHAN_VIEN else "⛔ chưa đủ 5 — chỉ nhận xét từng cuộc"))

    print()
    print("ĐO LẠI KỲ TRƯỚC: [chưa có dữ liệu kỳ trước]")
    print("  ⚠ Đây là mục duy nhất chứng minh cả quy trình có tác dụng — ⛔ đừng bỏ (ts-F §5).")

    gd = d.get("gia_dinh") or []
    cx = d.get("cho_xac_nhan") or []
    if gd:
        print()
        print("GIẢ ĐỊNH AGENT TỰ ĐẶT")
        for g in gd:
            print("  · %s" % g)
    if cx:
        print()
        print("[CHỜ XÁC NHẬN]")
        for it in cx:
            print("  · %s" % it.get("muc"))
            print("      ai cấp: %s · chặn: %s" % (it.get("ai_cap"), it.get("chan_gi")))
    print()
    print(vach("═"))
    print("⛔ Bản này chưa qua CỔNG B. Quản lý trực tiếp phải ký trước khi dùng.")
    print()
    return 0


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    lenh, duong_dan = sys.argv[1], sys.argv[2]
    d = nap(duong_dan)
    if lenh == "kiem":
        return lenh_kiem(d)
    if lenh == "cham":
        return lenh_cham(d)
    if lenh == "cohoi":
        return lenh_cohoi(d)
    if lenh == "giaoan":
        if len(sys.argv) < 4:
            print("⛔ Thiếu mã nhân viên: qc.py giaoan <mau.json> <NV-xx>")
            return 2
        return lenh_giaoan(d, sys.argv[3])
    if lenh == "tuan":
        return lenh_tuan(d)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
