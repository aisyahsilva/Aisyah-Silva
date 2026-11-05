def describe_city(city, country='indonesia'):
    """Mencetak kalimat sederhana yang menyatakan letak sebuah kota."""
    print(f"{city.title()} berada di negara {country.title()}.")


# Pemanggilan fungsi dengan mematuhi standar gaya
describe_city('jakarta')
describe_city('tokyo', country='jepang')