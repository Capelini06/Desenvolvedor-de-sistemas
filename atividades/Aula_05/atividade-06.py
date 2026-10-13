nome = input("Nome do vendedor: ")
salarioFixo = float(input("Salario fisico: "))
valorVendido = float(input("Valor total vendido no mês: "))
percentualComissao = float(input("Percentual de comissão:"))

comissao = valorVendido * (percentualComissao/100)

salarioFinal = salarioFixo + comissao

print("Salario final: ", salarioFinal)