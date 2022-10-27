num = int(input("Infrese el numero isbn(10digitos)\n"))
d1 = (num // 1) % 10
d2 = (num // 10) % 10
d3 = (num // 100) % 10
d4 = (num // 1000) % 10
d5 = (num // 10000) % 10
d6 = (num // 100000) % 10
d7 = (num // 1000000) % 10
d8 = (num // 10000000) % 10
d9 = (num // 100000000) % 10
d10 = (num // 1000000000) % 10

print(f"{d1}")