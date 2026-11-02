# stripping_names.py

# Variabel dengan karakter whitespace (\t untuk tab, \n untuk baris baru) di awal dan akhir
nama_dengan_spasi = "\t\n  Louis Elliot Jiho Jourdain Lim \n\t"

print("--- TAMPILAN ASLI ---")
print(nama_dengan_spasi)

print("\n--- MENGGUNAKAN lstrip() (Menghapus spasi kiri) ---")
print(nama_dengan_spasi.lstrip())

print("\n--- MENGGUNAKAN rstrip() (Menghapus spasi kanan) ---")
print(nama_dengan_spasi.rstrip())

print("\n--- MENGGUNAKAN strip() (Menghapus spasi kiri & kanan) ---")
print(nama_dengan_spasi.strip())