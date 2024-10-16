'''Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario
adivinarlo. El programa debe dar pistas si el número ingresado es mayor o menor que el número
secreto. Usa un ciclo while para permitir al usuario seguir intentando hasta que adivine el
número
Ejercicio 7:'''

import random

numero_secreto = random.randint(1, 100)

intentos = 0
adivinado = False

print("¡He pensado en un número entre 1 y 100! Trata de adivinarlo.")

while not adivinado:
    intento = int(input("Ingresa tu adivinanza: "))

    intentos += 1

    if intento < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("El número secreto es menor. Intenta de nuevo.")
    else:
        adivinado = True
        print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
