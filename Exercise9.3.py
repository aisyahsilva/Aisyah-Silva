class User:
    """Merepresentasikan profil pengguna."""

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\nRingkasan Profil: {self.first_name} {self.last_name}")
        print(f"  - Username: {self.username}")
        print(f"  - Email: {self.email}")
        print(f"  - Lokasi: {self.location}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali di sistem kami.")


# Membuat beberapa instance yang merepresentasikan pengguna berbeda
user_1 = User('Budi', 'Santoso', 'bsantoso', 'budi@email.com', 'Jakarta')
user_2 = User('Siti', 'Aisyah', 'siti_a', 'siti@email.com', 'Bandung')
user_3 = User('Joko', 'Widodo', 'jokow', 'joko@email.com', 'Surakarta')

# Memanggil kedua metode untuk setiap pengguna
for user in (user_1, user_2, user_3):
    user.describe_user()
    user.greet_user()