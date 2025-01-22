'''
Si un cliente es mayor de edad y si es VIP "Tienes total control"
Si un cliente es menor de edad y si es VIP "Tienes acceso a ciertos lugares"
Si es mayor de edad y no es vip "Darle paso pero no a todo"
Si es menor de edad y no es vip "No puede acceder"
'''

nombre_cliente = input("Ingrese el nombre del cliente: ")
edad_cliente =  int(input("Ingrese su edad: "))
vip = False
if edad_cliente >= 18 and vip == True:
    print("Tienes total control")
elif edad_cliente <= 17 and vip == True:
    print("Tienes acceso a ciertos lugares")
elif edad_cliente >= 18 and vip != True:
    print("Darle paso pero no a todo")
else:
    print("Es menor de edad y no es vip, sin acceso")