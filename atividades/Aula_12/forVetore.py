nomes:list[str] = []

for i in range(5):
    nome = input("Digite um nome: ")

    nomes.append(nome)

for i in range(len(nomes)):
    print(i+1, "-", nomes[i])