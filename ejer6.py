'''El programa genera un número aleatorio entre 1 y 10. El usuario debe adivinar el número, y el
programa indica si el número ingresado es mayor, menor o igual al número generado.'''

import random
numers = random.randint(1, 10)

print("¡Bienvenido al juego de adivinanza de números!")
print("He generado un número entre 1 y 10. ¡Intenta adivinarlo!")
while True:
    intento = int(input("Ingresa un número: "))
    if intento < numers:
        print("El número es mayor. Intenta de nuevo.")
    elif intento > numers:
        print("El número es menor. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número {numers}.")
        break  # Terminar el juego
