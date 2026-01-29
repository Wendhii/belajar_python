nama_siswa = ["Andi", "Budi", "Cici", "Doni"]
nilai_siswa = [60, 75, 85, 90]
for daftarSiswa, daftarNilai in zip(nama_siswa, nilai_siswa):
    # menentukan kelulusan
    if daftarNilai >= 75:
        status = "LULUS"
    else:
        status = "TIDAK LULUS"
    # menentukan predikat
    if daftarNilai >= 90:
        predikat = "Sangat Baik"
    elif daftarNilai >= 80:
        predikat = "Baik"
    elif daftarNilai >= 75:
        predikat = "Cukup"
    else:
        predikat = "Tidak Lulus"
    print(f"""
========== OUTOUT =========

Nama        : {daftarSiswa}
Nilai       : {daftarNilai}
Status      : {status}
Predikat    : {predikat}

----------------------------
""")