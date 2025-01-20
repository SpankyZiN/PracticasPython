from datetime import datetime, timedelta
print("==========================")
print("Ejemplos practicos")
#Obtener fecha y hora actual

print("a) Obtener la fecha y hora actual")
ahora = datetime.now()
print(f"Fecha y la hora actual: {ahora}")
print("==========================")

print("b) Formatear una fecha")
#Formatear  la fecha usando strftime
print("Fecha formateada: ", ahora.strftime("%d %m %y %H:%M:%S"))
print("==========================")
print("c) Crear una fecha especifica")
mi_fecha = datetime(2025, 1, 16, 12, 30)
print(f"Fecha personalizada: {mi_fecha}")

print("==========================")
print("d) Calcular diferencias entre fechas")
fecha1 = datetime(2025, 1 ,16)
fecha2 = datetime(2025, 2, 16)
diferencia = fecha2 - fecha1
print(f"La diferencia de fechas son: {diferencia}")
print("==========================")

print("e) Sumar o restar días")
#sumar
ahora = datetime.now()
futuro = ahora + timedelta(days=10)
print(f"La fecha dentro de 10 dias es: {futuro}")
#Restar
pasado = ahora - timedelta(days=7)
print("Fecha hace 7 días:", pasado)