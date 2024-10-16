'''Solicita al usuario la distancia a recorrer (en km) y la velocidad promedio del automóvil (en km/h).
Calcula el tiempo de viaje en horas y minutos. Si la velocidad es mayor a 120 km/h, muestra un
mensaje de advertencia.'''

distancia = float(input("Ingresa la distancia a recorrer (en km): "))
velocidad = float(input("Ingresa la velocidad promedio del automóvil (en km/h): "))

if velocidad > 120:
    print("Advertencia: La velocidad es mayor a 120 km/h. Conduce con precaución.")

tiempo_horas = distancia / velocidad

horas = int(tiempo_horas)
minutos = int((tiempo_horas - horas) * 60)

print(f"Tiempo estimado de viaje: {horas} horas y {minutos} minutos.")
