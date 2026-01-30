nilai = int(input("Masukan Nilai: "))
if nilai >= 90:
    print(f"""
=== HASIL ===

Nilai kamu: {nilai}
Grade: A
Status: LULUS

""")
elif nilai >= 80:
    print(f"""
=== HASIL ===

Nilai kamu: {nilai}
Grade: B
Status: LULUS

""") 
elif nilai >= 70:
    print(f"""
=== HASIL ===

Nilai kamu: {nilai}
Grade: C
Status: LULUS

""")
elif nilai >= 60:
    print(f"""
=== HASIL ===

Nilai kamu: {nilai}
Grade: D
Status: LULUS

""")
else:
    print(f"""
=== HASIL ===

Nilai kamu: {nilai}
Grade: E
Status: TIDAK LULUS

""")
