# matriz mxn, con valores
# 0 = vacio, 1 = naranja fresca, 2 = naranja podrida
# cada minuto, las naranjas frescas adyacentes a una naranja podrida se pudren
# devolver el numero minimo de dias que deben pasar para que todas las naranjas frescas esten podridas
# si es imposible, retornamos -1
# se pudre si alguno de sus vecinos (arriba, abajo, izquierda, derecha) esta podrido
# tardan en pudrirse 1 dia
# lo haremos con BFS, porque es un problema de propagacion de niveles
# O(n*m) tiempo y espacio, donde n es el numero de filas y m es el numero de columnas
def rottingOranges(matriz):
    if not matriz:
        return -1

    filas = len(matriz)
    columnas = len(matriz[0])
    cola = []
    naranjas_frescas = 0

    # Agregar todas las naranjas podridas a la cola y contar las naranjas frescas
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 2:
                cola.append((i, j))
            elif matriz[i][j] == 1:
                naranjas_frescas += 1

    # Si no hay naranjas frescas, no necesitamos esperar
    if naranjas_frescas == 0:
        return 0

    dias = 0
    direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while cola:
        dias += 1
        for _ in range(len(cola)):
            x, y = cola.pop(0)
            for dx, dy in direcciones:
                nuevo_x, nuevo_y = x + dx, y + dy
                if (
                    0 <= nuevo_x < filas
                    and 0 <= nuevo_y < columnas
                    and matriz[nuevo_x][nuevo_y] == 1
                ):
                    matriz[nuevo_x][nuevo_y] = 2
                    naranjas_frescas -= 1
                    cola.append((nuevo_x, nuevo_y))

    # Si todavía hay naranjas frescas, significa que no todas se pudrieron
    return dias - 1 if naranjas_frescas == 0 else -1


# ejemplo de uso
if __name__ == "__main__":
    matriz = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    print(rottingOranges(matriz))  # Salida: 4
    matriz2 = [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1],
    ]
    print(rottingOranges(matriz2))  # Salida: -1
