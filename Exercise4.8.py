# cubes.py

cubes = []

# Menghitung kubik (pangkat 3) dari angka 1 sampai 10
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

# Mencetak hasil setiap kubik
for cube in cubes:
    print(cube)