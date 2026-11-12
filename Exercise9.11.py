# my_admin.py
from Modul.Exercise911 import Admin

# Membuat instance Admin
admin_user = Admin("Budi", "Santoso", "budis")

# Memanggil metode describe_user dan show_privileges
admin_user.describe_user()
admin_user.privileges.show_privileges()