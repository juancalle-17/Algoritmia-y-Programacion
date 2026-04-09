a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")

a = float(a)
b = float(b)

if a > b:
    print("a es mayor que b")
else:
    if b > a:
        print("b es mayor que a")
    else:
        print("a es igual a b")
