# Diccionario corregido
notas = {
    "Harry": [3.8, 4.0, 4.2],
    "Ron": [3.2, 3.8, 2.8],
    "Hermione": [5.0, 5.0, 5.0],
    "Draco": [4.5, 4.2, 5.0],
    "Neville": [2.5, 3.0, 3.2]
}
# 1) Promedio simple
def promedio_simple(lista):
    return sum(lista) / len(lista)
# 2) Promedio ponderado (30%, 30%, 40%)
def promedio_ponderado(lista):
    return lista[0]*0.3 + lista[1]*0.3 + lista[2]*0.4
# 3) Estudiante con mayor promedio final
def mejor_estudiante(diccionario):
    mejor = None
    mejor_prom = 0
    for nombre, lista in diccionario.items():
        prom = promedio_ponderado(lista)
        if prom > mejor_prom:
            mejor_prom = prom
            mejor = nombre
    return mejor, mejor_prom
# 4) Mostrar aprobados (>= 3.0)
def mostrar_aprobados(diccionario):
    print("\nEstudiantes aprobados:")
    for nombre, lista in diccionario.items():
        prom = promedio_ponderado(lista)
        if prom >= 3.0:
            print(f"{nombre}: {prom:.2f}")
# Bonus: mensaje tipo profesora McGonagall
def resultado_final(diccionario):
    print("\nResultados finales:")
    for nombre, lista in diccionario.items():
        prom = promedio_ponderado(lista)
        if prom >= 3.0:
            print(f"{nombre} ha aprobado la clase de la profesora McGonagall con {prom:.2f}")
        else:
            print(f"{nombre} ha reprobado la clase de la profesora McGonagall con {prom:.2f}")
# Uso del programa
print("Promedios simples:")
for nombre, lista in notas.items():
    print(f"{nombre}: {promedio_simple(lista):.2f}")
mejor, prom = mejor_estudiante(notas)
print(f"\nMejor estudiante: {mejor} con promedio {prom:.2f}")
mostrar_aprobados(notas)
resultado_final(notas)
