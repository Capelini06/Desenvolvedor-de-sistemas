nota:list[list[float]] = [
    [10, 6.7, 5.5],
    [9.5, 10, 3],
    [6.7, 7.5, 0]
]

for linha in range(len(nota)):
    for coluna in range(len(nota[linha])):
        print("ALUNO:", nota[linha][coluna])