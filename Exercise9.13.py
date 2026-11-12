from random import randint

class Die:
    """Merepresentasikan sebuah dadu bersisi banyak."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Mencetak angka acak antara 1 dan jumlah sisi dadu."""
        print(randint(1, self.sides))


# 1. Membuat dadu 6-sisi dan melemparnya 10 kali
print("--- Lemparan Dadu 6 Sisi (10x) ---")
d6 = Die()
for _ in range(10):
    d6.roll_die()

# 2. Membuat dadu 10-sisi dan melemparnya 10 kali
print("\n--- Lemparan Dadu 10 Sisi (10x) ---")
d10 = Die(sides=10)
for _ in range(10):
    d10.roll_die()

# 3. Membuat dadu 20-sisi dan melemparnya 10 kali
print("\n--- Lemparan Dadu 20 Sisi (10x) ---")
d20 = Die(sides=20)
for _ in range(10):
    d20.roll_die()