print("Tienda de Ramon")

dict = {"manzana" : 2.5,
          "banana" : 1.8,
          "naranja" : 3.0,
          "pera" : 2.0,
          "monster" : 5.0,
          "agua" : 1.0,
          "coca-cola" : 3.5,}

print("1. Existencia en inventario")
print("2. Nuevo Producto")
print("3. Eliminar Producto")
print("4. Nuevo precio")
opcion = int(input("seleccion una opcion: "))

if opcion == 1:
    print("verificacion de productos")
    producto = input("ingrese el producto a verificar: ")
    if producto in dict:
        print("el producto se encuentra en el inventario")
    else:
        print("el producto no se encuentra en el inventario")
elif opcion == 2:
    print("agregar producto")
    nproducto = input("agregue nuevo producto: ")
    nprecio = float(input("ingrese nuevo precio: "))
    dict[nproducto] = nprecio
    print(dict)
elif opcion == 3:
    print("eliminar producto")
    eproducto = input("seleccione producto para eliminar: ")
    eliminar = dict.pop(eproducto)
    print(dict)
elif opcion == 4:
    print("que precio desea actualizar?: ")
    acproducto = input("producto a actualizar precio: ")
    if acproducto == "manzana":
        nuevo = float(input("nuevo precio: "))
        dict["manzana"] = nuevo
        print(dict)
    elif acproducto == "banana":
        nuevo = float(input("nuevo precio: "))
        dict["banana"] = nuevo
        print(dict)
    elif acproducto == "naranja":
        nuevo = float(input("nuevo precio: "))
        dict["naranja"] = nuevo
        print(dict)
    elif acproducto == "pera":
        nuevo = float(input("nuevo precio: "))
        dict["pera"] = nuevo
    elif acproducto == "monster":
        nuevo = float(input("nuevo precio: "))
        dict["monster"] = nuevo
        print(dict)
    elif acproducto == "agua":
        nuevo = float(input("nuevo precio: "))
        dict["agua"] = nuevo
        print(dict)
    elif acproducto == "coca-cola":
        nuevo = float(input("nuevo precio: "))
        dict["coca-cola"] = nuevo
        print(dict)
