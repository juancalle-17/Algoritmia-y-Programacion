numero=int(input("Ingrese un número entero "))

divisor=2

print("los factores son")

while numero > 1:
    if numero % divisor == 0:
        print(divisor)
        numero = numero / divisor
    else: divisor = divisor + 1
