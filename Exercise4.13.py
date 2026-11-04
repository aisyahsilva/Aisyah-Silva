# buffet.py

# 1. Menyimpan 5 makanan dasar ke dalam sebuah tuple (menggunakan tanda kurung siku/biasa)
menu_items = ("Nasi Goreng", "Ayam Bakar", "Sup Tom Yum", "Mie Goreng", "Es Teh Manis")

print("--- MENU AWAL RESTORAN ---")
for food in menu_items:
    print(f"- {food}")


# 2. Mencoba memodifikasi salah satu item secara langsung (Akan memicu TypeError)
# Jika baris di bawah ini di-uncomment, Python akan menolak keras dan menghentikan program:
# menu_items[0] = "Bubur Ayam"


# 3. Restoran mengubah menu: mengganti 2 item (mengganti indeks 0 dan 1 dengan menu baru)
# Kita tidak bisa mengubah isi tuple yang sudah ada, tetapi kita bisa menimpa (reassign)
# variabel tuple tersebut dengan tuple yang baru.
menu_items = ("Soto Ayam", "Sate Madura", "Sup Tom Yum", "Mie Goreng", "Es Teh Manis")

print("\n--- MENU REVISI RESTORAN ---")
for food in menu_items:
    print(f"- {food}")