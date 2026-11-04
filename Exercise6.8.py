# Membuat dictionary hewan peliharaan
pet_1 = {'animal': 'kucing', 'owner': 'budi'}
pet_2 = {'animal': 'anjing', 'owner': 'siti'}
pet_3 = {'animal': 'burung', 'owner': 'andi'}

# Menyimpan ke dalam list 'pets'
pets = [pet_1, pet_2, pet_3]

# Melakukan perulangan untuk mencetak informasi hewan
for pet in pets:
    print(f"Jenis Hewan: {pet['animal'].title()}")
    print(f"Nama Pemilik: {pet['owner'].title()}\n")