metros = float(input("Insira um tamanho em metros: "))
conversao = int(input("Insira a conversão(1 - centimetros/ 2 - Quilômetros/ 3 - Milimetros): "
))

match conversao:
    case 1:
        print("Centimetros: ", (metros * 100))
    case 2:
        print("Quilômetros: ", (metros / 1000))
    case 3:
        print("Milimetros: ", (metros * 1000))
    case _:
        print("Operação invalida.")