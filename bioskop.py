bookings = []

BARIS = ["A", "B"]
KOLOM = range(1, 11)

def buat_daftar_kursi():
    return [f"{b}{k}" for b in BARIS for k in KOLOM]

def kursi_sudah_terisi(no_kursi, judul, jam):
    for b in bookings:
        if b["no_kursi"] == no_kursi and b["judul_film"] == judul and b["jam_tayang"] == jam:
            return True
    return False

def pesan_kursi():
    kode = input("Kode Booking: ")
    nama = input("Nama Penonton: ")
    film = input("Judul Film: ")
    jam = input("Jam Tayang: ")
    kursi = input("No Kursi: ").upper()
    harga = int(input("Harga Tiket: "))

    if kursi_sudah_terisi(kursi, film, jam):
        print("❌ Kursi sudah terisi")
        return

    bookings.append({
        "kode_booking": kode,
        "nama_penonton": nama,
        "no_kursi": kursi,
        "judul_film": film,
        "jam_tayang": jam,
        "harga_tiket": harga
    })
    print("✅ Booking berhasil")

def tampilkan_booking():
    film = input("Judul Film: ")
    jam = input("Jam Tayang: ")

    for b in bookings:
        if b["judul_film"] == film and b["jam_tayang"] == jam:
            print(b)

def ubah_booking():
    kode = input("Kode Booking: ")
    for b in bookings:
        if b["kode_booking"] == kode:
            nama_baru = input("Nama baru (kosong jika tidak diubah): ")
            kursi_baru = input("Kursi baru (kosong jika tidak diubah): ").upper()

            if kursi_baru:
                if kursi_sudah_terisi(kursi_baru, b["judul_film"], b["jam_tayang"]):
                    print("❌ Kursi sudah terisi")
                    return
                b["no_kursi"] = kursi_baru

            if nama_baru:
                b["nama_penonton"] = nama_baru

            print("✅ Data diperbarui")
            return
    print("❌ Kode booking tidak ditemukan")

def hapus_booking():
    kode = input("Kode Booking: ")
    for i, b in enumerate(bookings):
        if b["kode_booking"] == kode:
            bookings.pop(i)
            print("✅ Booking dibatalkan")
            return
    print("❌ Data tidak ditemukan")

def urutkan_booking():
    pilih = input("Urutkan berdasarkan (1) Kursi (2) Nama: ")
    if pilih == "1":
        bookings.sort(key=lambda x: x["no_kursi"])
    elif pilih == "2":
        bookings.sort(key=lambda x: x["nama_penonton"])

def cari_booking():
    kode = input("Kode Booking: ")
    for b in bookings:
        if b["kode_booking"] == kode:
            print(b)
            return
    print("❌ Data tidak ditemukan")

def tampilkan_kursi():
    film = input("Judul Film: ")
    jam = input("Jam Tayang: ")

    terisi = [
        b["no_kursi"] for b in bookings
        if b["judul_film"] == film and b["jam_tayang"] == jam
    ]

    for b in BARIS:
        for k in KOLOM:
            kursi = f"{b}{k}"
            print("[X]" if kursi in terisi else "[ ]", end=" ")
        print()

def laporan_pendapatan():
    film = input("Judul Film: ")
    jam = input("Jam Tayang: ")

    total = sum(
        b["harga_tiket"] for b in bookings
        if b["judul_film"] == film and b["jam_tayang"] == jam
    )
    print("Total Pendapatan:", total)

def menu_utama():
    while True:
        print("""
1. Pesan Kursi
2. Tampilkan Booking
3. Ubah Booking
4. Batalkan Booking
5. Urutkan Booking
6. Cari Booking
7. Visual Kursi
8. Laporan Pendapatan
0. Keluar
""")
        pilih = input("Pilih menu: ")

        if pilih == "1": pesan_kursi()
        elif pilih == "2": tampilkan_booking()
        elif pilih == "3": ubah_booking()
        elif pilih == "4": hapus_booking()
        elif pilih == "5": urutkan_booking()
        elif pilih == "6": cari_booking()
        elif pilih == "7": tampilkan_kursi()
        elif pilih == "8": laporan_pendapatan()
        elif pilih == "0": break

menu_utama()