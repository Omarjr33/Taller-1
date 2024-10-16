'''Solicita al usuario que ingrese un año y determina si es bisiesto (divisible entre 4, pero no entre
100, salvo que sea divisible entre 400).'''

año = int(input("Ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")