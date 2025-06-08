from typing import List, Tuple

def mejor_ruta_apuestas(
    saldo_inicial: float,
    apuestas_posibles: List[int],
    tabla: List[List[float]]
) -> Tuple[float, List[int]]:
    """
    Utiliza backtracking para encontrar la mejor ruta de apuestas que maximiza las ganancias
    sin quedarse con saldo cero o negativo en ningún momento.

    Parámetros:
    - saldo_inicial: cantidad inicial de dinero disponible.
    - apuestas_posibles: lista de montos de apuesta permitidos.
    - tabla: matriz de multiplicadores. Cada fila es una ronda, cada columna un tipo de apuesta.

    Retorna:
    - mejor_saldo: el mayor saldo final alcanzado.
    - mejor_ruta: la secuencia de apuestas (una por ronda) que llevó a ese saldo.
    """
    mejor_saldo = -1
    mejor_ruta = []

    def backtrack(ronda: int, saldo_actual: float, ruta_actual: List[int]):
        nonlocal mejor_saldo, mejor_ruta

        # Caso base: terminamos todas las rondas
        if ronda == len(tabla):
            if saldo_actual > mejor_saldo:
                mejor_saldo = saldo_actual
                mejor_ruta = ruta_actual[:]
            return

        # Intentamos cada apuesta posible si el saldo lo permite
        for i, apuesta in enumerate(apuestas_posibles):
            if saldo_actual >= apuesta:
                multiplicador = tabla[ronda][i]
                ganancia = apuesta * multiplicador
                nuevo_saldo = saldo_actual - apuesta + ganancia

                if nuevo_saldo > 0:
                    ruta_actual.append(apuesta)
                    backtrack(ronda + 1, nuevo_saldo, ruta_actual)
                    ruta_actual.pop()  # backtrack

    # Comenzamos desde la ronda 0
    backtrack(0, saldo_inicial, [])
    return mejor_saldo, mejor_ruta


# ---------------------------------------
# Ejemplo de uso
# ---------------------------------------
if __name__ == "__main__":
    # Saldo inicial
    saldo_inicial = 100

    # Apuestas posibles
    apuestas_posibles = [10, 20, 50]

    # Tabla de multiplicadores por ronda
    # tabla[fila][columna] = multiplicador de apuesta
    tabla = [
        [1.5, 0.5, 2.0],  # Ronda 0
        [0.8, 1.2, 0.6],  # Ronda 1
        [2.0, 1.0, 0.3]   # Ronda 2
    ]

    # Ejecutamos la estrategia
    saldo_final, ruta = mejor_ruta_apuestas(saldo_inicial, apuestas_posibles, tabla)

    print("=== Resultados ===")
    print(f"Saldo inicial: {saldo_inicial}")
    print(f"Saldo final óptimo: {saldo_final:.2f}")
    print(f"Ruta de apuestas (una por ronda): {ruta}")
