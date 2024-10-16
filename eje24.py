'''Escribe un programa que solicite al usuario un número entero positivo n y calcule el factorial de
dicho número ( n! = 1 * 2 * 3 * ... * n ). Usa un ciclo for para realizar el cálculo.'''

texto = input("Ingresa una cadena de texto: ")

contador_vocales = 0

vocales = "aeiouAEIOU"

for caracter in texto:
    if caracter in vocales:
        contador_vocales += 1

print(f"La cadena contiene {contador_vocales} vocales.")
