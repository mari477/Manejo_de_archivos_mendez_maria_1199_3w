import os
nombre_archivo = "practica7_mendez_maria_1199.txt"

if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)
    print(" ")
    print(f"El archivo '{nombre_archivo}'ha sido eliminado.")
    print(" ")
else:
    print(f"El archivo '{nombre_archivo}'no existe.")
