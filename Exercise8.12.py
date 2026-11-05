# Mendefinisikan fungsi dengan parameter arbitrer (*items)
def make_sandwich(*items):
    """Mencetak ringkasan bahan-bahan sandwich yang dipesan."""
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for item in items:
        print(f"  - {item}")
    print("Sandwich Anda sedang disiapkan!")

# Memanggil fungsi tiga kali dengan jumlah argumen yang berbeda
make_sandwich('keju', 'tomat', 'daging')
make_sandwich('selai kacang', 'stroberi')
make_sandwich('ayam', 'selada', 'mayones', 'keju ekstra', 'bawang bombay')