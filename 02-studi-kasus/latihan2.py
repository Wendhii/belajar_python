umur = int(input("Masukan Umur  Anda: "))
sim = input("Punya Sim?: ")
if umur >= 17 and sim == "punya":
    print("boleh mengemudi")
elif umur >= 17 and sim == "tidak punya":
    print("belum boleh mengemudi")
else:
    print("belum cukup umur")
