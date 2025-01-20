destino = input("Ingrese el destino: (nacional o internacional) ")
peso_paquete = int(input("Ingrese el peso del paquete: (kg) "))
nacional = 10
internacional = 20
suma = 0
if destino == "nacional":
    suma = nacional * peso_paquete
else:
    suma = internacional * peso_paquete
print(f"El destino es: {destino}")
print(f"El peso es: {peso_paquete}")
print(f"El costo total es: {suma}$")


'''destino = str(input("Ingrese el destino (Nacional o Internacional): "))
peso = int(input("Ingrese el peso del paquete (kg): "))
nacional = "nacional"
internacional = "internacional"
NACIONAL = 10
INTERNACIONAL = 20
suma = 0
if destino == nacional:
    suma = NACIONAL * peso
elif destino == internacional:
    suma = INTERNACIONAL * peso
else:
    print("Proporcione una de las opciones")

print(f"El destino es: {destino}")
print(f"El peso es: {peso}")
print(f"El costo total es: {suma}$")
'''