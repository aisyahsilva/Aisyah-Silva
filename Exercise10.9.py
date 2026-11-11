filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            print(f"\nIsi file {filename}:\n{contents.strip()}")
    except FileNotFoundError:
        pass  # Gagal secara senyap tanpa menampilkan pesan error