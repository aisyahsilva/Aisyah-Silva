# Menentukan nama file tujuan
file_name = 'guest.txt'

# Meminta input nama dari pengguna
guest_name = input("Masukkan nama Anda: ")

# Membuka file dalam mode write ('w') untuk menulis data
with open(file_name, 'w') as file_object:
    file_object.write(guest_name)

print(f"Terima kasih, nama '{guest_name}' telah disimpan ke dalam {file_name}.")