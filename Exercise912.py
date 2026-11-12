# user.py

class User:
    """Merepresentasikan profil pengguna secara umum."""
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def describe_user(self):
        print(f"Pengguna: {self.first_name} {self.last_name} (@{self.username})")