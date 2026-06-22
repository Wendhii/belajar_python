nama = input("Masukan Nama: ")
umur = int(input("Masukan Umur: "))
nilaiUjian = int(input("Masukan Nilai Ujian: "))
statusSim = input("Punya Sim?: ")

# menentukan umur
if umur < 12:
    kategori = "Anak_anak"
elif umur < 18:
    kategori = "Remaja"
elif umur < 60:
    kategori = "Dewasa"
else:
    kategori = "Lansia"
# Menentukan Nilai
if nilaiUjian >= 90:
    grade = "A"
elif nilaiUjian >= 80:
    grade = "B"
elif nilaiUjian >= 70:
    grade = "C"
elif nilaiUjian >= 60:
    grade = "D"
else:
    grade = "E"
# Status izin mengemudi
if umur >= 17 and statusSim == "ya":
    statusMengemudi = "Boleh Mengemudi"
else:
    statusMengemudi = "belum Boleh Mengemudi"

print(f"""
===== HASIL DATA USER =====
      
nama: {nama}
umur: {umur}
kategori: {kategori}

Nilai Ujian : {nilaiUjian}
grade : {grade}

Status SIM : {statusSim}
Izin Mengemudi : {statusMengemudi}

==========================
""")
