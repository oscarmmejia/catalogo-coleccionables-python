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

id_cinco = input("Ingrese el identificador de la pieza: ")
name_cinco = input("Ingrese el nombre de la pieza: ")
category_cinco = input("Ingrese la categoria de la pieza: ")
price_cinco = float(input("Ingrese el precio de la pieza: "))
status_cinco = input("Ingrese el estado de la pieza: ")
description_cinco = input("Ingrese la descripción de la pieza: ")

pieza_cinco = {
    "id": id_cinco,
    "name": name_cinco,
    "category": category_cinco,
    "price": price_cinco,
    "status": status_cinco,
    "description": description_cinco
}

print(pieza_cinco)

catalog.append(pieza_cinco)

id_seis = input("Ingrese el identificador de la pieza: ")
name_seis = input("Ingrese el nombre de la pieza: ")
category_seis = input("Ingrese la categoria de la pieza: ")
price_seis = float(input("Ingrese el precio de la pieza: "))
status_seis = input("Ingrese el estado de la pieza: ")
description_seis = input("Ingrese la descripción de la pieza: ")

pieza_seis = {
    "id": id_seis,
    "name": name_seis,
    "category": category_seis,
    "price": price_seis,
    "status": status_seis,
    "description": description_seis
}

print(pieza_seis)

catalog.append(pieza_seis)

id_siete = input("Ingrese el identificador de la pieza: ")
name_siete = input("Ingrese el nombre de la pieza: ")
category_siete = input("Ingrese la categoria de la pieza: ")
price_siete = float(input("Ingrese el precio de la pieza: "))
status_siete = input("Ingrese el estado de la pieza: ")
description_siete = input("Ingrese la descripción de la pieza: ")

pieza_siete = {
    "id": id_siete,
    "name": name_siete,
    "category": category_siete,
    "price": price_siete,
    "status": status_siete,
    "description": description_siete
}

print(pieza_siete)

catalog.append(pieza_siete)

id_ocho = input("Ingrese el identificador de la pieza: ")
name_ocho = input("Ingrese el nombre de la pieza: ")
category_ocho = input("Ingrese la categoria de la pieza: ")
price_ocho = float(input("Ingrese el precio de la pieza: "))
status_ocho = input("Ingrese el estado de la pieza: ")
description_ocho = input("Ingrese la descripción de la pieza: ")

pieza_ocho = {
    "id": id_ocho,
    "name": name_ocho,
    "category": category_ocho,
    "price": price_ocho,
    "status": status_ocho,
    "description": description_ocho
}

print(pieza_ocho)

catalog.append(pieza_ocho)

id_nueve = input("Ingrese el identificador de la pieza: ")
name_nueve = input("Ingrese el nombre de la pieza: ")
category_nueve = input("Ingrese la categoria de la pieza: ")
price_nueve = float(input("Ingrese el precio de la pieza: "))
status_nueve = input("Ingrese el estado de la pieza: ")
description_nueve = input("Ingrese la descripción de la pieza: ")

pieza_nueve = {
    "id": id_nueve,
    "name": name_nueve,
    "category": category_nueve,
    "price": price_nueve,
    "status": status_nueve,
    "description": description_nueve
}

print(pieza_nueve)

catalog.append(pieza_nueve)

id_diez = input("Ingrese el identificador de la pieza: ")
name_diez = input("Ingrese el nombre de la pieza: ")
category_diez = input("Ingrese la categoria de la pieza: ")
price_diez = float(input("Ingrese el precio de la pieza: "))
status_diez = input("Ingrese el estado de la pieza: ")
description_diez = input("Ingrese la descripción de la pieza: ")

pieza_diez = {
    "id": id_diez,
    "name": name_diez,
    "category": category_diez,
    "price": price_diez,
    "status": status_diez,
    "description": description_diez
}

print(pieza_diez)

catalog.append(pieza_diez)

print(catalog)

print(len(catalog))

categorias = set()

categorias.add(pieza_uno["category"])
categorias.add(pieza_dos["category"])
categorias.add(pieza_tres["category"])
categorias.add(pieza_cuatro["category"])
categorias.add(pieza_cinco["category"])
categorias.add(pieza_seis["category"])
categorias.add(pieza_siete["category"])
categorias.add(pieza_ocho["category"])
categorias.add(pieza_nueve["category"])
categorias.add(pieza_diez["category"])

print(categorias)
print(len(categorias))

for pieza in catalog: #manera sencilla general de ver todas las piezas del catalogo en una lista de listas
    print(pieza)

for pieza in catalog: #manera especifica de ver por cada campo de cada diccionario y con f" o template string
    print(f"ID : {pieza['id']}")
    print(f"Nombre : {pieza['name']}")
    print(f"Categoria : {pieza['category']}")
    print(f"Precio : {pieza['price']}")
    print(f"Estado : {pieza['status']}")
    print(f"Descripcion : {pieza['description']}")

print("INFORMACION GENERAL DEL CATALOGO: ")
print(f"Cantidad total de piezas: {len(catalog)}")
print(f"Cantidad de categorias: {len(categorias)}")
print(f"Categorias Unicas: {categorias}")