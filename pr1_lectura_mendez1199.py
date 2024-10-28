nombre_archivo = "practica1_Mendez_Maria_1199.txt"
try:
    with open(nombre_archivo, "r") as f:
        contenido = f.read()
        print(contenido)
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe.")
except IOError:
    print("Ocurrió un error al intentar leer el archivo.")
