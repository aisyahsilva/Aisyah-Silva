favorite_places = {
    'budi': ['raja ampat', 'bromo', 'bali'],
    'siti': ['yogyakarta', 'bandung'],
    'andi': ['tokyo']
}

for name, places in favorite_places.items():
    print(f"Tempat-tempat favorit {name.title()} adalah:")
    for place in places:
        print(f"\t- {place.title()}")
    print()