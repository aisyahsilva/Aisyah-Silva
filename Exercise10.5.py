# Menentukan nama file buku tamu
file_name = 'guest_book.txt'

print("=== BUKU TAMU ===")
print("Ketik 'keluar' atau 'quit' jika sudah selesai.\n")

# Membuka file dalam mode append ('a') agar data terus bertambah ke bawah
with open(file_name, 'a') as file_object:
    while True:
        name = input("Masukkan nama tamu: ")
        
        # Kondisi untuk menghentikan perulangan
        if name.lower() in ['keluar', 'quit']:
            print("Pencatatan selesai. Buku tamu telah diperbarui.")
            break
            
        # Menulis nama ke file diikuti dengan karakter baris baru (\n)
        file_object.write(f"{name}\n")
        print(f"Halo {name}, kehadiran Anda telah dicatat.")