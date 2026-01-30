age = int(input("Masukan Umur Kamu: "))
if age < 12:
    print(f"""
        ==HASIL===
          
        Umur kamu {age}
        Kamu masih anak-anak

        Data berhasil diproses

        """)
elif age < 18:
    print(f"""
          
        ==HASIL===
          
        Umur kamu {age}
        Kamu remaja

        Data berhasil diproses

        """)
elif age < 60:
    print(f"""
          
        ==HASIL===
          
        Umur kamu {age}
        Kamu dewasa

        Data berhasil diproses

        """)
else:
    print(f"""
          
        ==HASIL===
          
        Umur kamu {age}
        Kamu lanjut usia

        Data berhasil diproses

        """)
