import os
carpeta = "practica9_mendez_maria_1199.txt"

try:
    os.rmdir(carpeta)
    print(f"La carpeta'{carpeta}' ha sido eliminada.")
except FileNotFoundError:
    print(f"La carpeta'{carpeta}' no existe.")
except OSError:
    print(f"La carpeta'{carpeta}' no esta vacia o no se puede eliminar.")
    