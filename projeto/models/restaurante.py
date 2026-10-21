from models.avaliacao import Avaliacao
from models.cardapio.itemCardapio import ItemCardapio
from models.endereco.endereco import Endereco


class Restaurante:
    restaurantes = []  # lista de todas as instâncias

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        self._endereco = []
        Restaurante.restaurantes.append(self)

    @property
    def ativo(self):
        return "[x]" if self._ativo else "[]"

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_Avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    def adicionar_item_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
        else:
            print(f"Não foi possivel adicionar {item}: não é um item de cardápio")

    def adicionar_endereco(self, endereco):
        if isinstance(endereco, Endereco):
            self._endereco.append(endereco)
        else:
            print(f'Não foi possível adicionar "{endereco}": não é um endereço.')
    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        soma = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        media = soma / len(self._avaliacoes)
        return round(media, 1)

    @property
    def exibir_cardapio(self):
        print(f"Cradapio de {self.nome}")
        for indice, item in enumerate(self._cardapio, start=1):
            linha = f"{indice}. {item._nome} - R$ {item._preco:.2f}"
            if hasattr(item, "_descricao"):
                linha += f" | Descrição: {item._descricao}"
            if hasattr(item, "_tamanho"):
                linha += f" | Tamanho: {item._tamanho}"
            if hasattr(item, "_sabor"):
                linha += f" | Descrição: {item._sabor}"
            print(linha)

    def resumo(self):
        print(f"Nome do restaurante: {self.nome}")
        print(f"Quantidade de itens no cardapio: {len(self._cardapio)}")
        print(f"Endereços cadastrados: {len(self._endereco)}")

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(
                restaurante.nome.ljust(20)
                + restaurante.categoria.ljust(15)
                + restaurante.ativo.ljust(5)
                + str(restaurante.media_avaliacoes).ljust(5)
            )

    def __str__(self):
        return f"{self.nome} | {self.categoria}"
