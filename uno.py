true = 1
initflap = true
tipodeboletos = 0
 


print("-" * 25)
print("Bienvenido a aerolinia esDuoc")
print("-" * 25)

while (initflap == True) :

  print("-"*30)
  print("1. ver asientos diponibles")
  print("2. comprar asiento")
  print("3. anular vuelo")
  print("4. modificar datos de pasajero")
  print("5. salir")
  print("-"*30)


  opSelect = int(input("Ingrese opción a ejecutar: "))

  while opSelect < 1 or opSelect > 5:

      print("Opción Incorrecta! Intente Nuevamente")
      opSelect = int(input("Ingrese opción a ejecutar: "))

  if opSelect == 1:

   num:str(input("ingrese su nombre :"))
   rut:str(input("ingrese su rut :"))
   banco:str(input("ingrese su banco :"))
   tele:str(input("ingrese su telefono :"))

   import numpy as np

   listasientos = np.arange(1,43,1, dtype=object)
   listasientos = listasientos.reshape(7,6)
   print (listasientos)

 
  if opSelect == 2:

    try:
      tipodeboletos = int(input("cantidad de boleto: "))
    except:
      print("error ingrese una cantidad de boleto")
      tipodeboletos = int(input("cantidad de boleto: "))

  for i in range(tipodeboletos):
      print("-" * 25)
      print("selecione boleto: ")
      print("-" * 25)
      print("1 asiento normal.   $78.900")
      print("2 asiento vip.      $240.000")
      print("-" * 25)
      opselecionada = int(input("ingrese boleto: "))

  if opSelect == 3:

     def anularvuelo(reservavuelo,listaasientos):
         opanul=input(f"el asiento que usted tiene reservado es el {reservavuelo[0]}. ¿desea anular su reserva? (y/n): ")                                                                
         while opanul !='y' and opanul != 'n':
            print("opcion no valida. vuelva a intentarlo.")
            opanul=input(f"¿desea anular su reserva de su asiento{reservavuelo[0]}? (y/n): ")
         if opanul =='y':
            listaasientos[reservavuelo[1]]=reservavuelo[0]


         else:
             pass
    
     def modificarpasajero(datos, reservauelo):
       rutPasajero = int(input("Ingrese el rut del pasajero que desea modificar: "))
     asientoPasajero = int(input("Ingrese el asiento del pasajero que desea modificar: "))
     if rutPasajero == datos[1] and asientoPasajero == reservaVuelo[0]:
        print("Pasajero válido.")
        print("¿Qué dato desea modificar?")
        print("1. Nombre del pasajero")
        print("2. Teléfono del pasajero")
        print("3. Cancelar acción")
        opMod = int(input())
        while opMod < 1 or opMod > 3:
            print("Opción no válida. Vuelva a ingresar una opción: ")
            opMod=int(input())
        if opMod == 1:
            print(f"Nombre del pasajero: {datos[0]}")
            nomPasajero=input("Ingrese nuevo nombre: ")
            datos[0] = nomPasajero
            print("Nombre de pasajero actualizado. Regresando al menú.")
        elif opMod == 2:
            print(f"Teléfono del pasajero: {datos[2]}")
            telPasajero=int(input("Ingrese nuevo teléfono (formato 9 dígitos sin +56): "))
            while telPasajero < 199999999 or telPasajero > 999999999:
                print("Teléfono ingresado no válido. Vuelva a ingresar su teléfono (formato 9 dígitos sin +56): ")
                telPasajero=int(input())
            datos[2] = telPasajero
            print("Teléfono de pasajero actualizado. Regresando al menú.")
        else:
            print("Regresando al menú")
     else:
        print("Datos ingresados no corresponden a nigun pasajero. regresando al menu.") 


               
     










