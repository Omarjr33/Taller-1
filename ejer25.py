'''Escribe un programa que solicite al usuario dos números enteros, un valor de inicio y un valor de
fin. El programa debe imprimir todos los números pares en ese rango, incluyendo los límites. Usa
un ciclo for para recorrer el rango.'''

texto = input("Ingresa una cadena de texto: ")

contador_vocales = 0


vocales = "aeiou"

for caracter in texto.lower():
    if caracter in vocales:
        contador_vocales += 1

print(f"El número de vocales en la cadena es: {contador_vocales}")
