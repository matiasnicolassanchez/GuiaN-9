numero = int(input("Ingrese un numero - Ingrese \"-1\" si desea terminar: "))
num1 = 0
num2 = 0
num3 = 0
num4 = 0
suma = 0
par = 0

while numero != (-1):
    num1 = (numero // 10) % 10
    num2 = (numero // 1) % 10
    num3 = (numero // 100) % 10
    num4 = (numero // 1000) % 10
    suma = (num1 + num2 + num3 + num4)
    if (numero % 2) == 0:
        par = (par + 1)
    print(f"{suma}")
    numero = int(input("Ingrese un numero - Ingrese \"-1\" si desea terminar"))

print(f"Usted ingreso {par} números pares")
