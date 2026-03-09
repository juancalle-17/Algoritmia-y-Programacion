x = 0
y = 0

for i in range(10):
    dado = int(input("Ingrese el valor del dado (1-6): "))

    # ejemplo simple de movimiento
    if dado == 1:
        x = x + 1
    elif dado == 2:
        x = x - 1
    elif dado == 3:
        y = y + 1
    elif dado == 4:
        y = y - 1
    elif dado == 5:
        x = x + 2
    elif dado == 6:
        y = y + 2

print("Posición final:", x, y)
