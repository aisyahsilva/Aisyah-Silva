# File Utama: Exercise8.16.py
# Demonstrasi 5 Cara Mengimpor Modul dari Folder 'Modul'

print("--- 1. import module_name ---")
import Modul.Exercise16
car_1 = Modul.Exercise16.make_car('subaru', 'outback', color='blue')
print(car_1)


print("\n--- 2. from module_name import function_name ---")
from Modul.Exercise16 import make_car
car_2 = make_car('toyota', 'supra', year=2022)
print(car_2)


print("\n--- 3. from module_name import function_name as fn ---")
from Modul.Exercise16 import make_car as mc
car_3 = mc('honda', 'civic', transmission='automatic')
print(car_3)


print("\n--- 4. import module_name as mn ---")
import Modul.Exercise16 as cm
car_4 = cm.make_car('tesla', 'model 3', autopilot=True)
print(car_4)


print("\n--- 5. from module_name import * ---")
from Modul.Exercise16 import *
car_5 = make_car('ford', 'mustang', color='red', convertible=True)
print(car_5)