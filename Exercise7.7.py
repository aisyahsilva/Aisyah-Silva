# Contoh Infinite Loop (Jangan dijalankan di lingkungan yang tidak mendukung interupsi)
x = 1
while x <= 5:
    print(f"Nilai x adalah: {x}")
    # Jika kita lupa menuliskan 'x += 1' di sini, 
    # nilai x akan selalu 1 dan loop tidak akan pernah berhenti!