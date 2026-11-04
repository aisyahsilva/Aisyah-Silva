# seeing_the_world.py

# 1. Menyimpan 5 tempat impian (tidak berurutan secara alfabetis)
places = ["Tokyo", "Reykjavik", "Kyoto", "Cairo", "Banff"]

# 2. Cetak list dalam urutan asli (raw list)
print("--- URUTAN ASLI ---")
print(places)

# 3. Gunakan sorted() untuk mencetak urutan alfabetis tanpa mengubah list asli
print("\n--- URUTAN ALFABETIS (sorted) ---")
print(sorted(places))

# 4. Tunjukkan bahwa list asli masih dalam urutan awal
print("\n--- URUTAN ASLI (KEMBALI DICETAK) ---")
print(places)

# 5. Gunakan sorted() dengan parameter reverse=True untuk urutan alfabetis terbalik
print("\n--- URUTAN ALFABETIS TERBALIK (sorted reverse) ---")
print(sorted(places, reverse=True))

# 6. Tunjukkan lagi bahwa list asli tidak berubah
print("\n--- URUTAN ASLI (MASIH UTUH) ---")
print(places)

# 7. Gunakan reverse() untuk mengubah urutan list secara permanen
places.reverse()
print("\n--- SETELAH DIBALIK (reverse) ---")
print(places)

# 8. Gunakan reverse() lagi untuk mengembalikannya ke urutan semula
places.reverse()
print("\n--- DIKEMBALIKAN KE URUTAN SEMULA (reverse lagi) ---")
print(places)

# 9. Gunakan sort() untuk mengubah urutan list secara permanen menjadi alfabetis
places.sort()
print("\n--- DIURUTKAN PERMANEN (sort alfabetis) ---")
print(places)

# 10. Gunakan sort(reverse=True) untuk mengubah urutan secara permanen menjadi alfabetis terbalik
places.sort(reverse=True)
print("\n--- DIURUTKAN PERMANEN (sort terbalik) ---")
print(places)