#Práctica Parcial Repka 

import random

x = 0
categorias = {
    "bajas": {"ventas": [],
              "total": x,
              "promedio": x},
    "medias": {"ventas": [],
               "total": x,
               "promedio": x},
    "altas": {"ventas": [],
              "total": x,
              "promedio": x}
}

cont = 0
while cont != 100:
    num_gen = random.randint(10,5000)
    if num_gen < 1000:
        categorias["bajas"]["ventas"].append(num_gen)
    elif num_gen >= 1000 and num_gen <= 3000:
        categorias["medias"]["ventas"].append(num_gen)
    else:
        categorias["altas"]["ventas"].append(num_gen)
    cont += 1

# Calcular el total de ventas por categoría
for i in categorias["bajas"]["ventas"]:
    categorias["bajas"]["total"] +=  i
for i in categorias["medias"]["ventas"]:
    categorias["medias"]["total"] +=  i
for i in categorias["altas"]["ventas"]:
    categorias["altas"]["total"] +=  i

# Calcular el total de ventas por categoría
categorias["bajas"]["promedio"] = categorias["bajas"]["total"] / len(categorias["bajas"]["ventas"])
categorias["medias"]["promedio"] = categorias["medias"]["total"] / len(categorias["medias"]["ventas"])
categorias["altas"]["promedio"] = categorias["altas"]["total"] / len(categorias["altas"]["ventas"])

# Impresión de cada apartado
print("\nBAJAS")
print("Ventas", categorias["bajas"]["ventas"])
print(f"Total U{'$'}S", categorias["bajas"]["total"])
print(f"Promedio U{'$'}S", categorias["bajas"]["promedio"])

print("\nMEDIAS")
print("Ventas", categorias["medias"]["ventas"])
print(f"Total U{'$'}S", categorias["medias"]["total"])
print(f"Promedio U{'$'}S", categorias["medias"]["promedio"])

print("\nALTAS")
print("Ventas", categorias["altas"]["ventas"])
print(f"Total U{'$'}S" , categorias["altas"]["total"])
print(f"Promedio U{'$'}S", categorias["altas"]["promedio"])

#Guardar en un archivo de texto
f = open(r"C:\Users\maxim\OneDrive\Desktop\UCP\Segundo Año\Paradigmas de Programación I\An-lisis-de-Ventas-de-empresa-retail\mi_fichero.txt", "w+")
f.write("altas: ")
f.write("\n\t")
f.write("ventas: ")
f.write(str(categorias["altas"]["ventas"]))
f.write("\n\t")
f.write("total: ")
f.write(str(categorias["altas"]["total"]))
f.write("\n\t")
f.write("promedio: ")
f.write(str(categorias["altas"]["promedio"]))
f.write("\n")
f.write("bajas: ")
f.write("\n\t")
f.write("ventas: ")
f.write(str(categorias["bajas"]["ventas"]))
f.write("\n\t")
f.write("total: ")
f.write(str(categorias["bajas"]["total"]))
f.write("\n\t")
f.write("promedio: ")
f.write (str(categorias["bajas"]["promedio"]))
f.write("\n\t")
f.write("medias: ")
f.write("\n\t")
f.write("ventas: ")
f.write(str(categorias["medias"]["ventas"]))
f.write("\n\t")
f.write("total: ")
f.write(str(categorias["medias"]["total"]))
f.write("\n\t")
f.write("promedio: ")
f.write (str(categorias["medias"]["promedio"]))
#f.close()"""
