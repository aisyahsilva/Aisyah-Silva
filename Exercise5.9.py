usernames = ['admin', 'jaden', 'sarah', 'michael', 'elena']

# Pengecekan apakah list tidak kosong
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Halo admin, apakah Anda ingin melihat laporan status?")
        else:
            print(f"Halo {username.title()}, terima kasih sudah masuk kembali.")
else:
    print("Kita harus mencari beberapa pengguna!")

print("\n--- Menguji kondisi list kosong ---")
# Menghapus semua elemen dalam list
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Halo admin, apakah Anda ingin melihat laporan status?")
        else:
            print(f"Halo {username.title()}, terima kasih sudah masuk kembali.")
else:
    print("Kita harus mencari beberapa pengguna!")