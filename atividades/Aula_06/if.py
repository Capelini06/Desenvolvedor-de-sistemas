idade = int(input("Insira sua idade: "))

if (idade >= 18):
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

print ("==============================================")
possuiIngresso = True

if (idade >= 18 and possuiIngresso):
    print("Entrada permitida")
else: 
    print("Entrada negada")
