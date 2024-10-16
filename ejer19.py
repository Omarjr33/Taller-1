'''Solicita una calificación numérica (0-100) y convierte esa calificación a una letra usando el
siguiente esquema:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59'''

calificacion = float(input("Ingresa la calificación numérica (0-100): "))

match calificacion:
    case calificacion if 90 <= calificacion <= 100:
        letra = "A"
    case calificacion if 80 <= calificacion < 90:
        letra = "B"
    case calificacion if 70 <= calificacion < 80:
        letra = "C"
    case calificacion if 60 <= calificacion < 70:
        letra = "D"
    case calificacion if 0 <= calificacion < 60:
        letra = "F"
    case _:
        letra = "Calificación fuera de rango"

print(f"La calificación en letra es: {letra}")
