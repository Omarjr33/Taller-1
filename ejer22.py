'''Escribe un programa que solicite al usuario un número entero positivo n y calcule la suma de los
primeros n números enteros. Utiliza un ciclo for para realizar la suma.'''

n = int(input("Ingresa un número entero positivo: "))

if n <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    suma = 0
    for i in range(1, n + 1):
        suma += i
    
    print(f"La suma de los primeros {n} números enteros es: {suma}")
