from random import choice

def get_winning_ticket(pool):
    """Mengambil 4 kombinasi pemenang secara acak."""
    winning_ticket = []
    while len(winning_ticket) < 4:
        item = choice(pool)
        if item not in winning_ticket:
            winning_ticket.append(item)
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    """Memeriksa apakah seluruh elemen tiket saya cocok dengan pemenang."""
    for item in played_ticket:
        if item not in winning_ticket:
            return False
    return True

# Kumpulan elemen lotre
lottery_pool = (1, 3, 5, 7, 9, 12, 15, 18, 20, 25, 'a', 'b', 'c', 'd', 'e')

# Tiket yang saya miliki
my_ticket = (7, 'b', 20, 3)

# Menghitung berapa kali percobaan loop hingga menang
plays = 0
won = False

print("Sedang memproses simulasi undian...")

while not won:
    new_winning_ticket = get_winning_ticket(lottery_pool)
    plays += 1
    
    # Karena urutan bisa diabaikan atau disesuaikan, kita cek kecocokannya
    if set(my_ticket) == set(new_winning_ticket):
        won = True

print(f"\nBerhasil! Tiket Anda ({my_ticket}) cocok dengan pemenang.")
print(f"Loop harus berjalan sebanyak {plays:,} kali untuk mendapatkan tiket kemenangan.")