'''Escribe un programa que solicite al usuario ingresar números enteros indefinidamente. El
programa debe sumar los números siempre que sean pares, pero debe detenerse si el usuario
ingresa un número impar. Usa un ciclo while para lograr esto.
'''

suma_pares = 0

print("Ingresa números enteros. El programa sumará los números pares. El programa terminará si introduces un número impar.")

while True:
    numero = int(input("Introduce un número entero: "))

    if numero % 2 != 0:
        print("Número impar detectado. El programa se detendrá.")
        break

    suma_pares += numero

print(f"La suma de los números pares es: {suma_pares}")
