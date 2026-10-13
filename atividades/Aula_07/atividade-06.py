peso = float(input("Insira o seu peso: "))
altura = float(input("Insira a sua altura: "))

imc = peso/(altura**2)

if (imc >= 30):
    print("Obesidade")
elif(imc>=25 and imc<= 29.9):
    print("Sobrepeso")
elif(imc>=18.5 and imc <= 24.9):
    print("Peso ideal")
else:
    print("Abaixo do peso")