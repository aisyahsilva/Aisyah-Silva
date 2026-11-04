# slices.py

# Membuat list berisi beberapa jenis pizza
pizzas = ["Pepperoni", "Meat Lovers", "Cheese Pizza", "Hawaiian", "Veggie", "BBQ Chicken"]

# 1. Tiga item pertama
print("The first three items in the list are:")
print(pizzas[:3])

# 2. Tiga item dari bagian tengah
# Mengambil indeks ke-1 sampai ke-4 (indeks 4 tidak termasuk)
print("\nThree items from the middle of the list are:")
print(pizzas[1:4])

# 3. Tiga item terakhir
# Menggunakan indeks negatif untuk menghitung dari belakang
print("\nThe last three items in the list are:")
print(pizzas[-3:])