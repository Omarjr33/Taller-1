'''Solicita al usuario los tres ángulos de un triángulo y clasifícalo en:
Agudo: Todos los ángulos son menores a 90°.
Rectángulo: Un ángulo es exactamente 90°.
Obtuso: Un ángulo es mayor a 90°.'''

angulo1 = float(input("Ingresa el primer ángulo del triángulo (en grados): "))
angulo2 = float(input("Ingresa el segundo ángulo del triángulo (en grados): "))
angulo3 = float(input("Ingresa el tercer ángulo del triángulo (en grados): "))

if angulo1 + angulo2 + angulo3 != 180:
    print("Los ángulos ingresados no forman un triángulo válido.")
else:
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        tipo_triangulo = "Rectángulo"
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        tipo_triangulo = "Obtuso"
    else:
        tipo_triangulo = "Agudo"
    
    print(f"El triángulo es de tipo: {tipo_triangulo}")
