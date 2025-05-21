#Práctica Parcial Repka 

import random

categorias = {
    "bajas": {"ventas": [],
              "total": [],
              "promedio": []},
    "medias": {"ventas": [],
               "total": [],
               "promedio": []},
    "altas": {"ventas": [],
              "total": [],
              "promedio": []}
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


# Calcular el total de ventas por categoría


#   Impresión de cada apartado
print("BAJAS")
print("Ventas", categorias["bajas"]["ventas"])
print("Total", categorias["bajas"]["Total"])
print("Promedio", categorias["bajas"]["ventas"])

print("MEDIAS")
print("Ventas", categorias["medias"]["ventas"])
print("Total", categorias["medias"]["Total"])
print("Promedio", categorias["medias"]["ventas"])

print("ALTAS")
print("Ventas", categorias["altas"]["ventas"])
print("Total", categorias["altas"]["Total"])
print("Promedio", categorias["altas"]["ventas"])