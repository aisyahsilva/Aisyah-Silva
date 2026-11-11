class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restoran: {self.restaurant_name}, Jenis Masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restoran {self.restaurant_name} sedang buka!")


# Membuat tiga instance berbeda dari class Restaurant
restaurant_1 = Restaurant('KFC', 'Fast Food')
restaurant_2 = Restaurant('Bebek Kaleyo', 'Kuliner Nusantara')
restaurant_3 = Restaurant('Sushi Tei', 'Jepang')

# Memanggil describe_restaurant() untuk setiap instance
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()