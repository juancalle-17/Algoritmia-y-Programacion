clientes = {}
precio = 0.15
nombre = input("ingresar usuario")
consumo = input("consumo en kWh")
clientes[nombre] = consumo
total_pagar = 0.15 * (clientes[nombre] * 1)
print("Cliente:", nombre)
print("Consumo:", clientes[nombre], "kWh")
print("Total a pagar: $", total_pagar)
