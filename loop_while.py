# saldo = 50000
# while saldo > 0:
#     ambil_uang = int(input("Berapa uang yang mau diambil?: "))
#     sisa_uang = saldo - ambil_uang
#     if ambil_uang > saldo:
#         print(f"""
# Saldo tidak cukup!
# Saldo yang kamu punya: {saldo}
#               """)
#     else:
#         saldo = saldo - ambil_uang
#         print(f"Uang yang kamu ambil = {ambil_uang}")
#         print(f"Sisa uang kamu = {sisa_uang}")
# print(f"Saldo habis! Sialakan isi ulang.")

# latihan 2
# password_benar = "python123"
# kesempatan = 3
# while kesempatan > 0:
#     user_password = input("Masukan Password: ")
#     if password_benar == user_password:
#         print("Login berhasil")
#         break
#     else:
#         kesempatan = kesempatan - 1
#         print(f"Password Salah! (kesempatan tersisa {kesempatan})")
# if kesempatan == 0:
#     print("Akun terblokir!")

# latihan 3
# warna = ["Merah", "Hijau", "Kuning"]
# for i in range(len(warna)):
#     print(f"Warna nomor {i+1} adalah {warna[i]}")

# latihan 4
# barang = ["Buku", "Pensil", "Penghapus"]
# stok = [10, 0, 5]
# for i in range(len(barang)):
#     stok[i] += int(input("tambah stok: "))
#     if stok[i] > 0:
#         print(f"{barang[i]} tersdia (sisa {stok[i]})" )
#     else:
#         print(f"{barang[i]} habis!" )

# latihan 5
# produk = ["Kopi", "Teh", "Susu"]
# harga = [5000, 3000, 7000]
# for i in range(len(produk)):
#     print(f"{i + 1}. {produk[i]}")
    
# pilihan = []
# beli = int(input("Mau beli nomor brapa? (1-3): "))
# pilihan.append(beli)
# pilihan = int(beli) - 1
# print(f"Anda memilih {produk[pilihan]} seharga {harga[pilihan]}")

# latihan 6
# nama_barang = ["Beras", "Gula", "Minyak", "Terigu", "Garam"]
# stok_barang = [50, 8, 15, 3, 20]
# total = []
# for jumalah_stok in range(len(nama_barang)):
#     if stok_barang[jumalah_stok] < 10:
#         status = "KRITIS!! (DiHARAPKAN RESTOK)"
#     else:
#         status = "Aman"
#     print(f"{jumalah_stok + 1}. {nama_barang[jumalah_stok]} (Sisa: {stok_barang[jumalah_stok]}) Status: {status}")
# total = 0
# jumlah_kritis = 0
# for i in range(len(stok_barang)):
#     total = total + stok_barang[i]
#     if stok_barang[i] < 10:
#         jumlah_kritis = jumlah_kritis + 1  
# print(f"{jumlah_kritis}") 
# print(total)

# latihan 7 
# keranjang = ["Kopi", "Susu", "Roti"]
# harga = [10000, 20000, 15000]
# total = 0
# print(f"====DAFTAR BARANG DAN HARGA====")
# for daftar_barang in range(len(keranjang)):
#     print(f"{daftar_barang + 1}. {keranjang[daftar_barang]} Harga: {harga[daftar_barang]}")
#     if harga[daftar_barang] >= 15000:
#         diskon = 2000
#     else:
#         diskon
#     harga_akhir_barang = harga
#     print(f"diskon {diskon} total bayar: {total}")

# keranjang = ["Kopi", "Susu", "Roti"]
# harga = [10000, 20000, 15000]

# total_belanja = 0 # Ini celengan besarnya

# print("==== DAFTAR BARANG DAN HARGA ====")

# for i in range(len(keranjang)):
#     harga_asli = harga[i]
    
#     # Tentukan diskon untuk BARANG INI SAJA
#     if harga_asli >= 15000:
#         potongan = 2000
#     else:
#         potongan = 0
    
#     harga_akhir_barang = harga_asli - potongan
    
