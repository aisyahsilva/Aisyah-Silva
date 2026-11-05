# Meminta input angka dari pengguna
number = input("Masukkan sebuah angka: ")
number = int(number)

# Memeriksa apakah sisa hasil bagi dengan 10 adalah 0
if number % 10 == 0:
    print(f"Angka {number} adalah kelipatan 10.")
else:
    print(f"Angka {number} bukan kelipatan 10.")