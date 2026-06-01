class Kendaraan:
    def __init__(self, nama_kendaraan, tarif_perhari):
        self.nama = nama_kendaraan
        self.tarif_perhari = tarif_perhari
    
    def cek_tarif(self):
        print(f"nama kendaraan: {self.nama}")
        print(f"tarif perhari: {self.tarif_perhari}")
        
class Mobil(Kendaraan):
    def __init__(self, nama_kendaraan, tarif_perhari, pintu):
        super().__init__(nama_kendaraan, tarif_perhari)
        self.jumlah_pintu = pintu
    def buka_pintu(self):
        print(f"Mobil {self.nama} yang punya {self.jumlah_pintu} pintu sedang dibuka!")
class Motor(Kendaraan):
    def __init__(self, nama_kendaraan, tarif_perhari, kopling):
        super().__init__(nama_kendaraan, tarif_perhari)
        self.jenis_kopling = kopling
    def standing(self):
        print(f"Motor {self.nama} dengan kopling {self.jenis_kopling} sedang beraksi standing!")
        
mobil = Mobil("avanza", 3000, 4)
motor = Motor("verza", 4000, "manual")

mobil.buka_pintu()
motor.standing()