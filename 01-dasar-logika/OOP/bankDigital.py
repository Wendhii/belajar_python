# Inheritence
# Encapsulation
# Pholymorphism
# Abstraction


from abc import ABC, abstractmethod;
class AkunBank(ABC):
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.__saldo = saldo_awal
    def get_saldo(self):
        return self.__saldo
    
    @abstractmethod
    def hitung_bunga(self):
        pass

class TabunganBiasa(AkunBank):
    def __init__(self, pemilik, saldo_awal):
        super().__init__(pemilik, saldo_awal)
    def hitung_bunga(self):
        return self.get_saldo() * 0.02
    
class AkunInvestasi(AkunBank):
    def __init__(self, pemilik, saldo_awal):
        super().__init__(pemilik, saldo_awal)
    def hitung_bunga(self):
        return self.get_saldo() * 0.10
    
akun_biasa = TabunganBiasa("Wendy", 1000000)
akun_investasi = AkunInvestasi("Wendy Pro", 5000000)
daftar_akun = [akun_biasa, akun_investasi]
for i in daftar_akun:
    print(int(i.hitung_bunga()))