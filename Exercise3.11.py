# intentional_error.py

# Membuat list berisi 3 elemen (indeks yang valid adalah 0, 1, dan 2)
mountain_peaks = ["Everest", "Kilimanjaro", "Denali"]

print("Daftar gunung:")
print(mountain_peaks)

# --- SENGAJA MEMICU INDEX ERROR ---
# List di atas hanya punya 3 elemen, jadi indeks maksimumnya adalah 2.
# Jika kita mencoba mengakses indeks 3 atau angka yang lebih besar, Python akan protes.
# 
# print(mountain_peaks[3])  # <- Baris ini akan memicu IndexError!


# --- KOREKSI KODE (CORRECTED VERSION) ---
# Untuk memperbaikinya, pastikan kita hanya memanggil indeks yang benar-benar ada.
# Indeks terakhir dari list di atas adalah len(mountain_peaks) - 1, yaitu 2.
print("\n--- SETELAH DIKOREKSI ---")
print(f"Gunung terakhir dalam list adalah: {mountain_peaks[2]}")