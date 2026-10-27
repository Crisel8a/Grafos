# Sum Root To Leaf Numbers
# tenemos la ra[iz de unarbol ninario q tiene digitos del 0 al 9, dame la suma de todos
# los numeros q se forman desde la raiz hasta las hojas. Por ejemplo, si el arbol es
#     1
#    / \
#   2   3
#  / \   \
# 4   5   6
# La suma sería: 124 + 125 + 136 = 375
def sumRootToLeaf(raiz):  # recursivo

    def dfs(nodo, numero_actual):
        if not nodo:
            return 0

        numero_actual = numero_actual * 10 + nodo.valor

        if not nodo.izquierda and not nodo.derecha:  # si es hoja
            return numero_actual

        return dfs(nodo.izquierda, numero_actual) + dfs(nodo.derecha, numero_actual)

    return dfs(raiz, 0)


# ejemplo de uso
class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha


raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
raiz.derecha.derecha = Nodo(6)

print(sumRootToLeaf(raiz))  # Salida: 375
