import json

filename = 'user_profile.json'

try:
    with open(filename) as f:
        contents = f.read()
        profile = json.loads(contents)
except FileNotFoundError:
    # Mengumpulkan informasi tambahan jika file belum ada
    profile = {
        'username': input("Masukkan username Anda: "),
        'age': input("Masukkan usia Anda: "),
        'city': input("Masukkan kota asal Anda: "),
    }
    
    # Menyimpan dictionary ke file menggunakan json.dumps()
    with open(filename, 'w') as f:
        f.write(json.dumps(profile))
    print("Profil Anda telah disimpan!")
else:
    print("\n--- Ringkasan Profil Pengguna ---")
    print(f"Username : {profile['username']}")
    print(f"Usia     : {profile['age']}")
    print(f"Kota     : {profile['city']}")