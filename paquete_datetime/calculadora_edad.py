from datetime import datetime

fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento en formato DD/MM/YYYY: ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
fecha_actual = datetime.now()
edad = fecha_actual.year - fecha_nacimiento.year
if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1
print(f"Tu edad es: {edad} años")

