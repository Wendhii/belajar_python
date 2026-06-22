# stok_kantin = {
#     "kopi": {"harga": 5000, "stok": 12},
#     "teh": {"harga": 3000, "stok": 3},
#     "roti": {"harga": 2000, "stok": 15},
#     "susu": {"harga": 7000, "stok": 2}
# }
# barang_habis = []
# for nama, stok in stok_kantin.items():
#     if stok["stok"] < 5:
#         barang_habis.append({"nama": nama,"sisa": stok["stok"]})
# for i in range(len(barang_habis)):
#     # data_barang = barang_habis[i]
#     print(f"{i + 1}. {barang_habis[i]["nama"]} (sisa: {barang_habis[i]["sisa"]})")

# latihan..
gudang = [
    {"nama": "kopi", "stok": 12, "rak": "A1", "harga": 3000},
    {"nama": "kopi jahe", "stok": 5, "rak": "A2", "harga": 4000},
    {"nama": "teh", "stok": 3, "rak": "B2", "harga": 2000},
    {"nama": "susu", "stok": 2, "rak": "A3", "harga": 7000}
]
cari = input("Masukan nama barang yang dicari: ").lower()

ketemu = False

for barang in gudang:
    if cari in barang["nama"]:
        print(f"Barang ditemukan! {barang['nama']} dengan harga {barang['harga']} ada di rak {barang['rak']} dengan sisa {barang['stok']} pcs.")
        ketemu = True
if ketemu == False:
    print("Maaf, barang tidak ada di gudang.")