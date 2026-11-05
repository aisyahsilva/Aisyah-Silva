# Mendefinisikan fungsi city_country
def city_country(city, country):
    """Mengembalikan string dengan format 'Kota, Negara'."""
    formatted_location = f"{city.title()}, {country.title()}"
    return formatted_location

# Memanggil fungsi dengan tiga pasang kota-negara dan mencetak hasilnya
print(city_country('santiago', 'chile'))
print(city_country('jakarta', 'indonesia'))
print(city_country('tokyo', 'jepang'))