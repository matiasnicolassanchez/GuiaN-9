contrasenia_guardada = input("Ingrese la contraseña que desea guardar: ")
contrasenia_acceso = input("Ingrese la contraseña de acceso: ")

while contrasenia_acceso != contrasenia_guardada:
    print("Su contraseña es incorrecta")
    contrasenia_acceso = input("Ingrese la contraseña de acceso: ")

if contrasenia_acceso == contrasenia_guardada:
    print("Su contraseña es correcta")