#     # KUNCI UTAMA: Tambahkan ke total belanja keseluruhan
#     total_belanja = total_belanja + harga_akhir_barang
    
#     print(f"{i+1}. {keranjang[i]} | Harga: {harga_asli} | Diskon: {potongan} | Bayar: {harga_akhir_barang}")

# print("-" * 30)
# print(f"TOTAL YANG HARUS DIBAYAR: {total_belanja}")

# latihan 8
# daftar_nama = ["Ani", "Budi", "Candra"]
# total_huruf = 0
# for jumlah_huruf in daftar_nama:
#     jumlah_huruf_nama_ini = len(jumlah_huruf)
#     total_huruf = total_huruf + jumlah_huruf_nama_ini
# print(total_huruf)

# latihan 9
# pemain = ["Alpha", "Beta", "Gamma"]
# skor = [150, 70, 200]
# total_skor = 0
# skor_rata_rata = 0
# for nama in range(len(pemain)):
    
#     nama_pemain = pemain[nama]
#     skor_pemain = skor[nama]
    
#     if skor[nama] > 100:
#         status = "PRO"
#     else:
#         status = "NOOB"
        
#     total_skor += skor[nama]
#     print(f"Nama: {nama_pemain} Skor: {skor_pemain} Status: {status}")
    
# skor_rata_rata = total_skor / len(pemain)
# print(f"Total Skor: {total_skor}")
# print(f"Skor Rata-Rata: {skor_rata_rata}")

# latihan 10 while loop
# uang = 100000
# harga_barang = 15000
# jumlah_beli = 0

# while uang >= harga_barang:
#     jumlah_beli = jumlah_beli + 1
#     uang = uang - harga_barang
#     print(uang)
# print(jumlah_beli)

# latihan 11
# rak_barang = ["Roti", "Susu", "Cokelat"]
# list_harga = [5000, 10000, 15000]
# uang_user = int(input("Masukan saldo anda: "))

# while True:
#     for i in range(len(rak_barang)):
#         print(f"No {i+1}. {rak_barang[i]} Harga: {list_harga[i]}")
#     user_beli = int(input("Mau beli nomor berapa? (1-3) atau ketik 0 untuk selesai: "))
#     if user_beli == 0:
#         break
#     i = user_beli - 1
#     if uang_user >= list_harga[i]:
#         uang_user -= list_harga[i]
#         print(f"Kamu membeli {rak_barang[i]} Sisa uang: {uang_user}")
#     else:
#         print("Uang tidak cukup! Terima kasih sudah mampir")
#         break

# latihan 12
# antrean = ["Budi", "Santi", "Agus"] 
# while len(antrean) > 0:
#     print("=====DAFTAR ANTREAN=====")
#     for nama in range(len(antrean)):
#         print(f"{nama + 1} {antrean[nama]}")
#     admin = input(f"Siap melayani {antrean[0]}? (y/n): ")   
#     if admin != "y":
#         print("Menunggu admin siap...")
#     else:
#         sudah_dilayani = antrean.pop(0)
#         print(f"{sudah_dilayani} Sudah selesai dilayani.")
# print("Semua nasabah sudah dilayani. Kantor tutup!")

# latihan 13
# gudang =  []
# while True:
#     admin = input("Masukan nama barang: \n")
#     if admin == "stop":
#         print("selesai")
#         break
#     else:
#         gudang.append(admin)
#         print(f"{admin} berhasil ditabahkan")
# print("====DAFTAR BARANG====")
# for i in range(len(gudang)):
#     print(f"{i + 1}. {gudang[i]}")
# cari_barang = input("cari barang: \n")
# kondisi = "barang tidak tersedia"
# for cari in gudang:
#     if cari_barang == cari:
#         kondisi = "barang tersedia"
#         break
# print(kondisi)

# latihan 14
# menu = []
# harga = []
# while True:
#     nama_menu = input("Nama Menu: ")
#     if nama_menu == "selesai":
#         print("proses selesai.")
#         break
#     harga_satuan = int(input("Harga: "))
#     menu.append(nama_menu)
#     harga.append(harga_satuan)  
    
