import time

contador = 1

while contador <= 10:
    print("ROJA encendida")
    time.sleep(20)

    print("VERDE encendida")
    time.sleep(40)

    print("AMARILLA encendida")
    time.sleep(5)

    print("VERDE y AMARILLA apagadas")

    contador = contador + 1

print("Proceso terminado")
