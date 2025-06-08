# Burbuja, selección, inserción, mezcla
# utils/data_management.py
import json
from utils.file_administration import *



# Algoritmo de ordenamiento burbuja, pero con los nombres
# Funciona por medio de codigo ASCII

def sort_elements_by(criteria, file):
    elemets = read_json(file)
    n = len(elemets)

    for i in range(n):
        for j in range(0, n - i - 1):
            valor_actual = elemets[j].get(criteria, 0)
            valor_siguiente = elemets[j + 1].get(criteria, 0)

            # Burbuja clásica: si el actual es mayor que el siguiente, intercambiar
            if valor_actual > valor_siguiente:
                elemets[j], elemets[j + 1] = elemets[j + 1], elemets[j]

    write_json(elemets, file)