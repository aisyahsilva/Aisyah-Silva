class Restaurant:
    """Model sederhana untuk sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Atribut baru dengan nilai awal 0

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restoran {self.restaurant_name} saat ini sedang buka!")

    def set_number_served(self, number):
        """Mengatur jumlah pelanggan yang telah dilayani."""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """Menambahkan jumlah pelanggan yang telah dilayani."""
        self.number_served += additional_customers


# Membuat instance restaurant
restaurant = Restaurant('Sederhana', 'Masakan Padang')

# 1. Mencetak jumlah pelanggan awal
print(f"Jumlah pelanggan yang dilayani: {restaurant.number_served}")

# 2. Mengubah nilai secara langsung dan mencetak kembali
restaurant.number_served = 15
print(f"Jumlah pelanggan setelah diubah: {restaurant.number_served}")

# 3. Memanggil method set_number_served() dengan angka baru
restaurant.set_number_served(50)
print(f"Jumlah pelanggan setelah set_number_served(): {restaurant.number_served}")

# 4. Memanggil method increment_number_served()
restaurant.increment_number_served(25)
print(f"Jumlah pelanggan setelah increment_number_served(): {restaurant.number_served}")