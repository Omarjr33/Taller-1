'''Solicita al usuario que ingrese las longitudes de los tres lados de un triángulo. Determina si el
triángulo es equilátero, isósceles o escaleno.'''

lado1 = float(input("Ingresa el tamaño del primer lado"))
lado2 = float(input("Ingresa el tamaño del segundo lado"))
lado3 = float(input("Ingresa el tamaño del tercer lado"))
if (lado1+lado2+lado3) and (lado1+lado2>lado3) and (lado1+lado3>lado1):
    if lado1==lado2==lado3:
        print("Es un triángulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Es un triángulo isósceles.")
    else:
        print("Es un triángulo escaleno.")
else:
    print("Los lados ingresados no forman un triángulo válido.")