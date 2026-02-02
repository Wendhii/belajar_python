list_suhu = [36.5, 38.2, 37.0, 39.5, 36.0]

def cek_kesehatan (angka_suhu):
    if angka_suhu > 37.5:
        return "DEMAM"
    return "NORMAL"

def filter_pengunjung (semua_suhu):
    boleh_masuk = []
    karantina = []
    for s in semua_suhu:
        status = cek_kesehatan(s)
        if status == "DEMAM":
            karantina.append(s)
        else:
            boleh_masuk.append(s)
    return boleh_masuk, karantina
boleh_masuk, karantina = filter_pengunjung(list_suhu)
print(f"Boleh masuk: {boleh_masuk}")
print(f"Jumlah yang boleh masuk: {len(boleh_masuk)} orang")
print(f"Karantina: {karantina}")
print(f"Jumlah yang dikarantina: {len(karantina)} orang")