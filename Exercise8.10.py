def send_messages(messages_to_send, sent_messages):
    """Mencetak pesan dan memindahkannya ke daftar pesan terkirim."""
    while messages_to_send:
        current_message = messages_to_send.pop(0) # Mengambil pesan pertama (indeks 0)
        print(f"Mengirim pesan: '{current_message}'")
        sent_messages.append(current_message)

# List awal
messages_list = [
    "Halo, bagaimana kabarmu?",
    "Jangan lupa pasang reminder rapat besok.",
    "Kode programnya sudah berjalan dengan lancar!"
]
sent_messages = []

# Memanggil fungsi
send_messages(messages_list, sent_messages)

# Memeriksa isi kedua list setelah fungsi dijalankan
print("\n--- Status List Setelah Pengiriman ---")
print(f"messages_list (asal): {messages_list}")
print(f"sent_messages (terkirim): {sent_messages}")