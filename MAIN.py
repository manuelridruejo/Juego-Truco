from funciones import *
from JUGAR import *
from Clases_Juego import *


lista_jugadores = lectura ('archivo_jugadores.csv')
lista_partidas = lectura ('archivo_partidas.csv')


opcion = 1

while opcion != 4:

  print("\n\n\nBienvenido! Que desea hacer?")
  print("\n1. Buscar en la base de datos")
  print("\n2. Jugar un partido de Truco")
  print('\n3. Ajustes de usuario')
  print("\n4. Salir")

  opcion = ValidarRTA(4)
  
  if opcion == 1: ##########################
    x = 10
  
  elif opcion == 2:
    ganador, perdedor, resultado = Jugar(lista_jugadores)
    partida_jugada = Partida(ganador, perdedor, resultado, lista_partidas)
    partida_a_agregar = [partida_jugada.codigo, partida_jugada.ganador, partida_jugada.perdedor, partida_jugada.resultado, partida_jugada.fecha]
    lista_partidas.append(partida_a_agregar)
    escritura ('archivo_partidas.csv', lista_partidas)
    print(lista_partidas)
  #hay que agregar al objeto jugador 1 partida como ganada/jugada, en caso de ser al menos uno usuario

  elif opcion == 3:
    print('Bienvenido al menu de ajustes. ')
    print('1. Crear un usuario')
    print('2. Modificar la informacion de un usuario existente')
    opcion = ValidarRTA (2)

    if opcion == 1:
      
      nombre, apellido, dni, mail, clave, usuario = PedirDatos (lista_jugadores)
      jugador = Jugador (nombre, apellido, dni, mail, clave, 0, 0, usuario)
      lista_jugadores += [jugador.nombre, jugador.apellido, jugador.DNI, jugador.mail, jugador.clave, jugador.partidas_jugadas, jugador.partidas_ganadas, jugador.usuario]
      escritura ('archivo_jugadores.csv', lista_jugadores)

      print('\nEl jugador ha sido ingresado con exito!')

    elif opcion == 2:
      print('Por favor, vamos a necesitar que ingrese con su usuario.')
      nombre_us, apellido_us, dni, mail, clave, partidas_jug, partidas_gan, usuario_sesion = IniciarSesion (lista_jugadores)
      usuario_en_sesion = Jugador (nombre_us, apellido_us, dni, mail, clave, partidas_jug, partidas_gan, usuario_sesion)
      
      for jugador in range(len(lista_jugadores)):
        if lista_jugadores[jugador][7] == usuario_en_sesion.usuario:
          lista_jugadores.pop(jugador)
      
      usuario_en_sesion.modificar()
      lista_jugadores.append(usuario_en_sesion.nombre, usuario_en_sesion.apellido, usuario_en_sesion.DNI, usuario_en_sesion.mail, usuario_en_sesion.clave, usuario_en_sesion.partidas_jugadas, usuario_en_sesion.partidas_ganadas, usuario_en_sesion.usuario)

      escritura ('archivo_jugadores.csv', lista_jugadores)


  elif opcion == 4:
    print('\nGracias por usar nuestro codigo!')
    print('Saludos.')
