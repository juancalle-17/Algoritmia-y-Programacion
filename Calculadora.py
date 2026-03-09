num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese el operador (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2

elif operador == "-":
    resultado = num1 - num2

elif operador == "*":
    resultado = num1 * num2

elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Error: no se puede dividir por cero")
        resultado = None
else:
    print("Operador no válido")
    resultado = None

if resultado != None:
    print("Resultado:", resultado)
