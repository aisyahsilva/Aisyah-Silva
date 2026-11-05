# Mendefinisikan fungsi make_album dengan parameter opsional songs=None
def make_album(artist, title, songs=None):
    """Membangun dictionary yang mendeskripsikan album musik."""
    album = {
        'artist': artist.title(),
        'title': title.title()
    }
    
    # Jika parameter songs diisi, tambahkan ke dalam dictionary
    if songs:
        album['songs'] = songs
        
    return album

# Membuat tiga dictionary album berbeda
album_1 = make_album('metallica', 'ride the lightning')
album_2 = make_album('taylor swift', '1989')
album_3 = make_album('ed sheeran', 'divide', songs=16) # Menyertakan jumlah lagu

# Mencetak setiap nilai kembalian
print(album_1)
print(album_2)
print(album_3)