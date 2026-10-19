matriz = [
    [5, 10, 15],
    [20, 25, 30]
]
cont = 0
soma = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        cont+=1
        soma+=matriz[linha][coluna]

media = soma/cont

print("SOMA: ", soma)
print("QUANTIDADE: ", cont)
print("MEDIA: ", media)