# Membuat glosarium istilah pemrograman yang diperluas (total 10 kata)
glossary = {
    'dictionary': 'Struktur data di Python yang menyimpan data dalam bentuk pasangan kunci-nilai (key-value pairs).',
    'loop': 'Blok kode untuk melakukan pengulangan terhadap sekumpulan item secara otomatis.',
    'string': 'Tipe data yang digunakan untuk menyimpan teks dan diapit oleh tanda kutip.',
    'list': 'Kumpulan item yang disusun secara berurutan dan nilainya dapat diubah (mutable).',
    'conditional': 'Pernyataan (seperti if-elif-else) yang digunakan untuk mengevaluasi kondisi dan membuat keputusan dalam program.',
    'variable': 'Wadah atau tempat untuk menyimpan nilai data di dalam memori komputer.',
    'integer': 'Tipe data numerik yang merepresentasikan angka bulat tanpa desimal.',
    'boolean': 'Tipe data yang hanya memiliki dua nilai, yaitu True (benar) atau False (salah).',
    'tuple': 'Kumpulan item yang mirip dengan list, tetapi bersifat immutable (tidak dapat diubah setelah dibuat).',
    'function': 'Blok kode terorganisasi dan dapat digunakan kembali yang dirancang untuk melakukan tugas tertentu.'
}

# Melakukan perulangan untuk mencetak setiap kata dan artinya secara otomatis
for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")