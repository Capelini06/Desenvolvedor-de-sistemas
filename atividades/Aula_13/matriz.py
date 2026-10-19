matriz: list[list[int]] = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna])

print(matriz[0])
print(matriz[1])
print(matriz[2])

soma = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        soma += matriz[linha][coluna]
print("SOMA: ", soma)