nombre_cliente = input("Ingrese su nombre: ")
dias_en_hotel = int(input("Ingrese los dias de estadia: "))
vista_mar = bool(input("Desea tener vista al mar? (True o False)"))
con_vista = 150.50
sin_vista = 125.50
if vista_mar:

    print("Cliente: ",nombre_cliente)
    print("Dias de estadia: ",dias_en_hotel)
    print("Costo Total: ", dias_en_hotel * con_vista)
    print("Habitacion con vista: ", vista_mar)

elif not vista_mar:
    print("Cliente: ", nombre_cliente)
    print("Dias de estadia: ", dias_en_hotel)
    print("Costo Total: ", dias_en_hotel * sin_vista)
    print("Habitacion con vista: ", vista_mar)
else:
    print("Ocurrio un problema")