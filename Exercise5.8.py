# Membuat list username
usernames = ['admin', 'jaden', 'sarah', 'michael', 'elena']

# Perulangan untuk menyapa setiap pengguna
for username in usernames:
    if username == 'admin':
        print("Halo admin, apakah Anda ingin melihat laporan status?")
    else:
        print(f"Halo {username.title()}, terima kasih sudah masuk kembali.")