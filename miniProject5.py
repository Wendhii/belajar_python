nama = input("Masukan Nama: ")
umur = int(input("Umur: "))
nilaiUjian = int(input("Nilai Ujian: "))
kehadiran = int(input("Kehadiran: "))
statusTugas = input("Status Tugas Akhir: ")
# meenentukan kelulusan
lulus = nilaiUjian >= 75 and kehadiran >= 80 and statusTugas == "selesai"
statusKelulusan = "LULUS" if lulus else "TIDAK LULUS"
if statusTugas != "selesai":
    lulus = False
elif nilaiUjian >= 90 and kehadiran >= 75:
    lulus = True
elif nilaiUjian >= 75 and kehadiran >= 89:
    lulus = True
else:
    lulus = False
# menentukan predikat
if lulus >= 90:
    predikat = "Sangat  Baik"
elif lulus >= 80 and nilaiUjian >= 89:
    predikat = "BAIK"
elif lulus >= 75 and nilaiUjian >= 79:
    predikat = "Cukup"
else:
    predikat = "Tidak Memenuhi Syarat"

print(f"""

======= HASIL EVALUASI =======
      
Nama                : {nama}
Umur                : {umur}
Nilai               : {nilaiUjian}
Status Tugas        : {statusTugas}
Status Kelulusan    : {statusKelulusan}
Predikat            : {predikat}

==============================
""")