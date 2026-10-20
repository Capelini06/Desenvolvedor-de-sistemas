from models.cardapio.itemCardapio import ItemCardapio

class Bebidas(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho