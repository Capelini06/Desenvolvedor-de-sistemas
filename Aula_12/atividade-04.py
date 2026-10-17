notas = [5, 4, 3, 7, 9, 10]
aprovados = 0
reprovados = 0

for i in range(len(notas)):
    if(notas[i] >= 6):
        aprovados+=1
    else:
        reprovados+=1

print("Aprovados: ", aprovados)
print("Reprovados: ", reprovados)