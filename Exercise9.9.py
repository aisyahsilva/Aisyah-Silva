class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini memiliki baterai berkapasitas {self.battery_size}-kWh.")

    def get_range(self):
        if self.battery_size == 40:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 225
        print(f"Mobil ini dapat menempuh jarak sekitar {range_miles} mil dengan pengisian penuh.")

    def upgrade_battery(self):
        """Memeriksa ukuran baterai dan mengubahnya ke 65 jika belum."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Baterai berhasil ditingkatkan menjadi 65 kWh.")
        else:
            print("Baterai sudah berada di kapasitas maksimum.")


class ElectricCar(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


# Membuat instance mobil listrik dengan baterai bawaan default
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

# Memanggil get_range() pertama kali (baterai default 40)
my_leaf.battery.get_range()

# Mengupgrade baterai dan memanggil get_range() kedua kalinya
print("\n-- Melakukan Upgrade Baterai --")
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()