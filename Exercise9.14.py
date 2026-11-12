from random import choice

# Membuat list/tuple berisi 10 angka dan 5 huruf
lottery_pool = (1, 3, 5, 7, 9, 12, 15, 18, 20, 25, 'a', 'b', 'c', 'd', 'e')

# Memilih 4 elemen secara acak
winning_ticket = []
while len(winning_ticket) < 4:
    selected_item = choice(lottery_pool)
    # Memastikan tidak ada elemen duplikat yang terpilih
    if selected_item not in winning_ticket:
        winning_ticket.append(selected_item)

# Mencetak hasil undian pemenang
print("=== UNDIAN LOTRE ===")
print(f"Tiket yang cocok dengan kombinasi berikut dinyatakan sebagai pemenang: {winning_ticket}")