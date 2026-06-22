from abc import ABC, abstractmethod

class TiketHabisException(Exception):
    pass
class MelebihiBatasPembelianException(Exception):
    pass

class TiketKonser(ABC):
    def __init__(self, jenisTiket, hargaAsli, sisaKuota):
        self.jenisTiket = jenisTiket
        self.__hargaAsli = hargaAsli
        self._sisaKuota = sisaKuota
    def getHarga(self):
        return self.__hargaAsli
    def getKuota(self):
        return self._sisaKuota
    def setKuota(self, kuotaBaru):
        self._sisaKuota = kuotaBaru
    @abstractmethod
    def hitungTotalBayar(self, jumlah_tiket):
        pass

class TiketFestival(TiketKonser):
    def __init__(self, jenisTiket, hargaAsli, sisaKuota):
        super().__init__(jenisTiket, hargaAsli, sisaKuota)
    def hitungTotalBayar(self, jumlah_tiket):
        return self.getHarga() * jumlah_tiket
class TiketVIP(TiketKonser):
    def __init__(self, jenisTiket, hargaAsli, sisaKuota):
        super().__init__(jenisTiket, hargaAsli, sisaKuota)
    def hitungTotalBayar(self, jumlah_tiket):
        return (self.getHarga() * jumlah_tiket) + 200000
    
def beliTiket(tiketObj, namaPembeli, jumlahYangDibeli):
    if jumlahYangDibeli > 4:
        raise MelebihiBatasPembelianException(f"🚨 Transaksi Ditolak: Maksimal pembelian adalah 4 tiket per transaksi!")
    if tiketObj.getKuota() < jumlahYangDibeli:
        raise TiketHabisException(f"🚨 Transaksi Gagal: Sisa tiket {tiketObj.jenisTiket} tidak mencukupi! sisa stok")
    else:
        tiketObj.setKuota(tiketObj.getKuota() - jumlahYangDibeli)
        with open("nota.txt", "a") as file:
            file.write(f"===================================\nNama Pembeli: {namaPembeli}\nJenis Tiket : {tiketObj.jenisTiket}\nJumlah      : {jumlahYangDibeli}\nSisa Kuota  : {tiketObj.getKuota()}\ntotal bayar : {tiketObj.hitungTotalBayar(jumlahYangDibeli)}\n===================================\n")

tiketFest = TiketFestival("Festival", 500000, sisaKuota=3)
tiketVIP = TiketVIP("VIP", 1500000, sisaKuota=10)

try:
    beliTiket(tiketFest, "Toni si Calo", 5)
except MelebihiBatasPembelianException as e:
    print(e)
try:
    beliTiket(tiketFest, "wendy", 2)
except MelebihiBatasPembelianException as e:
    print(e)
try:
    beliTiket(tiketFest, "budi", 2)
except TiketHabisException as e:
    print(e)
try:
    beliTiket(tiketVIP, "Siti", 2)
except TiketHabisException as e:
    print(e)