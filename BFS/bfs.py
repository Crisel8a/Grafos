# imprimir todos los valores de un arbol en el orden bfs
def BFS(root):
    if not root:
        return []
    respuesta = [root]
    cola = [root]
    nivel = 0

    while cola:
        for _ in range(len(cola)):
            nodoActual = cola.pop(0)
            print("Valor del nodo actual:", nodoActual.valor)
            respuesta.append(nodoActual)
            for hijo in nodoActual.children:
                cola.append(hijo)
        nivel += 1
    print("Niveles del arbol:", nivel)

    return respuesta


# ejemplo de uso
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.children = []


# ejemplo de uso

raiz = Nodo(1)
raiz.children = [Nodo(2), Nodo(3)]
raiz.children[0].children = [Nodo(4), Nodo(5)]

respuesta = BFS(raiz)
print("Respuesta del BFS:", [nodo.valor for nodo in respuesta])
