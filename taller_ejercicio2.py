# Funciones básicas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a / b


# Exponente usando multiplicación
def exponente(base, exp):
    resultado = 1
    for _ in range(int(exp)):
        resultado = multiplicacion(resultado, base)
    return resultado


# Raíz cuadrada (aproximación)
def raiz_cuadrada(n):
    if n < 0:
        return "Error: número negativo"
    x = n
    for _ in range(10):
        x = (x + n / x) / 2
    return x


# Factorial
def factorial(n):
    if n < 0:
        return "Error: no existe factorial de negativos"
    resultado = 1
    for i in range(1, int(n) + 1):
        resultado = multiplicacion(resultado, i)
    return resultado


# Inversa
def inversa(n):
    if n == 0:
        return "Error: no tiene inversa"
    return 1 / n


# Programa principal
num1 = float(input("Ingrese el número: "))
operador = input("Ingrese el operador (+, -, *, /, ^, sqrt, !, inv): ")

# Para operaciones binarias
if operador in ["+", "-", "*", "/", "^"]:
    num2 = float(input("Ingrese el segundo número: "))

if operador == "+":
    resultado = suma(num1, num2)

elif operador == "-":
    resultado = resta(num1, num2)

elif operador == "*":
    resultado = multiplicacion(num1, num2)

elif operador == "/":
    resultado = division(num1, num2)

elif operador == "^":
    resultado = exponente(num1, num2)

elif operador == "sqrt":
    resultado = raiz_cuadrada(num1)

elif operador == "!":
    resultado = factorial(num1)

elif operador == "inv":
    resultado = inversa(num1)

else:
    resultado = "Operador no válido"

print("Resultado:", resultado)
