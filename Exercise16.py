# Modul: Modul/Exercise16.py

def make_car(manufacturer, model, **options):
    """Membuat dictionary yang merepresentasikan informasi mobil."""
    car = {
        'manufacturer': manufacturer, 
        'model': model
    }
    car.update(options)
    return car