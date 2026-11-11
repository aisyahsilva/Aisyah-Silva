class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\nProfil: {self.first_name} {self.last_name} (@{self.username})")
        print(f"  - Email: {self.email}")
        print(f"  - Lokasi: {self.location}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")


class Privileges:
    """Kelas terpisah untuk mengelola daftar hak akses."""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Menampilkan daftar hak akses."""
        print("Daftar Hak Akses:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Merepresentasikan admin yang menggunakan instance class Privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()  # Menjadikan instance Privileges sebagai atribut


# Membuat instance Admin dan menggunakan metode show_privileges dari kelas Privileges
admin_user = Admin("Siti", "Rahma", "siti_admin", "siti@email.com", "Surabaya")
admin_user.describe_user()
admin_user.privileges.show_privileges()