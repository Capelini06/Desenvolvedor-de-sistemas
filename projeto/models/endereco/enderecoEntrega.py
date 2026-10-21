from models.endereco.endereco import Endereco

class EnderecoEntrega(Endereco):
    def __init__(self, rua, cidade, intrucoesEntrega):
        super().__init__(rua, cidade)
        self._intrucoesEntrega = intrucoesEntrega