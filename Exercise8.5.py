# Mendefinisikan fungsi dengan nilai default untuk parameter country
def describe_city(city, country='indonesia'):
    print(f"{city.title()} berada di negara {country.title()}.")

# 1. Memanggil fungsi menggunakan negara default ('indonesia')
describe_city('jakarta')

# 2. Memanggil fungsi untuk kota lain di Indonesia menggunakan nilai default
describe_city('bandung')

# 3. Memanggil fungsi untuk kota yang TIDAK berada di negara default (menyertakan argumen country)
describe_city('tokyo', country='jepang')