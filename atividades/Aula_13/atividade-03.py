numeros:list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in range(len(numeros)):
    for coluna in range(len(numeros[linha])):
        print(numeros[linha][coluna])