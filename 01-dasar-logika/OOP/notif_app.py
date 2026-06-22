class EmailNotif:
    def kirim(self, pesan):
        self.isiPesan = pesan
        print(f"📧 Mengirim Email berisi pesan: {self.isiPesan}")

class SMSNotif:
    def kirim(self, pesan):
        self.isiPesan = pesan
        print(f"💬 Mengirim SMS berisi pesan: {self.isiPesan}")
class WaNotif:
    def kirim(self, pesan):
        self.isipPesan = pesan
        print(f"🟢 Mengirim WhatsApp berisi pesan: {self.isipPesan}")

isi_pesan = "Diskon Gede-Gedean 50% Malam Ini!"        
email = EmailNotif()
sms = SMSNotif()
wa = WaNotif()

daftar_pesan = [email, sms, wa]
for i in daftar_pesan:
    i.kirim(isi_pesan)