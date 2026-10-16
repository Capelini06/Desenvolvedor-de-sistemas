numero = int(input("Insira um numero para ver a sua tabuada: "))

for i in range(1, 11):
    mult = numero * i
    print(numero," * ", i, " = ", mult)