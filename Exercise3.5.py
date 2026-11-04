
# Daftar tamu awal
guest_list = ["Kim Ryul", "Louis Elliot Jiho Jourdain Lim", "Jung Woojin", "Kwon Ohyul"]

# Cetak undangan pertama
print("--- UNDANGAN PERTAMA ---")
print(f"Kepada Yth. {guest_list[0]}, Anda diundang untuk makan malam bersama.")
print(f"Kepada Yth. {guest_list[1]}, Anda diundang untuk makan malam bersama.")
print(f"Kepada Yth. {guest_list[2]}, Anda diundang untuk makan malam bersama.")
print(f"Kepada Yth. {guest_list[3]}, Anda diundang untuk makan malam bersama.")

# Ada tamu yang tidak bisa hadir
tamu_tidak_bisa_hadir = "Jung Woojin"
print(f"\n[Info] Sayang sekali, {tamu_tidak_bisa_hadir} berhalangan hadir.\n")

# Mengganti tamu dengan yang baru
tamu_pengganti = "Han Sohee"
indeks_ganti = guest_list.index(tamu_tidak_bisa_hadir)
guest_list[indeks_ganti] = tamu_pengganti

# Cetak undangan kedua
print("--- UNDANGAN KEDUA ---")
print(f"Kepada Yth. {guest_list[0]}, Anda diundang untuk makan malam bersama.")
print(f"Kepada Yth. {guest_list[1]}, Anda diundang untuk makan malam bersama.")
print(f"Kepada Yth. {guest_list[2]}, Anda diundang untuk makan malam bersama.")
print(f"Kepada Yth. {guest_list[3]}, Anda diundang untuk makan malam bersama.")