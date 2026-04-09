print("bucle de calculo")
print("La suma de todos los números pares entre 2 y 100")

sumapar=0
numero=2

while numero <= 100:
    sumapar = sumapar + numero
    numero = numero + 2
    print(sumapar)

print("La suma de todos los cuadrados entre 1 y 100")
sumacuadrados=0
numero=1

while numero <= 100:
    sumacuadrados = sumacuadrados + numero*numero
    numero = numero + 1
    print(sumacuadrados)

print("La suma de todos los números impares entre a y b")
a=int(input("ingrese el valor de a"))
b=int(input("ingrese el valor de b"))
sumaimpares=0
num=a

while num <= b:
    if num % 2 != 0:
        sumaimpares = sumaimpares + num
    num = num + 1

print("La suma de todos los dígitos impares de n.")
n=int(input("ingrese el valor de n"))
sumadigitos=0
while n > 0:
    digito = n % 10
    if digito % 2 != 0:
        sumadigitos = sumadigitos + digito
    n = n / 10

print(sumadigitos)
