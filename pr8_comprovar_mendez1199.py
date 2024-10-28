import os
archivo = "practica8_mendez_maria_1199.txt"

if os.path.exists(archivo):
    os.remove(archivo)
    print(f"{archivo} ha sido eliminado.")
else:
    print(f"{archivo} no existe.")

