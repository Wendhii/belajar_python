data_kelompok = [
    {"nama": "Wendy", "peran": ["Fullstack", "Project Manager"]},
    {"nama": "Ananda", "peran": ["Designer", "Presenter"]},
    {"nama": "King", "peran": ["Presenter"]},
    
]
data_kelompok.append({"nama": "Asep", "peran": ["ITSupport"]})
for anggota in data_kelompok:
    print(f"Nama: {anggota['nama']}")
    for peran_anggota in anggota['peran']:
        print(f"- {peran_anggota}")
    print("----------------")