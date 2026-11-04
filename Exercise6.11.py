cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': '10.5 juta',
        'fact': 'Merupakan pusat pemerintahan dan ekonomi negara.'
    },
    'tokyo': {
        'country': 'jepang',
        'population': '14 juta',
        'fact': 'Salah satu kota metropolitan terpadat di dunia.'
    },
    'paris': {
        'country': 'perancis',
        'population': '2.1 juta',
        'fact': 'Dikenal sebagai Kota Mode dan memiliki Menara Eiffel.'
    }
}

for city, info in cities.items():
    print(f"🌆 Kota: {city.title()}")
    print(f"\tNegara: {info['country'].title()}")
    print(f"\tPopulasi: Sekitar {info['population']}")
    print(f"\tFakta unik: {info['fact']}\n")