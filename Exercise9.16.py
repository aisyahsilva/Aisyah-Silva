import random

# List kartu atau data
cards = ['As', 'King', 'Queen', 'Jack', '10']

# Mengacak posisi elemen di dalam list secara langsung (shuffle)
random.shuffle(cards)
print(f"Hasil setelah di-acak (shuffle): {cards}")

# Mengambil beberapa sampel acak sekaligus (sample)
lucky_draw = random.sample(cards, k=2)
print(f"Sampel acak terpilih: {lucky_draw}")