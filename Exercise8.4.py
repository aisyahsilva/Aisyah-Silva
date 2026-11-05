# Memodifikasi fungsi dengan nilai default (ukuran 'large', pesan 'I love Python')
def make_shirt(size='large', message='I love Python'):
    print(f"Membuat kaos ukuran {size.upper()} dengan cetakan pesan: '{message}'.")

# 1. Membuat kaos ukuran Large dengan pesan default
make_shirt()

# 2. Membuat kaos ukuran Medium dengan pesan default
make_shirt(size='medium')

# 3. Membuat kaos ukuran lain (misal: Small) dengan pesan kustom
make_shirt(size='S', message='Belajar Pemrograman Itu Seru!')