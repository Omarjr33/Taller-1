'''Solicita al usuario que ingrese una temperatura y una escala (C o F). Convierte la temperatura a la
escala opuesta usando match .'''

temperatura = float(input("Ingresa la temperatura: "))
escala = input("Ingresa la escala (C para Celsius o F para Fahrenheit): ").upper()


match escala:
    case "C":
        fahrenheit = (temperatura * 9/5) + 32
        print(f"{temperatura}°C es igual a {fahrenheit}°F.")
    case "F":
        celsius = (temperatura - 32) * 5/9
        print(f"{temperatura}°F es igual a {celsius}°C.")
    case _:
        print("Escala no válida. Usa 'C' para Celsius o 'F' para Fahrenheit.")
