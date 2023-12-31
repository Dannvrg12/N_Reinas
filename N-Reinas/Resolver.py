def resolver_n_reinas_util(tablero, fila, n):
    if fila == n:
        return [list(tablero)]

    soluciones = []
    for columna in range(n):
        if es_seguro(tablero, fila, columna):
            tablero[fila] = columna
            soluciones.extend(resolver_n_reinas_util(tablero, fila + 1, n))

    return soluciones

  # Esta función es una  recursiva que se utiliza para encontrar todas las soluciones al problema de las N reinas.

 # La función contiene una condición de parada que verifica si todas las reinas han sido colocadas (fila == n). Si esto pasa ,la función retorna una lista que representa una solución válida del tablero.

# (soluciones = []) Se inicializa una lista llamada soluciones para almacenar todas las soluciones encontradas.

#(for columna in range(n):) aca la  función utiliza un bucle for para iterar a través de todas las columnas en la fila actual (range(n)).

#(if es_seguro(tablero, fila, columna):)Para cada columna, se verifica si es seguro colocar una reina en esa posición utilizando la función es_seguro. Si es seguro, se procede.
# Se actualiza el tablero colocando una reina en la posición (fila, columna).Se realiza una llamada recursiva a resolver_n_reinas_util para continuar con la siguiente fila (fila + 1).

#(soluciones.extend(...)): Las soluciones encontradas en la llamada recursiva se extienden a la lista de soluciones actual. Esto se hace para acumular todas las soluciones válidas.

#Retorno de Soluciones (return soluciones) Finalmente, la función retorna la lista de soluciones encontradas.
