# Abrir el archivo y agregar contenido
with open("practica5_mendez_maria_1199.txt", "a") as f:
    f.write("Ahora el archivo tiene más contenido\n")

# Leer el contenido del archivo
with open("practica5_mendez_maria_1199.txt", "r") as f:
    print(f.read())

    