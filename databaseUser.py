class DatabaseUser:
    def __init__(self):
        self.__databaseUser = {}
    def daftarkanUser(self, username, password):
        if username in self.__databaseUser:
            print(f"🚨 Error: Username {username} sudah dipakai orang lain!")
        else:
            self.__databaseUser[username] = password
            print(f"✅ Berhasil mendaftarkan user: {username}")
            with open("database.txt", "a") as database:
                database.write(f"{username} | {password}\n")
    def loginUser(self, username, password):
        if username not in self.__databaseUser:
            print("❌ Login Gagal: Username tidak ditemukan!")
        elif username in self.__databaseUser:
            if self.__databaseUser[username] == password:
                print(f"🔓 Login Sukses! Selamat datang, {username}.")
            else:
                print("🔑 Login Gagal: Password salah!")
            
db = DatabaseUser()
db.daftarkanUser("wendy", "rahasia123")
db.daftarkanUser("wendy", "passwordbaru")
db.daftarkanUser("budi", "kopi hitam")
db.loginUser("wendy", "rahasia123")
db.loginUser("calo", "rahasia123")