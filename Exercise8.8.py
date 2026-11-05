def make_album(artist, title, songs=None):
    album = {
        'artist': artist.title(),
        'title': title.title()
    }
    if songs:
        album['songs'] = int(songs)
    return album

print("=== PENDATAAN ALBUM MUSIK ===")
print("Ketik 'quit' kapan saja untuk menghentikan program.\n")

while True:
    artist_input = input("Masukkan nama artis/band: ")
    if artist_input.lower() == 'quit':
        break
        
    title_input = input("Masukkan judul album: ")
    if title_input.lower() == 'quit':
        break
        
    songs_input = input("Masukkan jumlah lagu (opsional, tekan Enter jika dilewati): ")
    if songs_input.lower() == 'quit':
        break
        
    # Memanggil fungsi berdasarkan ketersediaan input jumlah lagu
    if songs_input:
        user_album = make_album(artist_input, title_input, songs=songs_input)
    else:
        user_album = make_album(artist_input, title_input)
        
    print("\nDictionary Album yang Berhasil Dibuat:")
    print(user_album)
    print("-" * 40)

print("\nTerima kasih telah menggunakan program pendataan album!")