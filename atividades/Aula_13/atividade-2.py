matriz:list[list[str]] = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"]
]

print(matriz[0][0])
print(matriz[1][1])
print(matriz[2][2])
matriz[1][1] = "OCUPADO"
print("============================")

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna])
