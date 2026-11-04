# Perluasan dari Latihan 6-11 dengan menambahkan kunci 'landmarks'
cities_extended = {
    'jakarta': {
        'country': 'indonesia',
        'population': '10.5 juta',
        'fact': 'Merupakan pusat pemerintahan dan ekonomi negara.',
        'landmarks': ['Monumen Nasional (Monas)', 'Kota Tua', 'Gelora Bung Karno']
    },
    'tokyo': {
        'country': 'jepang',
        'population': '14 juta',
        'fact': 'Salah satu kota metropolitan terpadat di dunia.',
        'landmarks': ['Tokyo Skytree', 'Shibuya Crossing', 'Kuil Senso-ji']
    },
    'paris': {
        'country': 'perancis',
        'population': '2.1 juta',
        'fact': 'Dikenal sebagai Kota Mode dan memiliki Menara Eiffel.',
        'landmarks': ['Menara Eiffel', 'Museum Louvre', 'Katedral Notre-Dame']
    }
}

print("=" * 50)
print(" INFORMASI PARIWISATA KOTA DUNIA")
print("=" * 50)

for city, info in cities_extended.items():
    print(f"\n📍 Kota: {city.title()} ({info['country'].title()})")
    print(f"   • Perkiraan Populasi : {info['population']}")
    print(f"   • Fakta Utama        : {info['fact']}")
    print(f"   • Landmark Populer   :")
    for landmark in info['landmarks']:
        print(f"     - {landmark}")
    print("-" * 50)