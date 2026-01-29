nama = input("Nama Siswa: ")
nilaiUjian = int(input("Nilai Ujian: "))
kehadiran = int(input("Kehadiran Siswa: "))

if nilaiUjian >= 85:
    grade = "A"
elif nilaiUjian >= 75:
    grade = "B"
elif nilaiUjian >= 65:
    grade = "C"
else:
    grade = "D"

# logika kelulusan
lulus = nilaiUjian >= 75 and kehadiran >= 80

statusKelulusan = "LULUS" if lulus else "TIDAK LULUS"
print(f"""
===== HASIL DATA SISWA =====

Nama                : {nama}
Nilai Ujian         : {nilaiUjian}
Grade               : {grade}
Kehadiran           : {kehadiran}%
Status Kelulusan    : {statusKelulusan}

=============================
""")