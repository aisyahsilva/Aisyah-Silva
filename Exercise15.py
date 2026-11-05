def print_models(unprinted_designs, completed_models):
    """Mensimulasikan pencetakan desain satu per satu hingga habis."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Mencetak model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Menampilkan semua model yang sudah berhasil dicetak."""
    print("\nModel berikut telah berhasil dicetak:")
    for completed_model in completed_models:
        print(f" - {completed_model}")