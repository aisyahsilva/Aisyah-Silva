import json

def get_stored_username(filename):
    """Mendapatkan username yang tersimpan jika ada."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(filename):
    """Meminta username baru dari pengguna."""
    username = input("Siapa nama Anda? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Menyapa pengguna dan memverifikasi identitasnya."""
    filename = 'username.json'
    username = get_stored_username(filename)
    
    if username:
        # Memverifikasi apakah username yang tersimpan adalah benar
        correct = input(f"Apakah '{username}' adalah username Anda? (y/n): ")
        if correct.lower() == 'y':
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(filename)
            print(f"Kami akan mengingat Anda saat kembali, {username}!")
    else:
        username = get_new_username(filename)
        print(f"Kami akan mengingat Anda saat kembali, {username}!")

greet_user()