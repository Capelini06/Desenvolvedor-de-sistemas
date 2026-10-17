nomes:list[str] = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]

notas:list[int] = [8, 9, 7, 3]

concluidos:list[bool] = [True, False, False, True]

for i in nomes:
    print(i)
print("Quantidade de itens: ", len(nomes))

print("====================================")

for i in notas:
    print(i)
print("Quantidade de itens: ", len(notas))

print("====================================")

for i in concluidos:
    print(i)
print("Quantidade de itens: ", len(concluidos))