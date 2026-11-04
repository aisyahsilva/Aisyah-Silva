
# Daftar lengkap dari latihan 3-6
guest_list = [
    "Park Seo-jun", "Kim Ryul", "Louis Elliot Jiho Jourdain Lim", 
    "IU", "Han Sohee", "Kwon Ohyul", "Son Heung-min"
]

print("[Info] Maaf, meja besar baru tidak tiba tepat waktu. Kami hanya bisa mengundang dua orang.\n")

# Menggunakan pop() untuk mengeluarkan tamu satu per satu
dihapus_1 = guest_list.pop()
print(f"Maaf {dihapus_1}, kami tidak bisa mengundang Anda.")

dihapus_2 = guest_list.pop()
print(f"Maaf {dihapus_2}, kami tidak bisa mengundang Anda.")

dihapus_3 = guest_list.pop()
print(f"Maaf {dihapus_3}, kami tidak bisa mengundang Anda.")

dihapus_4 = guest_list.pop()
print(f"Maaf {dihapus_4}, kami tidak bisa mengundang Anda.")

dihapus_5 = guest_list.pop()
print(f"Maaf {dihapus_5}, kami tidak bisa mengundang Anda.")

print("\n--- UNDANGAN FINAL (2 Orang Tersisa) ---")
print(f"Kepada Yth. {guest_list[0]}, Anda masih diundang!")
print(f"Kepada Yth. {guest_list[1]}, Anda masih diundang!")

# Menggunakan del untuk mengosongkan sisa list
del guest_list[0]
del guest_list[0] # Perhatikan: indeks 0 bergeser setelah elemen pertama dihapus

print("\n--- DAFTAR TAMU AKHIR ---")
print(f"Isi list saat ini (harus kosong): {guest_list}")