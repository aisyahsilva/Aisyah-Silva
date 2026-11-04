# every_function.py

# Membuat list awal berisi beberapa negara
countries = ["Jepang", "Kanada", "Norwegia", "Selandia Baru", "Swiss"]

print("--- 1. KONDISI AWAL ---")
print(countries)
print(f"Jumlah elemen awal (len): {len(countries)}")

# 2. append() - Menambahkan elemen di akhir list
countries.append("Islandia")
print("\n--- 2. SETELAH APPEND ('Islandia') ---")
print(countries)

# 3. insert() - Menambahkan elemen pada indeks tertentu
countries.insert(1, "Belgia")
print("\n--- 3. SETELAH INSERT ('Belgia' di indeks 1) ---")
print(countries)

# 4. del - Menghapus elemen berdasarkan posisi indeks
del countries[0]
print("\n--- 4. SETELAH DEL (Menghapus indeks ke-0) ---")
print(countries)

# 5. pop() - Menghapus elemen terakhir dan mengambil nilainya
popped_country = countries.pop()
print(f"\n--- 5. SETELAH POP (Menghapus '{popped_country}' dari akhir) ---")
print(countries)

# 6. remove() - Menghapus elemen berdasarkan nama nilainya
countries.remove("Kanada")
print("\n--- 6. SETELAH REMOVE ('Kanada') ---")
print(countries)

# 7. sorted() - Mengurutkan sementara tanpa merusak list asli
print("\n--- 7. PENGGUNAAN SORTED (Sementara) ---")
print("Hasil sorted:", sorted(countries))
print("List asli tetap aman:", countries)

# 8. reverse() - Membalik urutan list secara permanen
countries.reverse()
print("\n--- 8. SETELAH REVERSE (Dibalik permanen) ---")
print(countries)

# 9. sort() - Mengurutkan list secara permanen (sesuai abjad)
countries.sort()
print("\n--- 9. SETELAH SORT (Diurutkan alfabetis permanen) ---")
print(countries)

# Mengurutkan terbalik secara permanen
countries.sort(reverse=True)
print("\n--- SETELAH SORT REVERSE (Alfabetis terbalik permanen) ---")
print(countries)