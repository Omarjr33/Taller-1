'''El costo de estacionamiento se calcula de la siguiente manera:
Primera hora: $5
Segunda a cuarta hora: $4 por hora
Más de cuatro horas: $3 por cada hora adicional
Solicita al usuario el número de horas de estacionamiento y calcula el costo total'''

horas = float(input("Ingresa el número de horas de estacionamiento: "))

costo_total = 0

if horas > 0:
    costo_total += 5

    if horas > 1:
        horas_adicionales = min(horas - 1, 3) 
        costo_total += horas_adicionales * 4

    if horas > 4:
        horas_adicionales = horas - 4
        costo_total += horas_adicionales * 3

print(f"El costo total de estacionamiento es: ${costo_total:.2f}")
