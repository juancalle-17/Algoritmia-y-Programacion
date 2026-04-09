mport random

x=0
y=0

for i in range(100):
    direccion = random.randint(1,4)
    if direccion ==1:
        x = x + 1
    elif direccion == 2:
        x = x - 1
    elif direccion == 3:
        y = y + 1
    elif direccion == 4:
        y = y - 1
        
print("posicion final: (", x, ",", y, ")")
