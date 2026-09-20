print("Catalogo de Coleccionables")
print("Bienvenidos al Catalogo de Coleccionables Digitech")

catalog = []

id = input("Ingrese el identificador de la pieza: ")
name = input("Ingrese el nombre de la pieza: ")
category = input ("Ingrese la categoria de la pieza: ")
price = float(input("Ingrese el precio de la pieza: "))
status = input("Ingrese el estado de la pieza: ")
description = input("Ingrese la descripcion de la pieza: ")

pieza_uno = {
    "id": id,
    "name": name,
    "category": category,
    "price": price,
    "status": status,
    "description": description
}

print(pieza_uno)

catalog.append(pieza_uno)

id_dos = input("Ingrese el identificador de la pieza: ")
name_dos = input("Ingrese el nombre de la pieza: ")
category_dos = input("Ingrese la categoría de la pieza: ")
price_dos = float(input("Ingrese el precio de la pieza: "))
status_dos = input("Ingrese el estado de la pieza: ")
description_dos = input("Ingrese la descripción de la pieza: ")

pieza_dos = {
    "id": id_dos,
    "name": name_dos,
    "category": category_dos,
    "price": price_dos,
    "status": status_dos,
    "description": description_dos
}

print(pieza_dos)

catalog.append(pieza_dos)

id_tres = input("Ingrese el identificador de la pieza: ")
name_tres = input("Ingrese el nombre de la pieza: ")
category_tres = input("Ingrese la categoria de la pieza: ")
price_tres = float(input("Ingrese el precio de la pieza: "))
status_tres = input("Ingrese el estado de la pieza: ")
description_tres = input("Ingrese la descripción de la pieza: ")

pieza_tres = {
    "id": id_tres,
    "name": name_tres,
    "category": category_tres,
    "price": price_tres,
    "status": status_tres,
    "description": description_tres
}

print(pieza_tres)

catalog.append(pieza_tres)

id_cuatro = input("Ingrese el identificador de la pieza: ")
name_cuatro = input("Ingrese el nombre de la pieza: ")
category_cuatro = input("Ingrese la categoria de la pieza: ")
price_cuatro = float(input("Ingrese el precio de la pieza: "))
status_cuatro = input("Ingrese el estado de la pieza: ")
description_cuatro = input("Ingrese la descripción de la pieza: ")

pieza_cuatro = {
    "id": id_cuatro,
    "name": name_cuatro,
    "category": category_cuatro,
    "price": price_cuatro,
    "status": status_cuatro,
    "description": description_cuatro
}

print(pieza_cuatro)

catalog.append(pieza_cuatro)

print(catalog)

print(len(catalog))