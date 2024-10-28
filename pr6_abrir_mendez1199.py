# Abrir archivo
f = open("practica6_mendez_maria_1199.txt", "w", encoding='utf-8')
f.write("Mendez Sanchez Maria Guadalupe Yazmin va a la escuela todos los días")
f.close()

f = open("practica6_mendez_maria_1199.txt", "r", encoding='utf-8')
print(f.read())
f.close()
