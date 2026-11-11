print("Masukkan dua angka untuk dijumlahkan.")
first_number = input("Angka pertama: ")
second_number = input("Angka kedua: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Maaf, input yang Anda masukkan harus berupa angka, bukan teks.")
else:
    print(f"Hasil penjumlahannya adalah: {answer}")