# print("====DAFTAR MENU====")
# for i in range(len(menu)):
#     print(f"{i + 1}. {menu[i]} Harga: {harga[i]}")

# # ... (Bagian input menu & harga lu udah TOP, nggak perlu diubah)

# # TAHAP PENJUALAN
# while True: # Gua bungkus while biar bisa beli berkali-kali
#     beli = input("\nMau beli apa? (atau ketik 'stop' untuk selesai): ")
#     if beli == "stop":
#         break

#     # 1. SIAPIN PENANDA (FLAG)
#     ketemu = False
#     index_barang = -1

#     # 2. CARI BARANGNYA
#     for i in range(len(menu)):
#         if beli == menu[i]:
#             ketemu = True
#             index_barang = i # Simpan posisinya di mana
#             break

#     # 3. CEK HASIL PENCARIAN DI LUAR LOOP
#     if ketemu:
#         jumlah = int(input(f"Mau beli berapa {menu[index_barang]}? "))
#         total_bayar = harga[index_barang] * jumlah
#         print(f"Total bayar: Rp {total_bayar}")
#     else:
#         print("Maaf, menu tersebut tidak ada di kantin.")    

# latihan ..
# keranjang_buah = []
# harga = []
# while True:
#     nama_buah = input("Nama buah (ketik y/n untuk selesai): ")
#     if nama_buah == "selesai":
#         break
#     harga_buah = int(input("Harga: "))
#     keranjang_buah.append(nama_buah)
#     harga.append(harga_buah)
# total = 0
# for b in range(len(keranjang_buah)):
#     total += harga[b]
#     print(f"Buah ke-{b + 1} adalah {keranjang_buah[b]} Harganya {harga[b]}")
# print(total)

# latihan ...
# member_list = ["budi", "santi", "agus"]
# siapa = input("Masukan nama member: ").lower()
# ketemu = False
# for member in member_list:
#     if siapa == member.lower():
#         ketemu = True
#         break
# if ketemu:
#     print("Akses Diterima! Selamat Datang.")
# else:
#     print("Akses Ditolak! Anda bukan member.")

# latihan..
# barang_tersedia = ["sabun", "indomie", "susu"]
# harga_barang = [5000, 3000, 15000]

# total_belanja = 0
# while True:
#     beli = input("Mau beli apa? (ketik 'bayar' untuk selesai): ")
#     if beli == "bayar":
#         break
#     ketemu = False
#     for barang in range(len(barang_tersedia)):
#         if beli == barang_tersedia[barang]:
#             ketemu = True
#             break
#     if ketemu:
#         jumlah_beli = int(input("Beli berapa banyak?: "))
#         total_belanja += harga_barang[barang] * jumlah_beli
#         print("Berhasil menambah keranjang.")
#     else:
#         print("Maaf, barang tersebut tidak kami jual.")
# print(f"Total yang harus dibayar adalah: Rp {total_belanja}")

# latihan ...
menu = ["beras", "telur", "minyak"]
stok = [10, 20, 5]
harga = [12000, 2000, 15000]

pendapatan_hari_ini = 0
pelanggan_baru = "" 
while True:
    if pelanggan_baru == "n":
        break
    status = False
    cari_barang = input("Nama barang: ").lower()
    for m in range(len(menu)):
        if cari_barang == menu[m]:
            status = True
            break
    if status:
        jumlah_beli = int(input("Beli berapa banyak?: "))
        sisa_stok = stok[m]
        if jumlah_beli <= stok[m]:
            sisa_stok = stok[m] - jumlah_beli
            stok[m] = sisa_stok
            pendapatan_hari_ini += harga[m] * jumlah_beli
            print(f"Berhasil! Sisa stok {menu[m]} sekarang: {stok[m]}")
        else:
            print(f"Maaf, stok tidak cukup! Stok sisa: {stok[m]}")
    else:
        print("Barang tidak tersedia.")
    pelanggan_baru = input("Ada pelanggan lain? (y/n): ")
print(f"Total pendapatan hari ini: {pendapatan_hari_ini}")