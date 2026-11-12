# city_functions.py

def city_country(city, country, population=''):
    """Mengembalikan string dengan format 'Kota, Negara – population xxx' atau 'Kota, Negara'."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"