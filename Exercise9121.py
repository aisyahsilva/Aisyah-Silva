# admin_privileges.py
from Exercise912 import User

class Privileges:
    """Menyimpan daftar hak istimewa (privileges) milik admin."""
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("Hak istimewa Admin:")
        for priv in self.privileges:
            print(f"- {priv}")


class Admin(User):
    """Kelas khusus untuk pengguna bertipe Admin."""
    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privileges = Privileges()