entrada = input("Recuerde ingresar \"salir\" para salir del eco.\nIngrese lo que desee al eco: ")
salida = str
while entrada != "salir":
    salida = entrada
    print(f"{salida}")
    entrada = input("Recuerde ingresar \"salir\" para salir del eco.\nIngrese lo que desee al eco: ")
if entrada == "salir":
    print("Usted a salido del eco".upper())
