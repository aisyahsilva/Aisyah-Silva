# File Utama: Exercise8.15.py
# Menarik fungsi dari file Exercise15 yang berada di dalam folder Modul
from Modul.Exercise15 import print_models, show_completed_models

# Data awal
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Memanggil fungsi yang sudah diimpor
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)