# Membuat glosarium istilah pemrograman
glossary = {
    'dictionary': 'Struktur data di Python yang menyimpan data dalam bentuk pasangan kunci-nilai (key-value pairs).',
    'loop': 'Blok kode untuk melakukan pengulangan terhadap sekumpulan item secara otomatis.',
    'string': 'Tipe data yang digunakan untuk menyimpan teks dan diapit oleh tanda kutip.',
    'list': 'Kumpulan item yang disusun secara berurutan dan nilainya dapat diubah (mutable).',
    'conditional': 'Pernyataan (seperti if-elif-else) yang digunakan untuk mengevaluasi kondisi dan membuat keputusan dalam program.'
}

# Mencetak kata dan artinya secara rapi
for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")