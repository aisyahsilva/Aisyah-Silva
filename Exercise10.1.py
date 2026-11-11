# Tentukan nama file yang akan dibaca
FILE_NAME = 'Exercise10.txt'

print("--- 1. Membaca Seluruh File Sekaligus ---")
with open(FILE_NAME) as file_object:
    # Membaca seluruh isi file ke dalam satu string
    contents = file_object.read()
    print(contents.strip())

print("\n--- 2. Menyimpan Baris ke dalam List dan Melakukan Looping ---")
with open(FILE_NAME) as file_object:
    # Menyimpan setiap baris ke dalam list menggunakan readlines()
    lines = file_object.readlines()

# Melakukan perulangan untuk mencetak setiap baris
for line in lines:
    print(line.strip())