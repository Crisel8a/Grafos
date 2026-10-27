def numIslands(maps: list[list[str]]) -> int:
    CantidadDeIslas = 0

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "1":
                dfs(i, j, maps)
                CantidadDeIslas += 1

    return CantidadDeIslas


def dfs(i, j, maps):
    # Verificar límites y si la celda es agua
    if i < 0 or i >= len(maps) or j < 0 or j >= len(maps[0]) or maps[i][j] == "0":
        return

    maps[i][j] = "0"  # Marcar como visitado

    dfs(i + 1, j, maps)  # Abajo
    dfs(i - 1, j, maps)  # Arriba
    dfs(i, j + 1, maps)  # Derecha
    dfs(i, j - 1, maps)  # Izquierda


# Ejemplo de uso
if __name__ == "__main__":
    maps = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    print(numIslands(maps))  # Output: 1
