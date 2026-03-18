spek_komputer = {
    "prosesor": "i3 gen 4",
    "ram": "8gb",
    "storage": 128,
    "gpu": "nvidia"
}
# ubah data dict
spek_komputer["storage"] = 258
# tambah data dict
spek_komputer["koneksi"] = "Wifi"
# hapus data dict
del spek_komputer["gpu"]
# bongkar isi data dictionary menggunakan looping
for kunci, nilai in spek_komputer.items():
    print(f"Komponen {kunci} berisi {nilai}")
