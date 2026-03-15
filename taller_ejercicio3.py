print("todas las potencias de 2 desde 20 hasta 220")
potencia = 1
while potencia <= 220:
    print(potencia)
    potencia = potencia * 2

print("La suma de todos los números impares comprendidos entre a y b")
a=int(input("ingrese el valor de a"))
b=int(input("ingrese el valor de b"))
sumaimpares=0
num=a
while num <= b:
    if num % 2 != 0:
        sumaimpares = sumaimpares + num
    num = num + 1
    print(sumaimpares)

print("La suma de todos los dígitos impares de una entrada.")
n=int(input("ingrese el valor de n"))
sumadigitos=0
while n > 0:
    digito = n % 10
    if digito % 2 != 0:
        sumadigitos = sumadigitos + digito
    n = n // 10
    print(sumadigitos)
