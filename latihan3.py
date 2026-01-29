nilai1 = int(input("Masukan Nilai Pertama: "))
nilai2 = int(input("Masukan Nilai Kedua: "))
tambah = nilai1 + nilai2
kurang = nilai1 - nilai2
kali = nilai1 * nilai2
bagi = nilai1 / nilai2
bagiBilanganBulat = nilai1 // nilai2
sisaBagi = nilai1 % nilai2

print(f""" ===HASIL DATA===
      
Penjumlahan     : {nilai1} + {nilai2}  = {tambah}
Pengurangan     : {nilai1} - {nilai2} = {kurang}
Perkalian       : {nilai1} * {nilai2} = {kali}
Pembagian       : {nilai1} / {nilai2} = {bagi}
Pembagian bulat : {nilai1} // {nilai2} = {bagiBilanganBulat}
Sisa Bagi       : {nilai1} % {nilai2} = {sisaBagi}
 """)