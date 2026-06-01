# Inheritence
# Esncapsulation

class Buku:
    def __init__(self, judul, harga_sewa):
        self.judul = judul
        self.__harga = harga_sewa
    
    def get_harga(self):
        return self.__harga
    
class Komik(Buku):
    def __init__(self, judul, harga_sewa, volume):
        super().__init__(judul, harga_sewa)
        self.volume = volume
    def baca_komik(self):
        print(f"Membaca komik {self.judul} Volume {self.volume}...")

class Novel(Buku):
    def __init__(self, judul, harga_sewa, penulis):
        super().__init__(judul, harga_sewa)
        self.penulis = penulis
    def baca_novel(self):
        print(f"Membaca novel karya {self.penulis} yang berjudul {self.judul}...")

def hitung_total_sewa(daftar_buku, durasi_hari):
    total = 0
    total_bayar = 0
    for i in daftar_buku:
        total += i.get_harga()
    total_bayar = total * durasi_hari 
    print(total_bayar)

komik1 = Komik("One Piece", 3000, 3)
komik2 = Komik("Black Clover", 5000, 1)
novel = Novel("Solo Leveling", 5000, "gak tau")

komik1.baca_komik()
komik2.baca_komik()
novel.baca_novel()

# tes hack
novel.__harga = 700000
print(novel.get_harga())

komikP = [komik1, komik2, novel]
hitung_total_sewa(komikP, 2)