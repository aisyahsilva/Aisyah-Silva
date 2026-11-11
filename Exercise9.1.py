class Restaurant:
    """Model sederhana untuk sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restoran {self.restaurant_name} saat ini sedang buka!")


# Membuat instance bernama restaurant
restaurant = Restaurant('Sederhana', 'Masakan Padang')

# Mencetak atribut secara individual
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Memanggil kedua metode
restaurant.describe_restaurant()
restaurant.open_restaurant()