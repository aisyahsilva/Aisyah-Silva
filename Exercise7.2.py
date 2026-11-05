# Meminta input jumlah orang dan mengonversinya ke tipe integer
group_size = input("Berapa banyak orang yang ada di rombongan makan malam Anda? ")
group_size = int(group_size)

# Mengevaluasi ketersediaan meja berdasarkan jumlah rombongan
if group_size > 8:
    print("Maaf, rombongan Anda lebih dari 8 orang. Anda harus menunggu meja kosong.")
else:
    print("Meja Anda sudah siap! Silakan masuk.")