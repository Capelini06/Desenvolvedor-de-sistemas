from models.restaurante import Restaurante
from models.produto import Produto
from models.pedido import Pedido
from models.avaliacao import Avaliacao

restaurante_01 = Restaurante("Madá Pizzaria", "Italiana")
restaurante_02 = Restaurante("Vinigucci Pizzaria", "Italiana")

Restaurante.adicionar_item_cardapio()

produto3.aplicar_desconto(10)

Restaurante.listar_restaurantes()
print()
Produto.listar_produtos()
print()

pedido = Pedido(restaurante_01, [produto1, produto2])
print(pedido)

print("===============================")
# vars(objeto) devolve o __dict__ do objeto: um dicionário só com os
# atributos de INSTÂNCIA, ou seja, o que foi criado com self.algo no __init__.
# Para o pedido, isso é {'restaurante': ..., 'itens': [...]}.
# Métodos (calcular_total, __str__) NÃO aparecem, pois pertencem à classe.
# Como é um dicionário, .items() permite pegar nome e valor de cada atributo.

print("Atributos de instancia (vars):")
for nome, valor in vars(pedido).items():
    print(f"{nome}: {valor}")



# dir(objeto) devolve uma LISTA com os NOMES de tudo que o objeto consegue
# acessar: atributos de instância + métodos da classe + métodos herdados de
# object (__init__, __str__, __eq__, __class__...). Só nomes, sem valores.
# Por isso é preciso filtrar:
#   - not nome.startswith("__")       -> remove os métodos especiais (dunder)
#   - not callable(getattr(...))      -> getattr busca o valor pelo nome e
#                                        callable verifica se é função/método;
#                                        assim sobram só os atributos de dados.

print("Atributos filtrados de dir()):")
for nome in dir(pedido):
    if not nome.startswith("__") and not callable(getattr(pedido, nome)):
        print(f"{nome}")