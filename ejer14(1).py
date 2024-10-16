'''El programa contiene una letra secreta (por ejemplo, "A"). El usuario debe adivinar la letra, y el
programa le indicará si acertó o no.'''

letra_secreta = "A"

adivinanza = input("Adivina la letra secreta: ").upper()

match adivinanza:
    case _ if adivinanza == letra_secreta:
        print("¡Correcto! Has adivinado la letra secreta.")
    case _:
        print("Incorrecto. Intenta de nuevo.")
