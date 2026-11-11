# Ganti dengan nama file teks Project Gutenberg Anda
filename = 'sample_text.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Maaf, file '{filename}' tidak ditemukan.")
else:
    # 1. Menghitung kata 'the' (termasuk yang berada di dalam kata lain seperti 'then' atau 'there')
    count_the = contents.lower().count('the')
    print(f"Kata 'the' muncul sebanyak: {count_the} kali")
    
    # 2. Menghitung kata 'the ' dengan spasi di belakangnya (lebih akurat)
    count_the_space = contents.lower().count('the ')
    print(f"Kata 'the ' (dengan spasi) muncul sebanyak: {count_the_space} kali")