cidades = []

for i in range(5):
    cidade = input("Insira o nome de uma cidade: ")

    cidades.append(cidade)

for i in range(len(cidades)):
    print(1+i, " - ", cidades[i])