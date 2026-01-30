nama = input("Nama Siswa: ")
nilaiUjian = int(input("Nilai Ujian: "))
kehadiran = int(input("Kehadiran: "))
statusTugas = input("Status Tugas Akhir: ")
# menentukan kelulusan
lulus = nilaiUjian >= 75 and kehadiran >= 80 and statusTugas == "selesai"
statusKelulusan = "LULUS" if lulus else "TIDAK LULUS"

# menentukann predikat
if lulus and nilaiUjian >= 90:
    predikat = "Sangat Baik"
elif lulus and nilaiUjian > 75:
    predikat = "Baik"
else:
    predikat = "Perlu Perbaikan"
# output
print(f"""
======= DATA KELULUSAN SISWA ========
      
Nama                : {nama}
Nilai Ujian         : {nilaiUjian}
Kehadiran           : {kehadiran}%
Status Tugas        : {statusTugas}
Status Kelulusan    : {statusKelulusan}
Predikat            : {predikat}

=====================================
""")
