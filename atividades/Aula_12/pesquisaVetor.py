nomes:list[str] = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]

posicao = -1

pesquisa = input("Insira um nome para pesquisa: ")

for i in range(len(nomes)):
    if(nomes[i] == pesquisa):
        posicao = i
        print("Posição: ", posicao)
        break
