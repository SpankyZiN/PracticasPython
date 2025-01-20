#datos primitivos
x = 5 #int
y= 3.14 #float
# > mayor
# < menor
#type sirve para saber el tipo de variable o el dato
#el metodo int() sirve para convertir un tipo de datos a entero
#el metodo float() sirve para convertir un tipo de datos a flotante
a = int(y) # convierte a entero
print(a)
b= float(x) #Convierte a flotante "5.0"
print(b)
print("x:", x, "y:",y)
string= str(a)
print(string + " alejandro")
x, y, z = "Mora", "Alejandro", "Alessandro"
print(x, y, z)
suma = 2 + 2
resta = 4 - 2
multiplicacion = 4*2
division = 8 / 2
divison_entero = 9 //2
module =  8%2
potencia= 2**2

#Comparacion
igual = 5 ==3
diferente = 5 != 3
mayor_que = 5 > 3
menor_que = 5 < 3
mayor_o_igual = 5 >= 3
menor_o_igual = 5 <= 3

#input() sirve para ingresar datos por teclado
#nombre = input("Ingrese su nombre: ")
#edad = input("Ingrese su edad: ")
#print(nombre)
#print(edad)

#if int(edad) >= 18:
 #   print(edad)
#else:
 #   print("Es menor de edad")

'''
cadera de texto -> string o str
numero -> interger o int | flotante o float
boleano -> verdadero o falso | true o false

operadores de comparacion siempre dan verdaero o falso

un If siempre evalua un tipo de dato booleano, por ende da una respuesta booleanda (True o false)

Ciclo repetitivo
For -> "Para"
For i in range(6)
en un For siempre empieza desde 0


'''

for i in range(9):
    resultado = 0
    resultado = i + 1
    print(resultado)