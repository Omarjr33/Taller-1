'''Calculadora simple'''

numero1 = float(input("DIgite el primer numero"))
numero2 = float(input("Digite el otro numero"))
operacion = input("ingresa una operación(+,-,/,*,): ")
match operacion:
    case '+':
        resultado = numero1 + numero2
        print (f'El resultado de {numero1} y {numero2} es: {resultado}')
    case '-':
        resultado2 = numero1 - numero2
        print (f'El resultado de {numero1} y {numero2} es: {resultado2}')
    case '/':
        resultado3 = numero1 / numero2
        print (f'El resultado de {numero1} y {numero2} es: {resultado3}')
    case '*':
        resultado4 = numero1 * numero2
        print (f'El resultado de {numero1} y {numero2} es: {resultado4}')
