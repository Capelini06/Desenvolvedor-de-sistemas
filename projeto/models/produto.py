from models.avaliacao import Avaliacao

class Produto:
    produtos = []

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self._disponivel = False
        self._avaliacoes = []
        Produto.produtos.append(self)

    def alterar_disponibilidade(self):
        self._disponivel = not self._disponivel

    def receber_Avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        soma = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        media = soma / len(self._avaliacoes)
        return round(media, 1)

    @classmethod
    def listar_produtos(cls):
        for produto in cls.produtos:
            print(f"Produto: {produto.nome} | Preço: R$ {produto.preco:.2f}")

    @property
    def disponivel(self):
        return "Disponível" if self._disponivel else "Indisponível"

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"