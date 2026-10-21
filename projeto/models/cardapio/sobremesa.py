from models.cardapio.itemCardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, sabor):
        super().__init__(nome, preco)
        self._sabor = sabor