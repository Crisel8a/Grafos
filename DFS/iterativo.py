def DFS(root, targetValue):
    print(f"Actualmente estoy en el nodo con valor: {root.valor}")

    if root.valor == targetValue:
        print(f"¡Encontré el valor {targetValue}!")
        return root

    for i in range(len(root.children)):
        childNode = root.children[i]
        resultNode = DFS(childNode, targetValue)

        if resultNode is not None:
            return resultNode

    return None
