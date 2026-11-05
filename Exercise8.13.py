# Mendefinisikan fungsi build_profile dengan parameter **user_info untuk menampung argumen kata kunci arbitrer
def build_profile(first, last, **user_info):
    """Membangun dictionary yang berisi segala hal yang kita ketahui tentang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Membuat profil diri (silakan sesuaikan data di bawah ini)
my_profile = build_profile(
    'budi', 'santoso',
    location='jakarta',
    field='python programming',
    hobby='membaca buku'
)

print("--- Profil Pengguna ---")
print(my_profile)