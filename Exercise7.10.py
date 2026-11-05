# Dictionary untuk menyimpan hasil polling
dream_vacations = {}

# Variabel aktif untuk mengontrol perulangan polling
polling_active = True

while polling_active:
    # Meminta input nama dan tempat impian dari pengguna
    name = input("\nSiapa nama Anda? ").strip()
    location = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ").strip()
    
    # Menyimpan data ke dalam dictionary
    dream_vacations[name] = location
    
    # Menanyakan apakah ada orang lain yang ingin mengikuti polling
    repeat = input("Apakah ada orang lain yang ingin ikut polling? (ketik 'tidak' untuk berhenti): ").strip().lower()
    if repeat == 'tidak':
        polling_active = False

# Mencetak hasil rangkuman polling
print("\n--- 📊 Rangkuman Hasil Polling Liburan Impian ---")
for name, location in dream_vacations.items():
    print(f"{name.title()} ingin sekali mengunjungi {location.title()}.")