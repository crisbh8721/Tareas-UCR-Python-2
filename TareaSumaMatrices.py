#hacer una funcion que sume matrices de cualquier tamaño
def suma_matrices_flexible(m1, m2):
    # Determinar dimensiones máximas
    filas = max(len(m1), len(m2))
    columnas = max(
        max((len(fila) for fila in m1), default=0),
        max((len(fila) for fila in m2), default=0)
    )

    resultado = []
    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            val1 = m1[i][j] if i < len(m1) and j < len(m1[i]) else 0
            val2 = m2[i][j] if i < len(m2) and j < len(m2[i]) else 0
            fila_resultado.append(val1 + val2)
        resultado.append(fila_resultado)
    return resultado