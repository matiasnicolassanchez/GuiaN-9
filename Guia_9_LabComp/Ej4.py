botellas_nec = int(input("Ingrese la cantidad de botellas que se necesitan reciclar para obtener una nueva: "))
botellas_reciclar = int(input("Ingrese la cantidad de botellas a reciclar: "))
nuevas = (botellas_reciclar // botellas_nec)
sobrante = (botellas_reciclar % botellas_nec)
num_reciclaje = 1
while sobrante != 0:
    nuevas = (botellas_reciclar // botellas_nec)
    sobrante = (botellas_reciclar % botellas_nec)
    print(f"Reciclaje número {num_reciclaje}: \nBotellas a reciclar:{botellas_reciclar} \nbotellas necesarias para obtener una nueva:{botellas_nec} \nsobrante de reciclaje anterior:{sobrante} \nUsted obtendra")