# Dictionary bahasa favorit yang sudah ada
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# List orang yang seharusnya mengikuti polling 
# (beberapa sudah ada di dictionary, beberapa belum)
coders_to_poll = ['jen', 'budi', 'sarah', 'dewi', 'phil', 'joko']

# Perulangan untuk memeriksa status polling setiap orang
for person in coders_to_poll:
    if person in favorite_languages:
        print(f"Terima kasih, {person.title()}, karena sudah meluangkan waktu merespons polling.")
    else:
        print(f"Halo {person.title()}, Anda diundang untuk mengikuti polling bahasa pemrograman kami!")