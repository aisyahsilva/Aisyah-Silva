favorite_numbers = {
    'andi': [7, 14, 21],
    'siti': [12, 5],
    'budi': [42, 88, 100],
    'rina': [3],
    'eko': [99, 1, 50]
}

for name, numbers in favorite_numbers.items():
    print(f"Angka favorit {name.title()} adalah:")
    for number in numbers:
        print(f"\t{number}")
    print()