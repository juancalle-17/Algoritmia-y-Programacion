# Diccionario de productos (nombre: precio)
productos = {
    "agua": 1500,
    "gaseosa": 2500,
    "papas": 3000,
    "chocolate": 2000,
    "galletas": 1800
}
# Mostrar productos
def mostrar_productos(diccionario):
    print("\n--- PRODUCTOS DISPONIBLES ---")
    for nombre, precio in diccionario.items():
        print(f"{nombre} -> ${precio}")
# Verificar pago suficiente (BONUS)
def pago_suficiente(precio, dinero):
    return dinero >= precio
# Calcular cambio
def calcular_cambio(precio, dinero):
    return dinero - precio
# Proceso de compra
def comprar_producto(diccionario):
    mostrar_productos(diccionario)
    producto = input("\nIngrese el producto que desea: ").lower()
    if producto not in diccionario:
        print("Producto no disponible")
        return
    precio = diccionario[producto]
    print(f"El precio de {producto} es: ${precio}")
    dinero = int(input("Ingrese el dinero: "))
    # Verificar si alcanza el dinero
    if not pago_suficiente(precio, dinero):
        print("Dinero insuficiente. Intente nuevamente.")
        return
    cambio = calcular_cambio(precio, dinero)
    print(f"\nProducto entregado: {producto}")
    if cambio > 0:
        print(f"Su cambio es: ${cambio}")
    else:
        print("No hay cambio")
