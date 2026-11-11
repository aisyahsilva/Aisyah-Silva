import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("Berapa angka favorit Anda? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("Angka favorit Anda telah disimpan!")
else:
    print(f"I know your favorite number! It’s {number}.")