# Membuat dictionary angka favorit
favorite_numbers = {
    'andi': 7,
    'siti': 12,
    'budi': 42,
    'rina': 3,
    'eko': 99
}

# Menggunakan perulangan untuk mencetak nama dan angka favorit
for name, number in favorite_numbers.items():
    print(f"Angka favorit {name.title()} adalah {number}.")