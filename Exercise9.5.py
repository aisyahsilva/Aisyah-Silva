class User:
    """Merepresentasikan profil pengguna."""

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0  # Atribut baru untuk menghitung percobaan login

    def describe_user(self):
        print(f"\nRingkasan Profil: {self.first_name} {self.last_name}")
        print(f"  - Username: {self.username}")
        print(f"  - Email: {self.email}")
        print(f"  - Lokasi: {self.location}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali di sistem kami.")

    def increment_login_attempts(self):
        """Menaikkan nilai login_attempts sebesar 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mengembalikan nilai login_attempts menjadi 0."""
        self.login_attempts = 0


# Membuat instance dari User class
user_1 = User('Budi', 'Santoso', 'bsantoso', 'budi@email.com', 'Jakarta')

# Memanggil increment_login_attempts() beberapa kali
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

# Mencetak nilai login_attempts untuk memastikan bertambah
print(f"Jumlah percobaan login: {user_1.login_attempts}")

# Memanggil reset_login_attempts()
user_1.reset_login_attempts()

# Mencetak login_attempts lagi untuk memastikan kembali ke 0
print(f"Jumlah percobaan login setelah di-reset: {user_1.login_attempts}")