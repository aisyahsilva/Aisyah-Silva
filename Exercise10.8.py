filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\n--- Membaca file: {filename} ---")
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            print(contents.strip())
    except FileNotFoundError:
        print(f"Maaf, file '{filename}' tidak ditemukan di direktori ini.")