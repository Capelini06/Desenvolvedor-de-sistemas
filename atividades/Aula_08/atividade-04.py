numero1 = float(input("Insira um numero: "))
numero2 = float(input("Insira um numero: "))
operacao = input("Insira uma operação (+,-,*,/): ")

match operacao:
    case "+":
        resultado = numero1 + numero2
        print(numero1, " + ", numero2, " = ", resultado)
    case "-":
            resultado = numero1 - numero2
            print(numero1, " - ", numero2, " = ", resultado)
    case "*":
            resultado = numero1 * numero2
            print(numero1, " * ", numero2, " = ", resultado)
    case "/":
            resultado = numero1 / numero2
            print(numero1, " / ", numero2, " = ", resultado)
    case _:
            print("Operação invalida")