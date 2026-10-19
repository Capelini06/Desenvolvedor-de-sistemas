nomes = ["Ana", "Bruna", "Carlos", "Denise", "Eduarso"]
achou = False

pesquisa = input("Insira um nome para pesquisar: ")

for i in range(len(nomes)):
    if (pesquisa == nomes[i]):
        posicao = i
        achou = True
        break

if(achou):
    print("Nome encontrado no índice ", posicao)
else:
    print("Nome não encontrado")