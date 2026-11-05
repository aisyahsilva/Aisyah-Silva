# Mendefinisikan fungsi make_shirt
def make_shirt(size, message):
    print(f"Membuat kaos ukuran {size.upper()} dengan cetakan pesan: '{message}'.")

# 1. Memanggil fungsi menggunakan argumen posisional (berdasarkan urutan)
make_shirt('L', 'Keep Calm and Code On')

# 2. Memanggil fungsi menggunakan argumen kata kunci (menyebutkan nama parameter)
make_shirt(size='M', message='Python Developer')