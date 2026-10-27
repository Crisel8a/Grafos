# tablero de ajedrezinfinito con un caballo en una coordenada y se mueve normal
# numero min de pasos para llegar a otra coordenada target, siempre es posible
def minKnightMoves(origenx, origeny, targetx, targety):
    direcciones = [
        [2, 1],
        [2, -1],
        [-2, 1],
        [-2, -1],
        [1, 2],
        [1, -2],
        [-1, 2],
        [-1, -2],
    ]
    visitados = set()  # O(1)
    saltos = 0
    cola = []
    cola.append((origenx, origeny))
    while cola:
        for _ in range(len(cola)):
            x, y = cola.pop(0)
            if (x, y) == (targetx, targety):
                return saltos
            for dx, dy in direcciones:
                nuevo_x, nuevo_y = x + dx, y + dy
                if (nuevo_x, nuevo_y) not in visitados:
                    visitados.add((nuevo_x, nuevo_y))
                    cola.append((nuevo_x, nuevo_y))
        saltos += 1

    return saltos

    # ejemplo de uso
    print(minKnightMoves(0, 0, 2, 1))  # Salida: 1
    print(minKnightMoves(0, 0, 5, 5))  # Salida: 4
