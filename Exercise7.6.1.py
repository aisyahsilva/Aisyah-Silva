print("--- Versi 1: Tes Kondisional di While ---")
topping = ""
while topping != 'quit':
    topping = input("Masukkan topping (ketik 'quit' untuk keluar): ")
    if topping != 'quit':
        print(f"Menambahkan {topping}!")