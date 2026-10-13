nome = input("Nome do funcionario: ")
salarioBase = float(input("Insira o salario base: "))
horasExtras = float(input("Insira o valor de horas extras: "))
valorDesconto = float(input("Insira o valor de desconto: "))

salarioFinal = salarioBase + horasExtras - valorDesconto

print("Salario final: ", salarioFinal)