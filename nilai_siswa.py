# Encapsulation

class Mahasiswa:
    def __init__(self, nama, nilai_awal):
        self.nama = nama
        self.__nilai = nilai_awal
    def lihat_nilai(self):
        return self.__nilai
    def ubah_nilai(self, nilai_baru):
        if nilai_baru >= 0 and nilai_baru <= 100:
            self.__nilai = nilai_baru
            return self.__nilai
        else:
            print("Nilai gak valid! Harus 0 - 100.")

wendy = Mahasiswa("wendy", 70)
nilai = wendy.lihat_nilai()
print(f"nilai sebelum diubah: {nilai}")
ubahNilai = wendy.ubah_nilai(90)
print(f"nilai sesudah diubah: {ubahNilai}")
gagalUbah = wendy.ubah_nilai(120)

hacker = wendy.__nilai = 100
print(f"intip nilai yang hacker ganti: {wendy.lihat_nilai()}")