def profMin(raiz):  # recursivo
    if not raiz:
        return 0
    izquierda = profMin(raiz.izquierda)
    derecha = profMin(raiz.derecha)
    if not izquierda:
        return derecha + 1
    elif not derecha:
        return izquierda + 1
    else:
        return min(izquierda, derecha) + 1
