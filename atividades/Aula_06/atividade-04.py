saldo = float(input("Insira o seu saldo: "))
saque = float(input("Insira o quanto voce quer sacar: "))

if (saque <= saldo):
    print("Saque autorizado")
    print("Saldo restante: ", (saldo - saque))
else: 
    print("Saque recusado. Saldo insuficiente.")