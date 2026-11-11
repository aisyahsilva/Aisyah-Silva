# Tentukan nama file yang akan dibaca
FILE_NAME = 'Exercise10.txt'

with open(FILE_NAME) as file_object:
    contents = file_object.read()

# Melakukan looping langsung tanpa menggunakan variabel sementara 'lines'
for line in contents.splitlines():
    print(line)