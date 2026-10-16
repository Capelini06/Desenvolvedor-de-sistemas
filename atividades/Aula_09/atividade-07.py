preco = 0
qta = 0
while (True):
    opc = int(input("Você quer pedir um pastel(1 - SIM/ 2 - NÂO): "))

    if(opc == 1):
        print("1)Pastel de queijo: R$15,00")
        print("2)Pastel de carne: R$25,00")
        print("3)Pastel de pizza: R$28,00")
        pizza = int(input("Insira o seu pedido: "))

        match pizza:
            case 1:
                preco = preco + 15
                qta+=1
            case 2:
                preco = preco + 25
                qta+=1
            case 3:
                preco = preco + 28
                qta+=1
            case _:
                print("Opção invalida tente novamente")
    elif(opc == 2):
        break
    else:
        print("Opção inválida")

print("Vode pediu: ", qta, "pastéis")
print("Valor total: R$", preco)

