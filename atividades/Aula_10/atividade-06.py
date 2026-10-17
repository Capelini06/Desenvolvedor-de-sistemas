alunos = (int(input("Quantos alunos tem na sala:")))
presentes = 0
ausentes = 0
contador = 1

for i in range(1, alunos+1):
    print("O aluno", i, " esta presente?")
    presenca = input("(S-sim/ N-não): ")
    if (presenca == "s" or presenca == "S"):
        presentes+=1
    else:
        ausentes+=1
print("Alunos presentes: ", presentes)
print("Alunos ausentes: ", ausentes)