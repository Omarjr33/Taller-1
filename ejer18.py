'''Solicita al usuario ingresar el número de materias que ha cursado. Para cada materia, solicita el
puntaje y determina si ha aprobado o no (>= 60). Luego, calcula el número total de créditos del
estudiante (cada materia aprobada otorga 3 créditos).'''

numero_materias = int(input("Ingresa el número de materias cursadas: "))

creditos_totales = 0

for i in range(numero_materias):
    puntaje = float(input(f"Ingrese el puntaje para la materia {i + 1}: "))

    if puntaje >= 60:
   
        creditos_totales += 3

print(f"El número total de créditos del estudiante es: {creditos_totales}")
