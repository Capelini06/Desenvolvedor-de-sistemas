from models.endereco.endereco import Endereco

class EnderecoCobranca(Endereco):
    def __init__(self, rua, cidade, cnpjaCobranca):
        super().__init__(rua, cidade)
        self._cnpjaCobranca = cnpjaCobranca