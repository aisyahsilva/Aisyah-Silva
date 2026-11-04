# more_guests.py

# Daftar tamu dari latihan sebelumnya
guest_list = ["Kim Ryul", "Louis Elliot Jiho Jourdain Lim", "Han Sohee", "Kwon Ohyul"]

print("[Info] Kabar baik! Kami menemukan meja makan yang lebih besar.\n")

# Menambahkan tamu baru menggunakan insert() dan append()
guest_list.insert(0, "Park Seo-jun")                # Menambah di awal list
guest_list.insert(int(len(guest_list) / 2), "IU")   # Menambah di tengah list
guest_list.append("Son Heung-min")                  # Menambah di akhir list

# Cetak undangan baru untuk semua orang
print("--- UNDANGAN MEJA BESAR ---")
print(f"Kepada Yth. {guest_list[0]}, Anda diundang untuk makan malam.")
print(f"Kepada Yth. {guest_list[1]}, Anda diundang untuk makan malam.")
print(f"Kepada Yth. {guest_list[2]}, Anda diundang untuk makan malam.")
print(f"Kepada Yth. {guest_list[3]}, Anda diundang untuk makan malam.")
print(f"Kepada Yth. {guest_list[4]}, Anda diundang untuk makan malam.")
print(f"Kepada Yth. {guest_list[5]}, Anda diundang untuk makan malam.")
print(f"Kepada Yth. {guest_list[6]}, Anda diundang untuk makan malam.")