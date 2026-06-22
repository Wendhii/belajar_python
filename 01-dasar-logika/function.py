# def hitung_diskon (diskon):
#     print(f"Diskon hari ini {diskon}%")

# hitung_diskon(10)

# latihan ..
# def hitung_luas_persegi (sisi):
#     return sisi * sisi
# luas = hitung_luas_persegi(5)
# hasil = luas * 2

# print(hasil)

# latihan..
# def cek_diskon (total_belanja):
#     if total_belanja > 100000:
#         total_belanja -= 10000
#     # else:
#     #     total_belanja -= 0
#     return total_belanja

# total_belanja = 10000
# total_akhir = cek_diskon(total_belanja)
# print(total_akhir)

# latihan..
def hitung_harga (harga, jumlah):
    hasil = harga * jumlah
    return hasil
def cek_diskon (total_belanja):
    if total_belanja > 100000: 
        return total_belanja - 10000
    return total_belanja

harga_barang = int(input("Harga barang: "))
jumlah_beli = int(input("Jumlah beli: "))
total_akhir = hitung_harga(harga_barang, jumlah_beli)

print(cek_diskon(total_akhir))