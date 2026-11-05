prompt = "\nBerapa usia Anda?"
prompt += "\n(Ketik 'keluar' untuk menghentikan program) "

while True:
    age_input = input(prompt)
    
    if age_input.lower() == 'keluar':
        print("Terima kasih telah menggunakan sistem tiket kami.")
        break
        
    age = int(age_input)
    
    if age < 3:
        print("Tiket Anda gratis!")
    elif age <= 12:
        print("Harga tiket Anda adalah $10.")
    else:
        print("Harga tiket Anda adalah $15.")