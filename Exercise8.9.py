def show_messages(messages):
    """Mencetak setiap pesan teks dari daftar yang diberikan."""
    for message in messages:
        print(message)

# Membuat list pesan
messages_list = [
    "Halo, bagaimana kabarmu?",
    "Jangan lupa pasang reminder rapat besok.",
    "Kode programnya sudah berjalan dengan lancar!"
]

# Memanggil fungsi
show_messages(messages_list)