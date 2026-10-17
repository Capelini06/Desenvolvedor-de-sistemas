itens:list[str] = ["Espada", "Escudo", "Poção", "Mapa"]

print("Inventario: ", itens)

itens.append("Arco")

itens.pop()

itens[2] = "Poção Grande"

print("Inventario atualizado: ", itens)

print(len(itens))