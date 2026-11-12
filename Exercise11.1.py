# test_cities.py
from Modul.Exercise111 import city_country

def test_city_country():
    """Memverifikasi bahwa kombinasi kota dan negara berfungsi dengan benar."""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == "Santiago, Chile"

def test_city_country_population():
    """Memverifikasi bahwa fungsi juga dapat menerima parameter populasi."""
    santiago_chile = city_country('santiago', 'chile', population=5000000)
    assert santiago_chile == "Santiago, Chile – population 5000000"