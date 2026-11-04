# Inisialisasi variabel dengan nilai yang diminta
car = 'mazda'
age = 19
fruit = 'mango'
is_sunny = True
numbers = [1, 2, 3, 4, 5]

# --- 5 Pengujian yang Menghasilkan TRUE ---

# Tes 1: Memeriksa kesamaan string (sama)
print("1. Apakah car == 'mazda'? Saya memprediksi True.")
print(car == 'mazda')

# Tes 2: Memeriksa ketidaksamaan string (berbeda)
print("\n2. Apakah car != 'audi'? Saya memprediksi True.")
print(car != 'audi')

# Tes 3: Memeriksa perbandingan angka (lebih besar dari atau sama dengan)
print("\n3. Apakah age >= 18? Saya memprediksi True.")
print(age >= 18)

# Tes 4: Memeriksa penggunaan method string .lower()
print("\n4. Apakah fruit.lower() == 'mango'? Saya memprediksi True.")
print(fruit.lower() == 'mango')

# Tes 5: Memeriksa keberadaan elemen di dalam list
print("\n5. Apakah 3 ada di dalam list numbers? Saya memprediksi True.")
print(3 in numbers)


# --- 5 Pengujian yang Menghasilkan FALSE ---

# Tes 6: Memeriksa kesamaan string (berbeda)
print("\n6. Apakah car == 'audi'? Saya memprediksi False.")
print(car == 'audi')

# Tes 7: Memeriksa ketidaksamaan string (yang seharusnya sama)
print("\n7. Apakah car != 'mazda'? Saya memprediksi False.")
print(car != 'mazda')

# Tes 8: Memeriksa perbandingan angka (lebih kecil dari)
print("\n8. Apakah age < 18? Saya memprediksi False.")
print(age < 18)

# Tes 9: Memeriksa case sensitivity pada string (huruf kapital vs kecil)
print("\n9. Apakah fruit == 'Mango'? Saya memprediksi False.")
print(fruit == 'Mango')

# Tes 10: Memeriksa elemen yang tidak ada di dalam list
print("\n10. Apakah 10 ada di dalam list numbers? Saya memprediksi False.")
print(10 in numbers)