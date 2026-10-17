produto1 = input("Insira um primeiro produto: ")
produto2 = input("Insira um segundo produto: ")
produto3 = input("Insira um terceiro produto: ")

produtos = []

produtos.append(produto1)
produtos.append(produto2)
produtos.append(produto3)

print("=====LISTA DE COMPRAS=====")
print("Produtos: ", produtos)
print("Quantidade de produtos: ", len(produtos))
print("Primeiro produto: ", produtos[1])
print("Ultimo produto: ", produtos[2])