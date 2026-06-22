# class KTP:
#     def __init__(self, nik_warga, nama_warga, alamat_warga):
#         self.nik = nik_warga
#         self.nama = nama_warga
#         self.alamat = alamat_warga
#         self.status = "Belum Menikah"
        
#     def tampilkan_info(self):
#         print(f"\n=== KANTOR CAPIL ===")
#         print(f"NIK    : {self.nik}")
#         print(f"Nama   : {self.nama}")
#         print(f"Alamat : {self.alamat}")
#         print(f"Nikah  : {self.status}")
        
#     def ganti_status_nikah(self, status_baru):
#         self.status = status_baru
#         print(f"\n🔔 Status {self.nama} berhasil diubah menjadi: {status_baru}!")
        
# warga1 = KTP("123443", "Wendy", "Bandung")

# warga1.ganti_status_nikah("Sudah Menikah")

# warga1.tampilkan_info()

class AkunBank:
    def __init__(self, no_rekening, pemilik):
        self.no_rekening = no_rekening
        self.pemilik_akun = pemilik
        self.saldo = 0
        print("Akun berhasil dibuat")
    def cek_saldo(self):
        print(f"Nomor Rekening: {self.no_rekening}")
        print(f"Pemilik: {self.pemilik_akun}")
        print(f"Saldo Rekening: {self.saldo}")
    def menabung(self, jumlah):
        self.saldo = self.saldo + jumlah
        print("Saldo berhasil ditambahkan.")
    def tarik_tunai(self, jumlah):
        self.saldo = self.saldo - jumlah
        print(f"Uang yang di tarik: {jumlah}")
        print(f"Sisa saldo: {self.saldo}")
        
wendy = AkunBank("000976", "wendy")
wendy.saldo = 30000
print(wendy.__dict__)


# while True:
#     pilih = input("Pilih Menu (1.Buat Rekening Baru, 2.Cek Saldo, 3.Menabung, 4.Tarik Tunai): ")
#     if pilih == "1":
#         no_rekening = input("Masukan Nomor Rekening: ")
#         nama = input("Nama Pemilik: ")
#         akun = AkunBank(no_rekening, nama.capitalize())
#     elif pilih == "2":
#         akun.cek_saldo()
#     elif pilih == "3":
#         jumlah_uang = int(input("Masukan jumlah uang: "))
#         akun.menabung(jumlah_uang)
#     elif pilih == "4":
#         tarik_tunai = int(input("Masukan jumlah uang: "))
#         akun.tarik_tunai(tarik_tunai)
#     else:
#         break
        

# 1. CLASS INDUK (Wadah Sifat Umum Semua Hewan)
# class Hewan:
#     def __init__(self, nama_hewan):
#         self.nama = nama_hewan

#     def bersuara(self):
#         print(f"🔊 {self.nama} sedang mengeluarkan suara...")
        
#     def makan(self):
#         print(f"{self.nama} sedang makan.")


# class Kucing(Hewan): 
    
#     def __init__(self, nama_kucing):
#         super().__init__(nama_kucing)
        
#     def meong(self):
#         print(f"🐱 {self.nama} berkata: Meooonggg~")


# kucing_ku = Kucing("Oyen")
# kucing_2 = Kucing("Mujar")

# kucing_ku.bersuara()
# kucing_ku.meong()

# kucing_2.makan() 
# kucing_2.meong()