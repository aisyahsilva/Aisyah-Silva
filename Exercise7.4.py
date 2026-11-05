prompt = "\nMasukkan bahan topping pizza yang Anda inginkan:"
prompt += "\n(Ketik 'quit' untuk mengakhiri) "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        print("\nPesanan pizza Anda sedang disiapkan!")
        break
    else:
        print(f"Kami akan menambahkan {topping} ke pizza Anda.")