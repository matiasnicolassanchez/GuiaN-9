import time
def formatcero(p):              # funcion
    c1 = str(p)
    if p < 10:
        c1 = "0" + str(p)
    return c1

seg = 0
minutos = 0
horas = 0

while seg < 60:
    print(f"{horas}:{minutos}:{seg}")
    seg += 1
    # print(f"segundos:{seg}")
    if seg == 60:
        minutos = minutos + 1
        # print(f"{minutos}:{seg}")
        seg = 0
        if minutos == 60:
            horas += 1
            minutos = 0
            # print(f"horas:{horas}")
            if horas == 24:
                print("completo")
                seg = 0
                minutos = 0
                horas = 0
                break

for horas in range(0, 24):
    for minutos in range(0, 60):
        for seg in range(0, 60):
            time.sleep(1)           #El programa espera 1 segundo
            print(formatcero(horas),":",formatcero(minutos),":",formatcero(seg))