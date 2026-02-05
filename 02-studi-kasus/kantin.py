stok_kantin = {
    "kopi": {"harga": 5000, "stok": 12},
    "teh": {"harga": 3000, "stok": 3},
    "roti": {"harga": 2000, "stok": 15},
    "susu": {"harga": 7000, "stok": 2}
}
barang_habis = []
for nama, stok in stok_kantin.items():
    if stok["stok"] < 5:
        barang_habis.append({"nama": nama,"sisa": stok["stok"]})
for i in range(len(barang_habis)):
    # data_barang = barang_habis[i]
    print(f"{i + 1}. {barang_habis[i]["nama"]} (sisa: {barang_habis[i]["sisa"]})")