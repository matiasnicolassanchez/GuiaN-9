botellas_nec = int(input("Ingrese la cantidad de botellas que se necesitan para obtener una nueva: "))
botellas_reciclar = int(input("Ingrese la cantidad de botellas a reciclar: "))
sobrante = (botellas_reciclar % botellas_nec)
sobran = 0
reciclaje = 1
while sobrante != 0:
    nuevas = ((botellas_reciclar) // botellas_nec)
    sobran = (botellas_reciclar % botellas_nec)
    sobrante = sobran
    botellas_reciclar = (nuevas + sobran)
    print(f"{reciclaje} reciclaje: Con {botellas_reciclar} botellas a reciclar --> Se fabrican {nuevas} botellas y sobran {sobran} botellas ")
    reciclaje = (reciclaje + 1)
