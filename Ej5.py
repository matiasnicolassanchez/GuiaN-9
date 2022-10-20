nisbn = input("Ingrese el numero ISBN del libro\"SOLO LA PARTE NUMERICA\": ")
digito_verificador = nisbn[9]
# print(f"{digito_verificador}")
digito = 0
n = 0
producto = 0
sumatoria = 0
verificador = 0
for n in range(0, 9):
    digito = int(nisbn[n])
    producto = (digito * (n+1))
    sumatoria = (sumatoria + producto)
    # print(f"{sumatoria}")

verificador = (sumatoria % 11)
# print(f"{verificador}")
if verificador == int(digito_verificador):
    print(f"El número ISBN \"{nisbn}\" esta escrito correctamente")

else:
    print(f"El número ISBN \"{nisbn}\" esta escrito incorrectamente")
