nome = input("Insira o nome do aluno: ")
prova1 = float(input("Insira a primeira nota: "))
prova2 = float(input("Insira a segunda nota: "))
trabalho = float(input("Insira a nota de trabalho: "))

mediaFinal = ((prova1*3) + (prova2*4) + (trabalho*3))/10

print ("Media final", mediaFinal)