# Program Mini Game: Tebak Angka Pintar
import random

def play_guessing_game():
    print("=== SELAMAT DATANG DI GAME TEBAK ANGKA ===")
    target_number = random.randint(1, 50)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Tebak angka antara 1 sampai 50: "))
            attempts += 1
            
            if guess < target_number:
                print("Terlalu kecil! Coba lagi.")
            elif guess > target_number:
                print("Terlalu besar! Coba lagi.")
            else:
                print(f"🎉 Luar biasa! Anda berhasil menebak dalam {attempts} percobaan.")
                break
        except ValueError:
            print("Mohon masukkan angka yang valid!")

# Menjalankan game
play_guessing_game()