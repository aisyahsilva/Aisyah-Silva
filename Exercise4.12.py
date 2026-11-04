# more_loops.py

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# Menambahkan makanan berbeda ke masing-masing list
my_foods.append('cannoli')
friend_foods.append('ice cream')

# Mencetak list makanan saya menggunakan for loop
print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")

# Mencetak list makanan teman menggunakan for loop yang terpisah
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")