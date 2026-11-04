# my_pizzas_your_pizzas.py

# List awal pizza favorit saya
pizzas = ["Pepperoni", "Meat Lovers", "Cheese Pizza"]

# Menyalin list menggunakan irisan [:] agar menjadi dua objek terpisah di memori
friend_pizzas = pizzas[:]

# Menambahkan pizza baru ke list asli (saya)
pizzas.append("Supreme")

# Menambahkan pizza berbeda ke list teman
friend_pizzas.append("Quattro Formaggi")

# Membuktikan bahwa kedua list terpisah
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")