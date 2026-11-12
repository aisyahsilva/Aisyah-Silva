# city_functions.py

def city_country(city, country, population=''):
    """Mengembalikan string berbentuk 'Kota, Negara – populasi xxx'."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"