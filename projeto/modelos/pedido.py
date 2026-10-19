class Pedido:
    def __init__(self, restaurante, itens):
        self.restaurante = restaurante
        self.itens = itens

    def calcular_total(self):
        return sum(item.preco for item in self.itens)

    def __str__(self):
        linhas = [f"Pedido em: {self.restaurante}"]
        for item in self.itens:
            linhas.append(f" - {item}")
        linhas.append(f"Total: R$ {self.calcular_total():.2f}")
        return '\n'.join(linhas)