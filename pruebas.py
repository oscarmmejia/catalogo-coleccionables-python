try:
    precio_minimo = float(input("Ingrese el precio mínimo: "))
except ValueError:
    print("El precio debe ser un valor numérico")