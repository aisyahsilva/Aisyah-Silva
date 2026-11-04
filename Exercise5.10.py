current_users = ['admin', 'jaden', 'sarah', 'michael', 'elena']
new_users = ['SARAH', 'budi', 'jaden', 'siti', 'andi']

# Membuat list baru dengan versi huruf kecil semua dari current_users
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    # Membandingkan versi lowercase dari new_user dengan current_users_lower
    if new_user.lower() in current_users_lower:
        print(f"Maaf, username '{new_user}' sudah digunakan. Anda harus memasukkan username baru.")
    else:
        print(f"Username '{new_user}' tersedia.")