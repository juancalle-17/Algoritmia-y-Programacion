import time

hora = input("Ingrese la hora (ejemplo: 6 AM): ")

if hora == "6 AM":
    print("Alarma activada")

    print("Esperando 1 minuto o presiona Enter para apagarla...")
    
    inicio = time.time()

    while True:
        if time.time() - inicio >= 60:
            break
        if input() == "":
            break

    print("Alarma desactivada")
