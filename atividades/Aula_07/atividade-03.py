valor = float(input("Insira o valor da compra: "))

if(valor >= 1000):
    desconto = 20
    print("Desconto de ", desconto ,"% recebido")
elif(valor >= 500):
    desconto = 10
    print("Desconto de ", desconto ,"% recebido")
else:
    desconto = 0
    print("Nenhum desconto recebido")