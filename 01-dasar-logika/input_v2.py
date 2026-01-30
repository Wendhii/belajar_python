name = input("Masukan Nama: ")
age = int(input("Umur Kamu: "))
tahunSekarang = int(input("Masukan Tahun Sekarang: "))
nextAge = age + 5
pensiun = 55 - age
tahunPensiun = tahunSekarang + pensiun
print(f""" === Output ===
      
    Halo {name}!
    Umur kamu {age}.
    5 tahun lagi kamu akan berumur {nextAge} tahun.
    Jika umur pensiun 55, berarti kamu pensiun tahun {tahunPensiun}

=== Data Berhasil Dibuat ===""")
