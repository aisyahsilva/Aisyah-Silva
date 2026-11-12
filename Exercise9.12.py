# my_admin_multiple.py
from Modul.Exercise9121 import Admin

# Membuat instance Admin
admin_user = Admin("Siti", "Aminah", "sitia")

# Memverifikasi bahwa semuanya bekerja dengan benar
admin_user.describe_user()
admin_user.privileges.show_privileges()