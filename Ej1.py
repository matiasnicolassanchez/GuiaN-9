altura = int(input("Ingrese un numero entero: "))
n = 1
z = "*"

for n in range(1, altura + 1):
    print(f"{z * n}")
    n = (n + 1)
