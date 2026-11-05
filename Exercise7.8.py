# Daftar pesanan sandwich
sandwich_orders = ['tuna', 'ayam', 'keju', 'roti bakar', 'daging sapi']
finished_sandwiches = []

# Memproses setiap pesanan hingga list pesanan kosong
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()  # Mengambil pesanan dari akhir list
    print(f"Saya telah membuat sandwich {current_sandwich} Anda.")
    finished_sandwiches.append(current_sandwich)

# Menampilkan daftar sandwich yang sudah selesai dibuat
print("\n--- Daftar Sandwich yang Selesai ---")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")