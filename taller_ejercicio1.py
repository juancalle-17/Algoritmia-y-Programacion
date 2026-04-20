# Lista de temperaturas (24 horas)
temperaturas = [
    18, 17, 16, 15, 15, 16, 18, 20, 22, 24, 26, 28,
    30, 31, 29, 27, 25, 23, 22, 21, 20, 19, 18, 17
]
# 1) Función para calcular el promedio
def promedio(lista):
    return sum(lista) / len(lista)
# 2) Función para encontrar temperatura máxima y mínima
def extremos(lista):
    return max(lista), min(lista)
# 3) Función para contar valores sobre el promedio
def dias_sobre_promedio(lista):
    prom = promedio(lista)
    contador = 0
    for temp in lista:
        if temp > prom:
            contador += 1
    return contador
# Uso de las funciones
prom = promedio(temperaturas)
max_temp, min_temp = extremos(temperaturas)
sobre_prom = dias_sobre_promedio(temperaturas)
# Resultados
print("Temperatura promedio:", prom)
print("Temperatura máxima:", max_temp)
print("Temperatura mínima:", min_temp)
print("Horas por encima del promedio:", sobre_prom)
