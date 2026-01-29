# # soal 1
# nama = ["Doni", "Budi", "Cici"]
# for siswa in nama:
#     print(f"Nama siswa: {siswa}")
# # soal 2
# nilai = [70, 80, 90]
# for tambah in nilai:
#     print(tambah + 5)

# FOR + IF
# soal 1
# nilai = [60, 75, 80, 90]
# for lulus in nilai:
#     if lulus >= 75:
#         print(lulus)
# # soal 2
# nama = ["Andi", "Budi", "Cici"]
# for siswa in nama:
#     if len(siswa) >= 4:
#         print(siswa)

# soal 1
angka = [1, 2, 3, 4, 5, 6]
for genap in angka:
    if genap % 2 == 0:
        print(genap)
# soal 2
nilai = [40, 50, 75, 90]
for cekLulus in nilai:
    if cekLulus < 75:
        print(f"Nilai: {cekLulus} TIDAK LULUS")
# soal 3
nama = ["Adi", "Budi", "Rama", "Sinta"]
for siswa in nama:
    if len(siswa) < 5:
        print(siswa)
# soal 4
umur = [10, 15, 17, 18, 20]
for syaratSim in umur:
    if syaratSim >= 17:
        print("boleh buat SIM")