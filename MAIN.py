from AC_analisis_data import *


lista_jugadores = lectura_jugadores ('archivo_jugadores.csv')
lista_partidas = lectura_partidas ('archivo_partidas.csv')


opcion = 1
clear_terminal()

while opcion != 4:

  print("Bienvenido! Que desea hacer?")
  print("1. Buscar en la base de datos")
  print("2. Jugar un partido de Truco")
  print('3. Ajustes de usuario')
  print("4. Salir")
  opcion = ValidarRTA(4)
  clear_terminal()


  if opcion == 1: 
    while opcion != 5:
      print('Bienvenido al sector de analisis de datos. Que desea buscar?')
      print('1. Perfil de un usuario')
      print('2. Ver el registro de partidas')
      print('3. Buscar partida/s particular/es')
      print('4. Ranking de jugadores')
      print('5. Salir')
      opcion = ValidarRTA (5)
      clear_terminal()

      if opcion == 1:
        PerfilJugador(lista_jugadores)
        print('\n')
      
      elif opcion == 2:
        registro = RegistroPartidas(lista_partidas)
        clear_terminal()
        print(registro)
        print('\n')
          
      elif opcion == 3:
        registro = BuscarPartidaParticular(lista_partidas, lista_jugadores)
        clear_terminal()
        print(registro)
        print('\n')
      
      elif opcion == 4:
        registro = Ranking(lista_partidas, lista_jugadores)
        clear_terminal()
        print(registro)

  
  elif opcion == 2:

    print('Usted ha elegido jugar una partida de TRUCO!')
    
    print('Jugador 1, desea ingresar como usuario o como invitado?') 
    print('1. Usuario')
    print('2. Invitado')
    print('3. Salir')
    opcion = ValidarRTA (3)
    clear_terminal()

    if opcion != 3:

      p1_usuario = False
      p2_usuario = False
      
      if opcion == 1:
        nombre1, apellido1, dni1, mail1, clave1, partidas_jug1, partidas_gan1, usuario1 = IniciarSesion(lista_jugadores)
        p1 = usuario1
        p1_usuario = True
    
      else:
        nombre1 = input ('Ingrese su nombre por favor: ')
        apellido1 = ''
        dni1 = ''
        mail1 = ''
        clave1 = ''
        partidas_jug1 = 0
        partidas_gan1 = 0
        usuario1 = ''
        p1 = 'Invitado '+nombre1
      

      print('Jugador 2, desea ingresar como usuario o como invitado?') 
      print('1. Usuario')
      print('2. Invitado')
      print('3. Salir')
      opcion = ValidarRTA (3)
      clear_terminal()

      if opcion != 3:
        if opcion == 1:
          nombre2, apellido2, dni2, mail2, clave2, partidas_jug2, partidas_gan2, usuario2 = IniciarSesion (lista_jugadores)
          p2 = usuario2
          p2_usuario = True
        
        else:
          nombre2 = input ('Ingrese su nombre por favor: ')
          apellido2 = ''
          dni2 = ''
          mail2 = ''
          clave2 = ''
          partidas_jug2 = 0
          partidas_gan2 = 0
          usuario2 = ''
          p2 = 'Invitado '+ nombre2
        
        if p1 == p2:
          p1 += '1'
          p2 += '2'

        ganador= ''
        perdedor= ''
        resultado= ''
        partida_jugada = Partida(ganador, perdedor, resultado, lista_partidas)
        partida_jugada.ganador, partida_jugada.perdedor, partida_jugada.resultado, lista_jugadores = partida_jugada.Jugar(p1,p2,p1_usuario,p2_usuario,lista_jugadores,nombre1, apellido1, dni1, mail1, clave1, partidas_jug1, partidas_gan1, usuario1,nombre2, apellido2, dni2, mail2, clave2, partidas_jug2, partidas_gan2, usuario2)
        partida_a_agregar = [partida_jugada.codigo, partida_jugada.ganador, partida_jugada.perdedor, partida_jugada.resultado, partida_jugada.fecha]
        lista_partidas.append(partida_a_agregar)
        escritura ('archivo_partidas.csv', lista_partidas)
        escritura ('archivo_jugadores.csv', lista_jugadores)
    

  elif opcion == 3:
    print('Bienvenido al menu de ajustes. ')
    print('1. Crear un usuario')
    print('2. Modificar la informacion de un usuario existente')
    print('3. Salir')
    opcion = ValidarRTA (3)
    clear_terminal()

    if opcion == 1:
      
      nombre, apellido, dni, mail, clave, usuario = CrearUsuario (lista_jugadores)
      jugador = UsuarioRegistrado (nombre, apellido, dni, mail, clave, 0, 0, usuario)
      lista_jugadores += [[jugador.nombre, jugador.apellido, jugador.DNI, jugador.mail, jugador.clave, jugador.partidas_jugadas, jugador.partidas_ganadas, jugador.usuario]]
      escritura ('archivo_jugadores.csv', lista_jugadores)
      clear_terminal()

      print('El jugador ha sido ingresado con exito!')
      time.sleep(2)

    elif opcion == 2:

      print('Por favor, vamos a necesitar que ingrese con su usuario.')
      nombre_us, apellido_us, dni, mail, clave, partidas_jug, partidas_gan, usuario_sesion = IniciarSesion (lista_jugadores)
      usuario_en_sesion = UsuarioRegistrado (nombre_us, apellido_us, dni, mail, clave, partidas_jug, partidas_gan, usuario_sesion)
      
      usuario_a_modificar = 0
      for jugador in range(len(lista_jugadores)):
        if lista_jugadores[jugador][7] == usuario_en_sesion.usuario:
          usuario_a_modificar = jugador
      
      lista_jugadores.pop(usuario_a_modificar)
      
      seguir = 1
      while seguir != 2:
        clear_terminal()
        usuario_en_sesion.modificar(lista_jugadores)
        clear_terminal()
        print('Quiere seguir modificando su usuario?')
        print('1. Si')
        print('2. No')
        seguir = ValidarRTA(2)

      clear_terminal()  
      print('Datos cambiados con exito!')
      time.sleep(2)
      clear_terminal()
      time.sleep(1)

      lista_jugadores.append([usuario_en_sesion.nombre, usuario_en_sesion.apellido, usuario_en_sesion.DNI, usuario_en_sesion.mail, usuario_en_sesion.clave, usuario_en_sesion.partidas_jugadas, usuario_en_sesion.partidas_ganadas, usuario_en_sesion.usuario])
      escritura ('archivo_jugadores.csv', lista_jugadores)


  elif opcion == 4:
    print('Gracias por usar nuestro codigo!')
    print('Saludos.\n')