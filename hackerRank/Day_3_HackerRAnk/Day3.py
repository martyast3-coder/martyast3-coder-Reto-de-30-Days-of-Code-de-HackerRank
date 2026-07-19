#!/bin/python3

import math
import os
import random
import re
import sys


def is_weird(n):
    """
    Determina si un número es 'Weird' o 'Not Weird' según las reglas:
    - Impar -> Weird
    - Par y entre 2-5 -> Not Weird
    - Par y entre 6-20 -> Weird
    - Par y > 20 -> Not Weird
    """
    if n % 2 != 0:
        return "Weird"
    elif 2 <= n <= 5:
        return "Not Weird"
    elif 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"


if __name__ == '__main__':
    try:
        # Leemos y validamos la entrada
        N = int(input().strip())

        # Validamos que esté dentro del rango permitido por el enunciado
        if not (1 <= N <= 100):
            print("Error: N debe estar entre 1 y 100")
            sys.exit(1)

        # Llamamos a la función y mostramos el resultado
        print(is_weird(N))

    except ValueError:
        print("Error: debes ingresar un número entero válido")
        sys.exit(1)