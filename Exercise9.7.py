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


class Admin(User):
    """Merepresentasikan pengguna khusus dengan hak akses admin."""

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = ["can add post", "can delete post", "can ban user", "can reset password"]

    def show_privileges(self):
        """Menampilkan daftar hak akses yang dimiliki admin."""
        print(f"\nDaftar Hak Akses Admin ({self.username}):")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Membuat instance Admin dan memanggil metodenya
admin_user = Admin("Ahmad", "Fauzi", "fauzi_admin", "fauzi@email.com", "Bandung")
admin_user.describe_user()
admin_user.show_privileges()