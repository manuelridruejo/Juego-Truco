from AD_JUGAR import *


lista_jugadores = lectura_jugadores ('archivo_jugadores.csv')
lista_partidas = lectura_partidas ('archivo_partidas.csv')


opcion = 1

while opcion != 4:

  print("\n\n\nBienvenido! Que desea hacer?")
  print("\n1. Buscar en la base de datos")
  print("2. Jugar un partido de Truco")
  print('3. Ajustes de usuario')
  print("4. Salir")

  opcion = ValidarRTA(4)
  
  if opcion == 1: 
    print('\nBienvenido al sector de analisis de datos. Que desea buscar?')
    print('1. Perfil de un usuario')
    print('2. Ver el registro de partidas')
    print('3. Buscar partida/s particular/es')
    print('4. Ranking mensual de jugadores')
    opcion = ValidarRTA (4)

    if opcion == 1:
      BuscarJugador()
    
    elif opcion == 2:
      print(RegistroPartidas(lista_partidas))
        
    elif opcion == 3:
      print(BuscarPartidaParticular(lista_partidas))
    
    elif opcion == 4:
      print(RankingMensual(lista_partidas))

  
  elif opcion == 2:
    ganador, perdedor, resultado, lista_jugadores = Jugar(lista_jugadores)
    partida_jugada = Partida(ganador, perdedor, resultado, lista_partidas)
    partida_a_agregar = [partida_jugada.codigo, partida_jugada.ganador, partida_jugada.perdedor, partida_jugada.resultado, partida_jugada.fecha]
    lista_partidas.append(partida_a_agregar)
    escritura ('archivo_partidas.csv', lista_partidas)
    escritura ('archivo_jugadores.csv', lista_jugadores)
    

  elif opcion == 3:
    print('Bienvenido al menu de ajustes. ')
    print('1. Crear un usuario')
    print('2. Modificar la informacion de un usuario existente')
    opcion = ValidarRTA (2)

    if opcion == 1:
      
      nombre, apellido, dni, mail, clave, usuario = CrearUsuario (lista_jugadores)
      jugador = Jugador (nombre, apellido, dni, mail, clave, 0, 0, usuario)
      lista_jugadores += [[jugador.nombre, jugador.apellido, jugador.DNI, jugador.mail, jugador.clave, jugador.partidas_jugadas, jugador.partidas_ganadas, jugador.usuario]]
      escritura ('archivo_jugadores.csv', lista_jugadores)

      print('\nEl jugador ha sido ingresado con exito!')

    elif opcion == 2:
      print('Por favor, vamos a necesitar que ingrese con su usuario.')
      nombre_us, apellido_us, dni, mail, clave, partidas_jug, partidas_gan, usuario_sesion = IniciarSesion (lista_jugadores)
      usuario_en_sesion = Jugador (nombre_us, apellido_us, dni, mail, clave, partidas_jug, partidas_gan, usuario_sesion)
      
      usuario_a_modificar = 0
      for jugador in range(len(lista_jugadores)):
        if lista_jugadores[jugador][7] == usuario_en_sesion.usuario:
          usuario_a_modificar = jugador
      
      lista_jugadores.pop(usuario_a_modificar)
      
      seguir = 1
      while seguir != 2:
        usuario_en_sesion.modificar(lista_jugadores)
        print('Quiere seguir modificando su usuario?')
        print('1. Si')
        print('2. No')
        seguir = ValidarRTA(2)

      print('\nDatos cambiados con exito!')

      lista_jugadores.append([usuario_en_sesion.nombre, usuario_en_sesion.apellido, usuario_en_sesion.DNI, usuario_en_sesion.mail, usuario_en_sesion.clave, usuario_en_sesion.partidas_jugadas, usuario_en_sesion.partidas_ganadas, usuario_en_sesion.usuario])
      escritura ('archivo_jugadores.csv', lista_jugadores)

  elif opcion == 4:
    print('\nGracias por usar nuestro codigo!')
    print('Saludos.')