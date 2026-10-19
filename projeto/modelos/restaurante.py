from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []  # lista de todas as instâncias

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    @property
    def ativo(self):
        return "[x]" if self._ativo else "[]"

    def alternar_estado(self):
        self._ativo = not self._ativo

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

