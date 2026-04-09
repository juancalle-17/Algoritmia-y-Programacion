import time

valvula_abierta = False

while True:
    detector_vacio = input("¿Detector vacío activado? (si/no): ")
    detector_lleno = input("¿Detector lleno activado? (si/no): ")

    if detector_vacio == "si":
        valvula_abierta = True
        print("Válvula abierta")

    if detector_lleno == "si":
        valvula_abierta = False
        print("Válvula cerrada")
