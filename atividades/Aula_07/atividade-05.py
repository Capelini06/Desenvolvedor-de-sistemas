velocidade = float(input("Insira a velocidade em Km: "))

if(velocidade > 80):
    print("Multado")
elif(velocidade >= 61 and velocidade < 80):
    print("Atenção")
else:
    print("Velocidade dentro do permitido")