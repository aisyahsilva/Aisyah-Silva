class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restoran {self.restaurant_name} sedang buka!")


class IceCreamStand(Restaurant):
    """Merepresentasikan kedai es krim yang merupakan jenis khusus dari restoran."""

    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Matcha', 'Cookies & Cream']

    def display_flavors(self):
        """Menampilkan daftar rasa es krim yang tersedia."""
        print("\nDaftar rasa es krim yang tersedia:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Membuat instance dari IceCreamStand dan memanggil metodenya
my_ice_cream_stand = IceCreamStand("Sweet Scoop")
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()