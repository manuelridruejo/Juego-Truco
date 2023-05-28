from funciones import *
from Clases_Juego import *

def JugarPrimera (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_truco, quiero, mano):                 #JUGAR PRIMERA
  
  termino = False
  hubo_envido = False
  fin_partida = False
  carta1_p1=''
  ganador = ''

  if quiero == jug1 or quiero == '':

    if puntos_truco == 1:
      print('\n'+jug1+', que desea hacer?')
      mostrar_cartas(cartasj1)
      print('1. Cantar envido')
      print('2. Cantar truco')
      print('3. Tirar carta')
      print('4. Irse al mazo') 
      opcion = ValidarRTA (4)

      if opcion == 1:
        puntos1, puntos2, fin_partida = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True

        
        if fin_partida == False:

          if termino == False:
            print('\n'+jug1+', que desea hacer?')
            mostrar_cartas(cartasj1)
            print('1. Cantar truco')
            print('2. Tirar carta')
            print('3. Irse al mazo')
            opcion = ValidarRTA(3)
          else:
            opcion = 3
          
          if opcion == 1:
            puntos_truco, termino, ganador, quiero = CantarTruco (jug1, jug2)
          
            if termino != True:
              carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
              print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
          
          elif opcion == 2:
            carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
            print("\n{} ha tirado el {}".format(jug1, str(carta1_p1)))
        
          elif opcion == 3:
            termino = True
            ganador = jug2

        else:
          pass

      elif opcion == 2:
        puntos_truco, termino, ganador, quiero = CantarTruco (jug1, jug2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 4:
        termino = True
        ganador = jug2

    elif puntos_truco == 2:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo') 
      opcion = ValidarRTA (3)

      if opcion == 1:
        puntos_truco, termino, ganador, quiero = CantarReTruco (jug1, jug2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2
      
    elif puntos_truco == 3:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo') 
      opcion = ValidarRTA (3)

      if opcion == 1:
        puntos_truco, termino, ganador, quiero = CantarValeCuatro (jug1, jug2)
    
        if termino != True:
          carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2
      
    elif puntos_truco == 4:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo') 
      opcion = ValidarRTA (2)

      if opcion == 1:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        termino = True
        ganador = jug2
  
  elif quiero == jug2:

    if puntos_truco == 1:

      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar envido')
      print('2. Tirar carta')
      print('3. Irse al mazo') 
      opcion = ValidarRTA (3)

      if opcion == 1:
        puntos1, puntos2, fin_partida = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True

        if fin_partida == False:
          
          print('\n' + jug1 + ', que desea hacer?')
          mostrar_cartas (cartasj1)
          print('1. Tirar carta')
          print('2. Irse al mazo')
          opcion = ValidarRTA (2)

          if opcion == 1:
            carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
            print("\n{} ha tirado el {}".format (jug1, carta1_p1))

          elif opcion == 2:
            termino = True
            ganador = jug2

        else:
          pass

      elif opcion == 2:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2
    
    else:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo') 
      opcion = ValidarRTA (2)

      if opcion == 1:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        termino = True
        ganador = jug2
      
  return puntos1, puntos2, puntos_truco, termino, hubo_envido, carta1_p1, cartasj1, ganador, quiero, fin_partida


def JugarPrimeraSinTanto (jug1, cartasj1, jug2, puntos_truco, quiero):                            #JUGAR PRIMERA SIN TANTO
  
  carta1_p1 = ''
  ganador = ''
  termino = False 

  if quiero == jug1 or quiero == '':

    if puntos_truco == 1:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = ValidarRTA (3)

      if opcion == 1:
        puntos_truco, termino, ganador, quiero = CantarTruco (jug1, jug2)

        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2

    elif puntos_truco == 2:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = ValidarRTA (3)

      if opcion == 1:
        puntos_truco, termino, ganador, quiero = CantarReTruco (jug1, jug2)

        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2

    elif puntos_truco == 3:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = ValidarRTA (3)
      
      if opcion == 1:
        puntos_truco, termino, ganador, quiero = CantarValeCuatro (jug1, jug2)
          
        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2
    
    elif puntos_truco == 4:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo')
      opcion = ValidarRTA (2)

      if opcion == 1:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 2:
        termino = True
        ganador = jug2
  
  elif quiero == jug2:
    print('\n' + jug1 + ', que desea hacer?')
    mostrar_cartas (cartasj1)
    print('1. Tirar carta')
    print('2. Irse al mazo')
    opcion = ValidarRTA (2)

    if opcion == 1:
      carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
      print("\n{} ha tirado el {}".format (jug1, carta1_p1))

    elif opcion == 2:
      termino = True
      ganador = jug2

  return puntos_truco, termino, carta1_p1, cartasj1, ganador, quiero


def Jugar_Segunda(p1, puntos1, p2, puntos2, cartasj1, puntos_truco, quiero):                            #JUGAR SEGUNDA MANO
  
  termino= False
  carta1_p1 = ""
  ganador = ''

  if quiero == p1 or quiero == '':

    if puntos_truco == 1:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas(cartasj1)
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = ValidarRTA (3)
          
      if opcion == 1:
        
        puntos_truco, termino, ganador, quiero = CantarTruco (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))
 
      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2 

    elif puntos_truco == 2:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = ValidarRTA (3)

      if opcion == 1:
        
        puntos_truco, termino, ganador, quiero = CantarReTruco (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
          print("\n{} ha tirado el {}".format(p1,carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
        print("\n{} ha tirado el {}".format(p1, carta1_p1))
 
      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 3:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = ValidarRTA (3)

      if opcion == 1:     
        puntos_truco, termino, ganador, quiero = CantarValeCuatro (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 4:
      carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
      print("\n{} ha tirado el {}".format (p1, carta1_p1))
  
  elif quiero == p2:
    print('\n' + p1 + ', que desea hacer?')
    mostrar_cartas (cartasj1)
    print('1. Tirar carta')
    print('2. Irse al mazo')
    opcion = ValidarRTA (2)

    if opcion == 1:
      carta1_p1, cartasj1 = tirar_2 (p1, cartasj1)
      print("\n{} ha tirado el {}".format (p1, carta1_p1))

    elif opcion == 2:
      termino = True
      ganador = p2
     
  return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, ganador, quiero 


def Jugar_Tercera (p1, puntos1, p2, puntos2, cartasj1, puntos_truco, quiero):                #JUGAR TERCER MANO
  
  termino = False
  carta1_p1 = ""
  ganador = ''

  if quiero == p1 or quiero == '':

    if puntos_truco == 1:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar truco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = ValidarRTA (3)
      
      if opcion == 1:
        puntos_truco, termino, ganador, quiero = CantarTruco (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 2:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar retruco')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = ValidarRTA (3)

      if opcion == 1:
        
        puntos_truco, termino, ganador, quiero = CantarReTruco (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 3:
      print('\n' + p1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar vale cuatro')
      print('2. Tirar carta')
      print('3. Irse al mazo')
      opcion = ValidarRTA (3)

      if opcion == 1:
        
        puntos_truco, termino, ganador, quiero = CantarValeCuatro (p1, p2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
          print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
        print("\n{} ha tirado el {}".format (p1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = p2

    elif puntos_truco == 4:
      carta1_p1, cartasj1 = tirar_1 (p1, cartasj1)
      print("\n{} ha tirado el {}".format (p1, carta1_p1))
   
  elif quiero == p2:
    print('\n' + p1 + ', que desea hacer?')
    mostrar_cartas (cartasj1)
    print('1. Tirar carta')
    print('2. Irse al mazo')
    opcion = ValidarRTA (2)

    if opcion == 1:
      carta1_p1, cartasj1 = tirar_1(p1, cartasj1)
      print("\n{} ha tirado el {}".format(p1, carta1_p1))

    elif opcion == 2:
      termino = True
      ganador = p2
     
  return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, ganador, quiero 



def Jugar(lista):    

  print('\nUsted ha elegido jugar una partida de TRUCO!')
  
  print('\nJugador 1, desea ingresar como usuario o como invitado?') 
  print('1. Usuario')
  print('2. Invitado')
  opcion = ValidarRTA (2)

  p1_usuario = False
  p2_usuario = False

  if opcion == 1:
    nombre1, apellido1, dni1, mail1, clave1, partidas_jug1, partidas_gan1, usuario1 = IniciarSesion (lista)
    jugador1 = Jugador (nombre1, apellido1, dni1, mail1, clave1, partidas_jug1, partidas_gan1, usuario1)
    p1 = jugador1.usuario
    p1_usuario = True
  
  else:
    nombre1 = input ('Ingrese su nombre por favor: ')
    p1 = 'Invitado '+nombre1
  
  puntos1 = 0

  print('\nJugador 2, desea ingresar como usuario o como invitado?') 
  print('1. Usuario')
  print('2. Invitado')
  opcion = ValidarRTA (2)

  if opcion == 1:
    nombre2, apellido2, dni2, mail2, clave2, partidas_jug2, partidas_gan2, usuario2 = IniciarSesion (lista)
    jugador2 = Jugador (nombre2, apellido2, dni2, mail2, clave2, partidas_jug2, partidas_gan2, usuario2)
    p2 = jugador2.usuario
    p2_usuario = True
  
  else:
    nombre2 = input ('Ingrese su nombre por favor: ')
    p2 = 'Invitado '+ nombre2
  
  puntos2 = 0
  
  if p1 == p2:
    p1 += '1'
    p2 += '2'

  print("\nSe ha iniciado una nueva partida entre: " + p1 + " y " + p2)

  while puntos1 < 30 and puntos2 < 30:
    
    mazo=Mazo()       #Se crea el mazo

    cartas_en_juego = mazo.repartir()      #Se reparte el mazo
    ronda = 1
    mano, puntos_mano, pie, puntos_pie = quien_es_mano (ronda, p1, puntos1, p2, puntos2)        #Se determina que jugador es mano

    cartasmano = [cartas_en_juego[0], cartas_en_juego[2], cartas_en_juego[4]]         #Se dan las cartas al mano y al pie
    cartas_pie = [cartas_en_juego[1], cartas_en_juego[3], cartas_en_juego[5]]

    print('\nComienza la ronda '+str(ronda)+'!')

    print('\n'+mano, 'es MANO.')
    mostrar_cartas(cartasmano)
    print('\n')
    print(pie, 'es PIE.')
    mostrar_cartas(cartas_pie)
    puntos_truco = 1
    que_mano_es = 1
    hubo_envido = False
    termino = False
    quiero = ''

    while que_mano_es < 4:
      
      manos_pie = 0
      manos_mano = 0
      ganador1 = ''
      ganador2 = ''
      parda1 = False
      parda2 = False                 

      #Primera mano

      puntos_mano, puntos_pie, puntos_truco, termino, hubo_envido, carta1_mano, cartas_mano, ganador, quiero, fin_partida  = JugarPrimera (mano, puntos_mano, cartasmano, pie, puntos_pie, cartas_pie, puntos_truco, quiero, mano)
      
      if termino == True and fin_partida == False:
        if quiero == '':
          puntos_truco = 2
        break
    
      if fin_partida == True:
        break
      
      if hubo_envido == True:
        puntos_truco, termino, carta1_pie, cartas_pie, ganador, quiero  = JugarPrimeraSinTanto (pie, cartas_pie, mano, puntos_truco, quiero)
    
        if termino == True: 
          break

      elif hubo_envido == False:
        puntos_pie, puntos_mano, puntos_truco, termino, hubo_envido, carta1_pie, cartas_pie, ganador, quiero, fin_partida  = JugarPrimera (pie, puntos_pie, cartas_pie, mano, puntos_mano, cartasmano, puntos_truco, quiero, mano)

        if termino == True:
          break

        if fin_partida == True:
          break

      if carta1_pie > carta1_mano:
        ganador1 = pie
        print('\n'+pie, "ha ganado la mano")
        manos_pie += 1 

      elif carta1_mano > carta1_pie:
        ganador1 = mano 
        print('\n'+mano, "ha ganado la mano")
        manos_mano += 1

      elif carta1_mano == carta1_pie:
        parda1=True
        print('\nSe ha pardado')

      #Segunda Mano

      que_mano_es += 1

      if ganador1 == pie: #el pie gano primera arranca 2 el
        
        puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pie, ganador, quiero = Jugar_Segunda (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)

        if termino == True: 
          break

        puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador, quiero = Jugar_Segunda (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break

      elif ganador1 == mano: #la mano gano primera arranca la 2 el
        
        puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador, quiero = Jugar_Segunda (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break

        puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pie, ganador, quiero = Jugar_Segunda (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
        
        if termino == True: 
          break

      elif  parda1 == True: #Se juega la parda
        
        puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador, quiero = Jugar_Segunda (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break
        
        puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pie, ganador, quiero = Jugar_Segunda (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
        
        if termino == True: 
          break
        
        if carta2_mano == carta2_pie: #Se pardo segunda
          parda2 = True
          print("\nSe ha pardado")

        elif carta2_mano > carta2_pie: #gano la mano
          ganador = mano
          break
        
        elif carta2_pie > carta2_mano: #gano el pie
          ganador = pie
          break 
        
      if carta2_mano > carta2_pie: #mano gana segunda
        ganador2 = mano
        print('\n'+mano, "ha ganado la mano")
        manos_mano += 1

      elif carta2_pie > carta2_mano: #pie gana segunda
        ganador2 = pie
        manos_pie += 1
        print('\n'+pie, "ha ganado la mano")

      elif carta2_pie == carta2_mano and parda1 == False: #se parda 2 y no esta pardada primera
        if ganador1 == pie:
          ganador = pie
          break

        elif ganador1 == mano:
          ganador = mano

      if manos_pie == 2:
        ganador = pie
        break

      if manos_mano == 2:
        ganador = mano
        break 

      # Tercera Mano 
      
      que_mano_es += 1

      if ganador2 == pie:                 #pie gana 2 arranca en 3
      
        puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pie, ganador, quiero = Jugar_Tercera (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)

        if termino == True: 
          break

        puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador, quiero = Jugar_Tercera (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break

      elif ganador2 == mano: #mano gano 2 arranca en 3
        puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador, quiero = Jugar_Tercera (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break

        puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pie, ganador, quiero = Jugar_Tercera (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
        
        if termino == True: 
          break
        
      elif  parda2 == True and parda1 == True: #Se juega la parda
        puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador, quiero = Jugar_Tercera (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
        
        if termino == True: 
          break
        
        puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pie, ganador, quiero = Jugar_Tercera (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
        
        if termino == True: 
          break
        
        if carta3_mano == carta3_pie: #Se pardo tercera gana la mano
          ganador = mano

        elif carta3_mano > carta3_pie: #gano la mano
          ganador = mano
        
        elif carta3_pie > carta3_mano: #gano el pie
          ganador = pie
        
      elif carta3_mano > carta3_pie: #gano la mano la 3 se le suman los puntos
        ganador = mano
        break

      elif carta3_pie > carta3_mano: #gano el pie la tercera se le suman los puntos
        ganador = pie
        break

      que_mano_es += 1

    if fin_partida == False:
      if ganador == mano:
        puntos_mano += puntos_truco
        print("\nHa ganado: ", mano, " se le suman ", puntos_truco, " puntos")
        
      elif ganador == pie:
        puntos_pie += puntos_truco
        print("\nHa ganado: ", pie, " se le suman ", puntos_truco, " puntos")
      
    else:
      pass

    if p1 == mano:
      puntos1 = puntos_mano
      puntos2 = puntos_pie
    elif p2 == mano:
      puntos2 = puntos_mano
      puntos1 = puntos_pie
    
    print('\nPuntos de '+ p1 + ": " + str(puntos1))
    print('\nPuntos de ' + p2 + ": " + str(puntos2))
    print('\n------------------------------------------------------------------------------\n\n')
    ronda +=1

    fin_partida = chequearganador(puntos1, puntos2)

    if fin_partida == True:
      break
  

  if puntos1 < puntos2:
    ganador_final = p2
    perdedor_final = p1
    resultado = str(puntos2) + "-" + str(puntos1)
    print('\nFELICITACIONES ' + p2 + ', USTED HA GANAD0!')
    print('\nSe ha guardado el registro de la partida completo, el jugador '+p2+' ha derrotado a '+p1+' con un resultado de '+resultado+'.')
    if p1_usuario == True:
      jugador1.jugo_partida()
      for jugador in range(len(lista)):
        if jugador1.usuario == lista[jugador][7]:
          lista.pop(jugador)
          lista.append([jugador1.nombre,jugador1.apellido,jugador1.DNI,jugador1.mail,jugador1.clave,jugador1.partidas_jugadas,jugador1.partidas_ganadas,jugador1.usuario])

    if p2_usuario == True:
      jugador2.gano_partida()
      for jugador in range(len(lista)):
        if jugador2.usuario == lista[jugador][7]:
          lista.pop(jugador)
          lista.append([jugador2.nombre,jugador2.apellido,jugador2.DNI,jugador2.mail,jugador2.clave,jugador2.partidas_jugadas,jugador2.partidas_ganadas,jugador2.usuario])

  else:
    ganador_final = p1
    perdedor_final = p2
    resultado = str(puntos1) + "-"+str(puntos2)
    print('\nFELICITACIONES ' + p1 + ', USTED HA GANAD0!')
    print('\nSe ha guardado el registro de la partida completo, el jugador '+p1+' ha derrotado a '+p2+' con un resultado de '+resultado+'.')
    if p1_usuario == True:
      jugador1.gano_partida()
      for jugador in range(len(lista)-1):
        if jugador1.usuario == lista[jugador][7]:
          lista.pop(jugador)
          lista.append([jugador1.nombre,jugador1.apellido,jugador1.DNI,jugador1.mail,jugador1.clave,jugador1.partidas_jugadas,jugador1.partidas_ganadas,jugador1.usuario])

    if p2_usuario == True:
      jugador2.jugo_partida()
      for jugador in range(len(lista)):
        if jugador2.usuario == lista[jugador][7]:
          lista.pop(jugador)
          lista.append([jugador2.nombre,jugador2.apellido,jugador2.DNI,jugador2.mail,jugador2.clave,jugador2.partidas_jugadas,jugador2.partidas_ganadas,jugador2.usuario])
  
    

  return ganador_final, perdedor_final, resultado, lista
  
  
  
  