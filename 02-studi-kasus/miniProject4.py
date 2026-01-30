nama = input("Masukan Nama: ")
umur = int(input("Umur: "))
nilaiUjian = int(input("Nilai Ujian: "))
kehadiran = int(input("Kehadiran: "))
statusTugas = input("Status Tugas Akhir: ")
# menentukan kategori umur
if umur < 12:
    kategori = "Anak-Anak"
elif umur < 18:
    kategori = "Remaja"
elif umur < 60:
    kategori = "Dewasa"
else:
    kategori = "Lansia"
# menentukan grade nila
if nilaiUjian >= 85:
    grade = "A"
elif nilaiUjian >= 75:
    grade = "B"
elif nilaiUjian >= 65:
    grade = "C"
else:
    grade = "D"
# menentukan kelulusan
lulus = nilaiUjian >= 75 and kehadiran >= 80 and statusTugas == "selesai"
statusKlulusan = "LULUS" if lulus else "TIDAK LULUS"
# menentukan predikat
if lulus and grade == "A":
    predikat = "Sangat Baik"
elif lulus and grade in ("B", "C") :
    predikat = "Baik"
else:
    predikat = "Perlu Perbaikan"

print(f"""
      
======== DATA KELULUSAN USER ========

Nama                : {nama}
Umur                : {umur}
Kategori Umur       : {kategori}
Nilai & Grade       : {nilaiUjian} Grade {grade}
Kehadiran           : {kehadiran}
Status Tugas        : {statusTugas}
Status Kelulusan    : {statusKlulusan}
Predikat            : {predikat} 

=====================================
""")
