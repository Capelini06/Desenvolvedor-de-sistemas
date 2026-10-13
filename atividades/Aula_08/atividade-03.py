opcao = int(input("Insira um opçaõ de 1 a 5: "))

match opcao:
    case 1:
        print("Saldo")
    case 2:
        print("Saque")
    case 3:
        print("Depósito")
    case 4:
        print("PIX")
    case _:
        print("Opção invalida")