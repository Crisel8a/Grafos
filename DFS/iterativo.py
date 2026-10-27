def dfs(node, graph_adj, visited):
    stack = [node]

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            print("Visiting Node", node)

            for j in range(len(graph_adj[node])):
                if graph_adj[node][j] == 1:
                    stack.append(j)


# Ejemplo de uso
graph_adj = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]

visited = [False] * len(graph_adj)

dfs(0, graph_adj, visited)
