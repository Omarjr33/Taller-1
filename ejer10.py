'''Solicita una nota numérica y clasifícala como A (90-100), B (80-89), C (70-79), D (60-69), o F (<60).'''

nota = float(input("Ingresa la nota numérica: "))

if 90 <= nota <= 100:
    print("Calificación: A")
elif 80 <= nota < 90:
    print("Calificación: B")
elif 70 <= nota < 80:
    print("Calificación: C")
elif 60 <= nota < 70:
    print("Calificación: D")
elif 0 <= nota < 60:
    print("Calificación: F")
else:
    print("Nota no válida.")