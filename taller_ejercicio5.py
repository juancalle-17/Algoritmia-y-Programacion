import random

# 1) Elegir dificultad
def elegir_dificultad():
    print("Seleccione dificultad:")
    print("1. Fácil (10 intentos)")
    print("2. Medio (7 intentos)")
    print("3. Difícil (5 intentos)")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        return 10
    elif opcion == "2":
        return 7
    elif opcion == "3":
        return 5
    else:
        print("Opción no válida, se asigna Fácil")
        return 10

# 2) Generar número aleatorio
def generar_numero():
    return random.randint(1, 100)

# 3) Juego principal
def jugar(intentos):
    numero_secreto = generar_numero()
    intentos_restantes = intentos
    
    while intentos_restantes > 0:
        print(f"\nIntentos restantes: {intentos_restantes}")
        intento = int(input("Adivina el número (1-100): "))
        
        if intento == numero_secreto:
            print("¡Correcto! Adivinaste el número 🎉")
            return True, intentos - intentos_restantes + 1
        
        elif intento < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")
        
        intentos_restantes -= 1
    
    print(f"Perdiste. El número era: {numero_secreto}")
    return False, intentos

# Bonus: guardar historial
def guardar_historial(resultado, intentos_usados):
    with open("historial.txt", "a") as archivo:
        if resultado:
            archivo.write(f"Ganó en {intentos_usados} intentos\n")
        else:
            archivo.write("Perdió la partida\n")


# Programa principal
def main():
    intentos = elegir_dificultad()
    resultado, usados = jugar(intentos)
    guardar_historial(resultado, usados)

# Ejecutar
main()
