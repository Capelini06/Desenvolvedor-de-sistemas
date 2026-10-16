soma = 0
contador = 0

while (True):
    nota = (int(input("Insira a nota(insira um valor maior que 10 para terminar): ")))

    if(nota > 10):
        break
    else:
        soma = soma + nota
        contador +=1

media = soma / contador

print("Media: ", media)