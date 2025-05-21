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


#   Impresión de cada apartado
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