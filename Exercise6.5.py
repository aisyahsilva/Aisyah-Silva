# Membuat dictionary yang berisi sungai besar dan negaranya
rivers = {
    'nile': 'mesir',
    'amazon': 'brasil',
    'yangtze': 'china'
}

# 1. Mencetak kalimat tentang setiap sungai menggunakan perulangan
print("--- Informasi Sungai ---")
for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

# 2. Mencetak nama setiap sungai (keys)
print("\n--- Daftar Sungai ---")
for river in rivers.keys():
    print(river.title())

# 3. Mencetak nama setiap negara (values)
print("\n--- Daftar Negara ---")
for country in rivers.values():
    print(country.title())