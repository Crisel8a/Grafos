def DFSBinary(root, targetValue):
    if root is None:
        return None

    print(f"Actualmente estoy en el nodo con valor: {root.valor}")

    if root.valor == targetValue:
        print(f"¡Encontré el valor {targetValue}!")
        return root

    leftResult = DFSBinary(root.izquierda, targetValue)

    if leftResult is not None:
        return leftResult

    rightResult = DFSBinary(root.derecha, targetValue)

    if rightResult is not None:
        return rightResult

    return None
