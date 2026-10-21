class Endereco:
    def __init__(self, rua, cidade):
        self._rua = rua
        self._cidade = cidade

    def __str__(self):
        return self.cidade + self.rua