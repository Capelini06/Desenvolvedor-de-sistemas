opcao = int(input("Insira uma opção(1 a 3): "))

match opcao:
    case 1:
        print("Cadastro")
    case 2:
        print("Consulta")
    case 3:
        print("Sair")
    case _:
        print("Opção invalida")