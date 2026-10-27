class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def dfs(start, target):
    print("Visiting Node", start.value)

    if start.value == target:
        print("Found the node we're looking for!")
        return start

    for child in start.children:
        result = dfs(child, target)

        if result is not None:
            return result

    return None


# Crear el árbol
root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4), Node(5)]

# Buscar el nodo con valor 5
result = dfs(root, 5)

if result is not None:
    print("Resultado:", result.value)
else:
    print("Node not found")
