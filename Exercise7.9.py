# Daftar pesanan dengan 'pastrami' muncul beberapa kali
sandwich_orders = [
    'pastrami', 'tuna', 'pastrami', 'ayam', 
    'keju', 'pastrami', 'roti bakar'
]
finished_sandwiches = []

print("⚠️ Maaf, toko deli kehabisan stok pastrami hari ini!\n")

# Menghapus semua kemunculan 'pastrami' menggunakan while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Memproses sisa pesanan sandwich yang ada
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Saya telah membuat sandwich {current_sandwich} Anda.")
    finished_sandwiches.append(current_sandwich)

# Menampilkan daftar sandwich yang berhasil dibuat
print("\n--- Daftar Sandwich yang Selesai ---")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")