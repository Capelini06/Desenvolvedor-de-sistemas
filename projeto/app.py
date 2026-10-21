from models.restaurante import Restaurante
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebidas
from models.cardapio.sobremesa import Sobremesa
from models.endereco.enderecoEntrega import EnderecoEntrega
from models.endereco.enderecoCobranca import EnderecoCobranca

restaurante_mada = Restaurante("Madá Pizzaria", "Italiana")

pratoPizza01 = Prato("Pizza 4 queijos", 40.50, "Uma pizza com 4 tipos de queijo")
bebidaSuco = Bebidas("Suco de uva", 10.50, "grande")
sobremesaPudim = Sobremesa("Pudim de leite", 24.99, "leite condensado")

restaurante_mada.adicionar_item_cardapio(pratoPizza01)
restaurante_mada.adicionar_item_cardapio(bebidaSuco)
restaurante_mada.adicionar_item_cardapio(sobremesaPudim)
restaurante_mada.adicionar_item_cardapio("Comida")

entrega = EnderecoEntrega("Rua rio de janeiro - 348", "São josé dos pinhais", "Apartamento 403")
cobranca = EnderecoCobranca("Rua josé mauricio higgins", "Curitiba", "12.345.678/0001-90")

restaurante_mada.adicionar_endereco(entrega)
restaurante_mada.adicionar_endereco(cobranca)

def main():
    print()
    restaurante_mada.exibir_cardapio
    print()
    restaurante_mada.resumo()

if __name__ == "__main__":
    main()

