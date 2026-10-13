saldo = float(input("Insira o saldo: "))
saque = float(input("Qual sawue voce quer fazer: "))

if (saque > saldo):
    print("Saldo insuficiente")
else:
    print("Saque autorizado")