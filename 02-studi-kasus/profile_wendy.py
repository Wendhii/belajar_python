profile_wendy = {"nama": "Wendy", "semester": 2}
data_tambahan = {"semester": 3, "skill": ["Python", "PHP"]}
profile_wendy.update(data_tambahan)
print(profile_wendy.get("asisten", "Bukan Asisten"))
nama_user = profile_wendy.pop("nama")
print(nama_user)
print(profile_wendy)