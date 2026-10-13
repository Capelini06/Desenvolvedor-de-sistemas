nome = input("Nome do motorista: ")
distancia = float(input("Distância: "))
consumo = float(input("Consumo medio de gasolina por km: "))
precoCombustivel = float(input("Preço do litro do combustivel: "))

litrosUtilizados = distancia / consumo

custoTotal = litrosUtilizados * precoCombustivel

print("Valor gasto: ", custoTotal)