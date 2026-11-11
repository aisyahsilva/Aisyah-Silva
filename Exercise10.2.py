# Tentukan nama file yang akan dibaca
FILE_NAME = 'Exercise10.txt'

print("--- Membaca File dan Mengganti Kata 'Python' menjadi 'C' ---")

with open(FILE_NAME) as file_object:
    for line in file_object:
        # Mengganti kata 'Python' dengan 'C' dan mencetaknya
        modified_line = line.replace('Python', 'C')
        print(modified_line.strip())