while True:
    print()
    print("\n *****************")
    print("1- Suma")
    print("2- Resta")
    print("3- Division")
    print("4- Multiplicacion")
    print("5- Salir")
    print()
    opcion = int(input("Ingrese la opcion: "))
    num_uno = int(input("Ingrese el primer numero: "))
    num_dos = int(input("Ingrese el segundo numero: "))
    match opcion:
        case 1:
            suma = num_uno + num_dos
            print(f"El resultado es:  {suma}")
        case 2:
            resta = num_uno - num_dos
            print(f"El resultado de la resta es: {resta}")
        case 3:
            divison = num_uno / num_dos
            print(f"EL resultado de la division es: {divison}")
        case 4:
            multiplicacion = num_uno * num_dos
        case 5:
            print("Saliendo del programa...")
            break
