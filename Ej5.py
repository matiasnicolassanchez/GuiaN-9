nisbn = input("Ingrese el numero ISBN del libro\"SOLO LA PARTE NUMERICA\": ")
cant_suma = 1
sum_productos = 0
multiplicador = 1
producto = 0
ubicacion = 0
while ubicacion < 9:
    producto = (int(nisbn.index("ubicacion")) * multiplicador)
    sum_productos = (sum_productos + producto)
    ubicacion = (ubicacion + 1)
    multiplicador = (multiplicador + 1)

print(producto)
