valor = float(input("Insira o valor da compra: "))

if(valor >= 200):
    print("Desconto de 10% recebido")
    desconto = 10
else:
    desconto = 0

valorDesconto = valor * (desconto/100)

valorFinal = valor - valorDesconto

print("Valor de desconto: ", valorDesconto)
print("Valor de compra final: ", valorFinal)