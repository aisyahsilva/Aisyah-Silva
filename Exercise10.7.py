print("=== Kalkulator Penjumlahan ===")
print("Ketik 'q' kapan saja untuk keluar.\n")

while True:
    first_number = input("Angka pertama: ")
    if first_number.lower() == 'q':
        break
        
    second_number = input("Angka kedua: ")
    if second_number.lower() == 'q':
        break
        
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Error: Masukkan harus berupa angka! Silakan coba lagi.\n")
    else:
        print(f"Hasil penjumlahannya adalah: {answer}\n")