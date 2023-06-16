from random import shuffle
from AA_validaciones import *
from AA_CONSTANTES import *


class Carta():
  def __init__ (self, palo : str, numero : int):
    self.palo = palo
    self.numero = numero
    self.jerarquia = JERARQUIAS[(palo, numero)]
    self.jerarquia_envido = JERARQUIAS_ENVIDO [(palo, numero)]

  def __str__ (self):
    return "{} de {}".format(self.numero, self.palo)
  
  def __eq__ (self, other):
    return self.jerarquia == other.jerarquia 
  
  def __gt__ (self, other):
    return self.jerarquia > other.jerarquia

  def __lt__ (self, other):
    return self.jerarquia < other.jerarquia 
  
  def __ge__ (self, other):
    return self.jerarquia >= other.jerarquia 
  
  def __le__ (self, other):
    return self.jerarquia <= other.jerarquia 
  
  def __ne__ (self, other):
    return self.jerarquia != other.jerarquia 

  def __repr__ (self):
    return str (self)

class Mazo():
  def __init__(self) -> None:
    self.cartas = []
    for palo in PALOS:
      for numero in NUMEROS:
        self.cartas.append (Carta(palo, numero))
    self.mezclar()
  
  def __str__(self):
    impresion_mazo = ""
    for carta in self.cartas:
      impresion_mazo += (str(carta) + "\n")
    impresion_mazo = impresion_mazo[:-1]
    return impresion_mazo
  
  def mezclar (self):
    shuffle (self.cartas)
  
  def repartir (self):
    cartas=[]
    for i in range(6):
      cartas.append (self.cartas[i])
    return cartas
  
  def quien_es_mano (self,ronda, p1, puntos1, p2, puntos2):
  
    if ronda%2 == 0:
      mano = p1
      pie = p2
      puntos_mano = puntos1
      puntos_pie = puntos2

    if ronda%2 != 0:
      mano = p2
      pie = p1
      puntos_mano = puntos2
      puntos_pie = puntos1

    return mano, puntos_mano, pie, puntos_pie

class Jugador():
  
  def __init__ (self, nombre : str, apellido : str, DNI: int):
    self.nombre = nombre
    self.apellido = apellido
    self.DNI = DNI

class UsuarioRegistrado(Jugador):

  def __init__ (self, nombre : str, apellido : str, DNI: int, mail: str, clave: str, partidas_jugadas: int, partidas_ganadas: int, usuario: str):
    super().__init__(nombre, apellido, DNI)
    self.mail = mail
    self.clave = clave
    self.partidas_jugadas = partidas_jugadas
    self.partidas_ganadas = partidas_ganadas
    self.usuario = usuario
  
  def gano_partida(self):
    self.partidas_ganadas += 1
    self.partidas_jugadas += 1
  
  def jugo_partida (self):
    self.partidas_jugadas += 1

  def modificar(self, lista):
    print("Usted ha decidido modificar su usuario. Que atributo desea modificar?")
    print("\n1. Nombre")
    print("2. Apellido")
    print("3. DNI")
    print("4. Mail")
    print('5. clave')
    print('6. usuario')

    opcion = ValidarRTA(6)

    if opcion == 1:
      print("Usted ha elegido modificar su nombre")
      nombre_nuevo = input("Ingrese la informacion nueva: ")
      self.nombre = nombre_nuevo
      clear_terminal()
      print('Nombre cambiado con exito.')
      time.sleep(2)

    elif opcion == 2:
      print("Usted ha elegido modificar su apellido.")
      apellido_nuevo = input("Ingrese la informacion nueva: ")
      self.apellido = apellido_nuevo
      clear_terminal()
      print('Apellido cambiado con exito.')
      time.sleep(2)

    elif opcion == 3:
      print("Usted ha elegido modificar su DNI.")
      dni_nuevo = PedirDNI ()
      existe = Validar (lista, dni_nuevo, 2)
      while existe == True:
        print('DNI ya existente. Vuelva a intentarlo.')
        dni_nuevo = PedirDNI ()
        existe = Validar (lista, dni_nuevo, 2)
      self.DNI = dni_nuevo
      clear_terminal()
      print('DNI cambiado con exito.')
      time.sleep(2)
      
    elif opcion == 4:
      print("Usted ha elegido modificar su mail.")
      mail_nuevo = PedirMail()
      existe = Validar (lista, mail_nuevo, 3)
      while existe == True:
        print('mail ya existente. Vuelva a intentarlo.')
        mail_nuevo = PedirMail ()
        existe = Validar (lista, mail_nuevo, 3)
      self.mail = mail_nuevo
      clear_terminal()
      print('Mail cambiado con exito.')
      time.sleep(2)
    
    elif opcion == 5:
      print("Usted ha solicitado modificar su clave")
      nueva_clave =  Validarclave()

      self.clave = nueva_clave
      clear_terminal()
      print('Contraseña cambiada con exito.')
      time.sleep(2)
    
    elif opcion == 6:
      usuario_nuevo = input('Ingrese su usuario: ')
      existe = Validar (lista, usuario_nuevo, 7)
      while existe == True:
        print('Nombre de usuario ya existente. Vuelva a intentarlo.')
        usuario_nuevo = input('Ingrese su usuario: ')
        existe = Validar (lista, usuario_nuevo, 7)
      self.usuario = usuario_nuevo
      clear_terminal()
      print('Usuario cambiado con exito.')
      time.sleep(2)
  
  def __str__ (self):
    if self.partidas_jugadas==0:
      porcentaje = 0
    else:
      porcentaje= float(round(self.partidas_ganadas/self.partidas_jugadas, 2))
    return "Usuario: {}\nNombre: {}\nApellido: {}\nMail: {}\nPartidas jugadas: {}\nPorcentaje de victoria: {}".format(self.usuario, self.nombre, self.apellido, self.mail, self.partidas_jugadas, porcentaje)

class Partida():

  def __init__ (self, ganador: str, perdedor: str, resultado: str, lista_partidas):
    self.codigo = self.asignar_codigo (lista_partidas)
    self.ganador = ganador
    self.perdedor = perdedor
    self.resultado = resultado
    self.fecha = date.today()

  def asignar_codigo (self, lista_partidas):
    aux=''
    if len(lista_partidas) == 0:
      codigo = '0000001'
    else:
      cod = str(len(lista_partidas) + 1)
      largo = len(cod)
      for i in range(7-largo):
        aux += '0'
      codigo = aux + cod
      
    return codigo

  def __str__ (self):
    return "COD_PARTIDA {}:  {} vencio a {} con un resultado de {} el dia de la fecha {}".format(self.codigo, self.ganador, self.perdedor, self.resultado, self.fecha)
  
  def JugarPrimera (self,jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_truco, quiero, mano):                 #JUGAR PRIMERA
    
    termino = False
    hubo_envido = False
    fin_partida = False
    carta1_p1=''
    ganador = ''
    time.sleep(1)
    if quiero == jug1 or quiero == '':

      if puntos_truco == 1:
        print(jug1+', que desea hacer?')
        self.mostrar_cartas(cartasj1)
        print('1. Cantar envido')
        print('2. Cantar truco')
        print('3. Tirar carta')
        print('4. Irse al mazo')
        print('5. Rendirse')
        opcion = ValidarRTA (5)
        clear_terminal()

        if opcion == 1:
          puntos1, puntos2, fin_partida = self.envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
          hubo_envido = True

          if fin_partida == False:

            if termino == False:
              clear_terminal()
              print(jug1+', que desea hacer?')
              self.mostrar_cartas(cartasj1)
              print('1. Cantar truco')
              print('2. Tirar carta')
              print('3. Irse al mazo')
              print('4. Rendirse')
              opcion = ValidarRTA(4)
              clear_terminal()

            else:
              opcion = 3
            
            if opcion == 1:
              clear_terminal()
              puntos_truco, termino, ganador, quiero, fin_partida = self.CantarTruco (jug1, jug2)
            
              if termino != True:
                clear_terminal()
                carta1_p1, cartasj1 = self.tirar_3(jug1, cartasj1)
                print("{} ha tirado el {}".format(jug1, str(carta1_p1)))
                print('\n')
              elif fin_partida == True:
                if ganador == jug1:
                  puntos1 = 30
                  puntos2 = 0
                elif ganador == jug2:
                  puntos2 = 30
                  puntos1 = 0
            
            elif opcion == 2:
              carta1_p1, cartasj1 = self.tirar_3(jug1, cartasj1)
              print("{} ha tirado el {}".format(jug1, str(carta1_p1)))
              print('\n')
          
            elif opcion == 3:
              termino = True
              ganador = jug2
            
            elif opcion == 4:
              termino = True
              ganador = jug2
              puntos2 = 30
              puntos1 = 0
              fin_partida = True
              print(jug1+' se ha rendido')
              #fin de la partida

          else:
            pass

        elif opcion == 2:
          puntos_truco, termino, ganador, quiero, fin_partida = self.CantarTruco (jug1, jug2)
        
          if termino != True:
            clear_terminal()
            carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
            print("{} ha tirado el {}".format (jug1, carta1_p1))
            print('\n')

          elif fin_partida == True:
              if ganador == jug1:
                puntos1 = 30
                puntos2 = 0
              elif ganador == jug2:
                puntos2 = 30
                puntos1 = 0            

        elif opcion == 3:
          carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
          print("{} ha tirado el {}".format (jug1, carta1_p1))

        elif opcion == 4:
          termino = True
          ganador = jug2
        
        elif opcion == 5:
          termino = True
          ganador = jug2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(jug1+' se ha rendido')
          #fin de la partida

      elif puntos_truco == 2:
        print(jug1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Cantar retruco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        print('4. Rendirse')
        opcion = ValidarRTA (4)
        clear_terminal()

        if opcion == 1:
          puntos_truco, termino, ganador, quiero, fin_partida = self.CantarReTruco (jug1, jug2)
        
          if termino != True:
            clear_terminal()
            carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
            print("{} ha tirado el {}".format (jug1, carta1_p1))
          elif fin_partida == True:
              if ganador == jug1:
                puntos1 = 30
                puntos2 = 0
              elif ganador == jug2:
                puntos2 = 30
                puntos1 = 0

        elif opcion == 2:
          carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
          print("{} ha tirado el {}".format (jug1, carta1_p1))
          print('\n')

        elif opcion == 3:
          termino = True
          ganador = jug2
        
        elif opcion == 4:
          termino = True
          ganador = jug2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(jug1+' se ha rendido')
          #fin de la partida
        
      elif puntos_truco == 3:
        print(jug1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Cantar vale cuatro')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        print('4. Rendirse') 
        opcion = ValidarRTA (4)
        clear_terminal()

        if opcion == 1:
          puntos_truco, termino, ganador, quiero, fin_partida = self.CantarValeCuatro (jug1, jug2)
      
          if termino != True:
            clear_terminal()
            carta1_p1, cartasj1 = self.tirar_3(jug1, cartasj1)
            print("{} ha tirado el {}".format (jug1, carta1_p1))
            print('\n')

        elif opcion == 2:
          carta1_p1, cartasj1 = self.tirar_3(jug1, cartasj1)
          clear_terminal()
          print("{} ha tirado el {}".format (jug1, carta1_p1))
          print('\n')

        elif opcion == 3:
          termino = True
          ganador = jug2
        
        elif opcion == 4:
          termino = True
          ganador = jug2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(jug1+' se ha rendido')
          #fin de la partida
        
      elif puntos_truco == 4:
        print(jug1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Tirar carta')
        print('2. Irse al mazo') 
        print('3. Rendirse')
        opcion = ValidarRTA (3)
        clear_terminal()

        if opcion == 1:
          carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
          print("{} ha tirado el {}".format (jug1, carta1_p1))
          print('\n')

        elif opcion == 2:
          termino = True
          ganador = jug2
        
        elif opcion == 3:
          termino = True
          ganador = jug2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(jug1+' se ha rendido')
          #fin de la partida
    
    elif quiero == jug2:

      if puntos_truco == 1:
        print(jug1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Cantar envido')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        print('4. Rendirse')
        opcion = ValidarRTA (4)
        clear_terminal()

        if opcion == 1:
          puntos1, puntos2, fin_partida = self.envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
          hubo_envido = True

          if fin_partida == False:
            clear_terminal()
            print(jug1 + ', que desea hacer?')
            self.mostrar_cartas (cartasj1)
            print('1. Tirar carta')
            print('2. Irse al mazo')
            opcion = ValidarRTA (2)

            if opcion == 1:
              clear_terminal()
              carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
              print("{} ha tirado el {}".format (jug1, carta1_p1))
              print('\n')

            elif opcion == 2:
              termino = True
              ganador = jug2

          else:
            pass

        elif opcion == 2:
          carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
          print("{} ha tirado el {}".format (jug1, carta1_p1))
          print('\n')

        elif opcion == 3:
          termino = True
          ganador = jug2
        
        elif opcion == 4:
          termino = True
          ganador = jug2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(jug1+' se ha rendido')
          #fin de la partida
      
      else:
        print(jug1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Tirar carta')
        print('2. Irse al mazo')
        print('3. Rendirse')
        opcion = ValidarRTA (3)
        clear_terminal()

        if opcion == 1:
          carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
          print("{} ha tirado el {}".format (jug1, carta1_p1))
          print('\n')

        elif opcion == 2:
          termino = True
          ganador = jug2
        
        elif opcion == 3:
          termino = True
          ganador = jug2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(jug1+' se ha rendido')
          #fin de la partida
        
    return puntos1, puntos2, puntos_truco, termino, hubo_envido, carta1_p1, cartasj1, ganador, quiero, fin_partida


  def JugarPrimeraSinTanto (self, jug1, cartasj1, jug2, puntos_truco, quiero, puntos1, puntos2):                            #JUGAR PRIMERA SIN TANTO
    
    carta1_p1 = ''
    ganador = ''
    termino = False
    time.sleep(1) 

    if quiero == jug1 or quiero == '':

      if puntos_truco == 1:
        print(jug1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Cantar truco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        print('4. Rendirse')
        opcion = ValidarRTA (4)
        clear_terminal()

        if opcion == 1:
          puntos_truco, termino, ganador, quiero, fin_partida = self.CantarTruco (jug1, jug2)

          if termino != True:
            clear_terminal()
            carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
            print("{} ha tirado el {}".format (jug1, carta1_p1))
            print('\n')

          elif fin_partida == True:
              if ganador == jug1:
                puntos1 = 30
                puntos2 = 0
              elif ganador == jug2:
                puntos2 = 30
                puntos1 = 0

        elif opcion == 2:
          carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
          print("{} ha tirado el {}".format (jug1, carta1_p1))
          print('\n')

        elif opcion == 3:
          termino = True
          ganador = jug2
        
        elif opcion == 4:
          termino = True
          ganador = jug2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(jug1+' se ha rendido')
          #fin de la partida

      elif puntos_truco == 2:
        print(jug1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Cantar retruco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        print('4. Rendirse')
        opcion = ValidarRTA (4)
        clear_terminal()

        if opcion == 1:
          puntos_truco, termino, ganador, quiero, fin_partida = self.CantarReTruco (jug1, jug2)

          if termino != True:
            clear_terminal()
            carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
            print("{} ha tirado el {}".format (jug1, carta1_p1))
            print('\n')

          elif fin_partida == True:
            if ganador == jug1:
              puntos1 = 30
              puntos2 = 0
            elif ganador == jug2:
              puntos2 = 30
              puntos1 = 0

        elif opcion == 2:
          carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
          print("{} ha tirado el {}".format (jug1, carta1_p1))
          print('\n')

        elif opcion == 3:
          termino = True
          ganador = jug2
        
        elif opcion == 4:
          termino = True
          ganador = jug2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(jug1+' se ha rendido')
          #fin de la partida

      elif puntos_truco == 3:
        print(jug1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Cantar vale cuatro')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        print('4. Rendirse')
        opcion = ValidarRTA (4)
        clear_terminal()
        
        if opcion == 1:
          puntos_truco, termino, ganador, quiero, fin_partida = self.CantarValeCuatro (jug1, jug2)
            
          if termino != True:
            clear_terminal()
            carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
            print("{} ha tirado el {}".format (jug1, carta1_p1))
            print('\n')

          elif fin_partida == True:
            if ganador == jug1:
              puntos1 = 30
              puntos2 = 0
            elif ganador == jug2:
              puntos2 = 30
              puntos1 = 0

        elif opcion == 2:
          carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
          print("{} ha tirado el {}".format (jug1, carta1_p1))
          print('\n')

        elif opcion == 3:
          termino = True
          ganador = jug2
        
        elif opcion == 4:
          termino = True
          ganador = jug2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(jug1+' se ha rendido')
          #fin de la partida
      
      elif puntos_truco == 4:
        print(jug1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Tirar carta')
        print('2. Irse al mazo')
        print('3. Rendirse')
        opcion = ValidarRTA (3)
        clear_terminal()

        if opcion == 1:
          carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
          print("{} ha tirado el {}".format (jug1, carta1_p1))
          print('\n')

        elif opcion == 2:
          termino = True
          ganador = jug2
        
        elif opcion == 3:
          termino = True
          ganador = jug2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(jug1+' se ha rendido')
          #fin de la partida
    
    elif quiero == jug2:
      print(jug1 + ', que desea hacer?')
      self.mostrar_cartas (cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo')
      print('3. Rendirse')
      opcion = ValidarRTA (3)
      clear_terminal()

      if opcion == 1:
        carta1_p1, cartasj1 = self.tirar_3 (jug1, cartasj1)
        print("{} ha tirado el {}".format (jug1, carta1_p1))
        print('\n')

      elif opcion == 2:
        termino = True
        ganador = jug2
      
      elif opcion == 3:
        termino = True
        ganador = jug2
        puntos2 = 30
        puntos1 = 0
        fin_partida = True
        print(jug1+' se ha rendido')
        #fin de la partida

    return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, ganador, quiero

  def Jugar_Segunda(self,p1, puntos1, p2, puntos2, cartasj1, puntos_truco, quiero):                            #JUGAR SEGUNDA MANO
    
    termino= False
    carta1_p1 = ""
    ganador = ''

    if quiero == p1 or quiero == '':

      if puntos_truco == 1:
        print(p1 + ', que desea hacer?')
        self.mostrar_cartas(cartasj1)
        print('1. Cantar truco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        print('4. Rendirse')
        opcion = ValidarRTA (4)
        clear_terminal()
            
        if opcion == 1:
          puntos_truco, termino, ganador, quiero, fin_partida = self.CantarTruco (p1, p2)
        
          if termino != True:
            clear_terminal()
            carta1_p1, cartasj1 = self.tirar_2 (p1, cartasj1)
            print("{} ha tirado el {}".format (p1, carta1_p1))
            print('\n')

          elif fin_partida == True:
              if ganador == p1:
                puntos1 = 30
                puntos2 = 0
              elif ganador == p2:
                puntos2 = 30
                puntos1 = 0
  
        elif opcion == 2:
          carta1_p1, cartasj1 = self.tirar_2 (p1, cartasj1)
          print("{} ha tirado el {}".format (p1, carta1_p1))
          print('\n')

        elif opcion == 3:
          termino = True
          ganador = p2
        
        elif opcion == 4:
          termino = True
          ganador = p2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(p1 +' se ha rendido')
          #fin de la partida

      elif puntos_truco == 2:
        print(p1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Cantar retruco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = ValidarRTA (4)
        clear_terminal()

        if opcion == 1:
          puntos_truco, termino, ganador, quiero, fin_partida = self.CantarReTruco (p1, p2)
        
          if termino != True:
            clear_terminal()
            carta1_p1, cartasj1 = self.tirar_2 (p1, cartasj1)
            print("{} ha tirado el {}".format(p1,carta1_p1))
            print('\n')

          elif fin_partida == True:
              if ganador == p1:
                puntos1 = 30
                puntos2 = 0
              elif ganador == p2:
                puntos2 = 30
                puntos1 = 0

        elif opcion == 2:
          carta1_p1, cartasj1 = self.tirar_2 (p1, cartasj1)
          print("{} ha tirado el {}".format(p1, carta1_p1))
          print('\n')
  
        elif opcion == 3:
          termino = True
          ganador = p2
        
        elif opcion == 4:
          termino = True
          ganador = p2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(p1 +' se ha rendido')
          #fin de la partida

      elif puntos_truco == 3:
        print(p1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Cantar vale cuatro')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        print('4. Rendirse')
        opcion = ValidarRTA (4)
        clear_terminal()

        if opcion == 1:   
          puntos_truco, termino, ganador, quiero, fin_partida = self.CantarValeCuatro (p1, p2)
        
          if termino != True:
            clear_terminal()
            carta1_p1, cartasj1 = self.tirar_2 (p1, cartasj1)
            print("{} ha tirado el {}".format (p1, carta1_p1))
            print('\n')

          elif fin_partida == True:
            if ganador == p1:
              puntos1 = 30
              puntos2 = 0
            elif ganador == p2:
              puntos2 = 30
              puntos1 = 0

        elif opcion == 2:
          carta1_p1, cartasj1 = self.tirar_2 (p1, cartasj1)
          print("{} ha tirado el {}".format (p1, carta1_p1))
          print('\n')

        elif opcion == 3:
          termino = True
          ganador = p2
        
        elif opcion == 4:
          termino = True
          ganador = p2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(p1 +' se ha rendido')
          #fin de la partida

      elif puntos_truco == 4:
        carta1_p1, cartasj1 = self.tirar_2 (p1, cartasj1)
        print("{} ha tirado el {}".format (p1, carta1_p1))
        print('\n')
    
    elif quiero == p2:
      print(p1 + ', que desea hacer?')
      self.mostrar_cartas (cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo')
      print('3. Rendirse')
      opcion = ValidarRTA (3)
      clear_terminal()

      if opcion == 1:
        carta1_p1, cartasj1 = self.tirar_2 (p1, cartasj1)
        print("{} ha tirado el {}".format (p1, carta1_p1))
        print('\n')

      elif opcion == 2:
        termino = True
        ganador = p2
      
      elif opcion == 3:
        termino = True
        ganador = p2
        puntos2 = 30
        puntos1 = 0
        fin_partida = True
        print(p1 +' se ha rendido')
        #fin de la partida
      
    return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, ganador, quiero 

  def Jugar_Tercera (self,p1, puntos1, p2, puntos2, cartasj1, puntos_truco, quiero):                #JUGAR TERCER MANO
    
    termino = False
    carta1_p1 = ""
    ganador = ''

    if quiero == p1 or quiero == '':

      if puntos_truco == 1:
        print(p1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Cantar truco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        print('4. Rendirse')
        opcion = ValidarRTA (4)
        clear_terminal()

        if opcion == 1:
          puntos_truco, termino, ganador, quiero, fin_partida = self.CantarTruco (p1, p2)
        
          if termino != True:
            clear_terminal()
            carta1_p1, cartasj1 = self.tirar_1 (p1, cartasj1)
            print("{} ha tirado el {}".format (p1, carta1_p1))
            print('\n')

          elif fin_partida == True:
              if ganador == p1:
                puntos1 = 30
                puntos2 = 0
              elif ganador == p2:
                puntos2 = 30
                puntos1 = 0

        elif opcion == 2:
          carta1_p1, cartasj1 = self.tirar_1 (p1, cartasj1)
          print("{} ha tirado el {}".format (p1, carta1_p1))
          print('\n')
          
        elif opcion == 3:
          termino = True
          ganador = p2
        
        elif opcion == 4:
          termino = True
          ganador = p2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(p1 +' se ha rendido')
          #fin de la partida

      elif puntos_truco == 2:
        print(p1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Cantar retruco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        print('4. Rendirse')
        opcion = ValidarRTA (4)
        clear_terminal()

        if opcion == 1:
          puntos_truco, termino, ganador, quiero, fin_partida = self.CantarReTruco (p1, p2)
        
          if termino != True:
            clear_terminal()
            carta1_p1, cartasj1 = self.tirar_1 (p1, cartasj1)
            print("{} ha tirado el {}".format (p1, carta1_p1))
            print('\n')

          elif fin_partida == True:
              if ganador == p1:
                puntos1 = 30
                puntos2 = 0
              elif ganador == p2:
                puntos2 = 30
                puntos1 = 0

        elif opcion == 2:
          carta1_p1, cartasj1 = self.tirar_1 (p1, cartasj1)
          print("{} ha tirado el {}".format (p1, carta1_p1))
          print('\n')

        elif opcion == 3:
          termino = True
          ganador = p2
        
        elif opcion == 4:
          termino = True
          ganador = p2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(p1 +' se ha rendido')
          #fin de la partida

      elif puntos_truco == 3:
        print(p1 + ', que desea hacer?')
        self.mostrar_cartas (cartasj1)
        print('1. Cantar vale cuatro')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        print('4. Rendirse')
        opcion = ValidarRTA (4)
        clear_terminal()

        if opcion == 1:
          puntos_truco, termino, ganador, quiero, fin_partida = self.CantarValeCuatro (p1, p2)
        
          if termino != True:
            clear_terminal()
            carta1_p1, cartasj1 = self.tirar_1 (p1, cartasj1)
            print("{} ha tirado el {}".format (p1, carta1_p1))
            print('\n')

          elif fin_partida == True:
            if ganador == p1:
              puntos1 = 30
              puntos2 = 0
            elif ganador == p2:
              puntos2 = 30
              puntos1 = 0

        elif opcion == 2:
          carta1_p1, cartasj1 = self.tirar_1 (p1, cartasj1)
          print("{} ha tirado el {}".format (p1, carta1_p1))
          print('\n')

        elif opcion == 3:
          termino = True
          ganador = p2
        
        elif opcion == 4:
          termino = True
          ganador = p2
          puntos2 = 30
          puntos1 = 0
          fin_partida = True
          print(p1 +' se ha rendido')
          #fin de la partida

      elif puntos_truco == 4:
        clear_terminal()
        carta1_p1, cartasj1 = self.tirar_1 (p1, cartasj1)
        print("{} ha tirado el {}".format (p1, carta1_p1))
        print('\n')
    
    elif quiero == p2:
      print(p1 + ', que desea hacer?')
      self.mostrar_cartas (cartasj1)
      print('1. Tirar carta')
      print('2. Irse al mazo')
      print('3. Rendirse')
      opcion = ValidarRTA (3)
      clear_terminal()

      if opcion == 1:
        carta1_p1, cartasj1 = self.tirar_1(p1, cartasj1)
        print("{} ha tirado el {}".format(p1, carta1_p1))
        print('\n')

      elif opcion == 2:
        termino = True
        ganador = p2
      
      elif opcion == 3:
        termino = True
        ganador = p2
        puntos2 = 30
        puntos1 = 0
        fin_partida = True
        print(p1 +' se ha rendido')
        #fin de la partida
      
    return puntos1, puntos2, puntos_truco, termino, carta1_p1, cartasj1, ganador, quiero 

  def CantarTruco (self,p1, p2): 

    termino = False
    fin_partida = False
    ganador = ''

    print(p1, 'ha cantado TRUCO!')
    print(p2 + ', que desea hacer?')
    print('1. Retruco')
    print('2. Quiero')
    print('3. No quiero')
    print('4. Rendirse')
    opcion = ValidarRTA (4)

    if opcion == 1:
      clear_terminal()
      puntos_truco, termino, ganador, quiero, fin_partida = self.CantarReTruco (p2, p1)
    
    elif opcion == 2:
      clear_terminal()
      print(p2 + ', ha dicho QUIERO')
      puntos_truco = 2
      quiero = p2
            
    elif opcion == 3:
      clear_terminal()
      print(p2 + ', ha dicho NO QUIERO')
      puntos_truco = 1
      termino = True
      ganador = p1
      quiero = 'no'
    
    elif opcion == 4:
      clear_terminal()
      print(p2 + ' se ha rendido')
      puntos_truco = 0
      termino = True
      fin_partida = True
      ganador = p1
      quiero = 'no'

    
    return puntos_truco, termino, ganador, quiero, fin_partida

  def CantarReTruco (self,p1, p2):

    termino = False
    fin_partida = False
    ganador = ''

    print(p1, 'ha cantado RE TRUCO!')
    print(p2 + ', que desea hacer?')
    print('1. Vale cuatro')
    print('2. Quiero')
    print('3. No quiero')
    print('4. Rendirse')
    opcion = ValidarRTA (4)

    if opcion == 1:
      clear_terminal()
      puntos_truco, termino, ganador, quiero, fin_partida = self.CantarValeCuatro (p2, p1)
    
    elif opcion == 2: 
      clear_terminal()
      print(p2 + ', ha dicho QUIERO')
      puntos_truco = 3
      quiero = p2

    elif opcion == 3:
      clear_terminal()
      print(p2 + ', ha dicho NO QUIERO')
      puntos_truco = 2
      termino = True
      ganador = p1
      quiero = 'no'
    
    elif opcion == 4:
      clear_terminal()
      print(p2 + ' se ha rendido')
      puntos_truco = 0
      termino = True
      fin_partida = True
      ganador = p1
      quiero = 'no'

    return puntos_truco, termino, ganador, quiero, fin_partida

  def CantarValeCuatro (self,p1, p2):
    
    termino = False
    fin_partida = False
    ganador = ''

    print(p1, 'ha cantado QUIERO VALE CUATRO!')
    print(p2 + ', que desea hacer?')
    print('1. Quiero')
    print('2. No quiero')
    print('3. Rendirse')
    opcion = ValidarRTA (3)

    if opcion == 1:
      clear_terminal()
      print(p2 + ', ha dicho QUIERO')
      puntos_truco = 4
      quiero = p2
    
    elif opcion == 2:
      clear_terminal()
      print(p2 + ', ha dicho NO QUIERO')
      puntos_truco = 3
      termino = True
      ganador = p1
      quiero = 'no'
    
    elif opcion == 3:
      clear_terminal()
      print(p2 + ' se ha rendido')
      puntos_truco = 0
      termino = True
      fin_partida = True
      ganador = p1
      quiero = 'no'

    return puntos_truco, termino, ganador, quiero, fin_partida

  def envido (self,jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano):
    clear_terminal()
    print('Que desea cantar?')
    print('1. Envido')
    print('2. Real envido')
    print('3. Falta envido')
    opcion = ValidarRTA (3)

    if opcion == 1:          
      puntos_tanto = 2
      puntos_al_no = 1
      clear_terminal()
      print(jug1,'ha cantado ENVIDO')
      print(jug2 + ', que desea hacer?')
      self.mostrar_cartas (cartasj2)
      print('1. Envido')
      print('2. Real envido')
      print('3. Falta envido')
      print('4. Quiero')
      print('5. No quiero')
      opcion = ValidarRTA (5)

      clear_terminal()

      if opcion == 1:             
        puntos_al_no = puntos_tanto
        puntos_tanto = 4
        clear_terminal()
        print(jug2, 'ha cantado ENVIDO')
        self.mostrar_cartas (cartasj2)
        print(jug1 + ', que desea hacer?')
        print('1. Real envido')
        print('2. Falta envido')
        print('3. Quiero')
        print('4. No quiero')
        opcion = ValidarRTA (4)

        clear_terminal()
        if opcion == 1:            
          puntos_al_no = puntos_tanto
          puntos_tanto = 7
          puntos1, puntos2 = self.real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano)
          
        elif opcion == 2:                 
          puntos_al_no=4
          puntos1, puntos2 = self.falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
        
        elif opcion == 3:                 
          print(jug1 + ' ha dicho QUIERO')
          time.sleep(2)
          puntos1, puntos2 = self.sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)

        elif opcion == 4:                 
          print(jug1 + ' ha dicho NO QUIERO.', jug2, 'suma', puntos_al_no, 'puntos')
          puntos2 += puntos_al_no
          time.sleep(2)
          
      
      elif opcion == 2:                  
        puntos_al_no = puntos_tanto
        puntos_tanto=5
        clear_terminal()
        puntos1, puntos2 = self.real_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_tanto, puntos_al_no, mano)
        
      elif opcion == 3:          
        puntos_al_no=2
        clear_terminal()
        puntos1, puntos2 = self.falta_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_al_no, mano)
      
      elif opcion == 4: 
        clear_terminal()              
        print(jug2 + ' ha dicho QUIERO')
        puntos1, puntos2 = self.sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)
        time.sleep(2)

      elif opcion == 5:  
        clear_terminal()                
        print(jug2 + ' ha dicho NO QUIERO.',jug1,'suma',puntos_al_no,'puntos')
        puntos1 += puntos_al_no
        time.sleep(2)
        
      
    elif opcion == 2:                    
      puntos_al_no = 1
      puntos_tanto = 3
      puntos1, puntos2 = self.real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano)
    
    elif opcion == 3:
      puntos_al_no = 1
      puntos1, puntos2 = self.falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
    
    fin_partida = self.chequearganador(puntos1, puntos2)

    return puntos1, puntos2, fin_partida

  def real_envido (self,jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano):
    
    print(jug1, 'ha cantado REAL ENVIDO')
    self.mostrar_cartas (cartasj2)
    print(jug2 + ', que desea hacer?')
    print('1. Falta envido')
    print('2. Quiero')
    print('3. No quiero')
    opcion = ValidarRTA (3)
    clear_terminal()

    if opcion == 1:                   
      puntos_al_no=puntos_tanto
      puntos1, puntos2 = self.falta_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_al_no, mano)
      
    elif opcion == 2:                    
      print(jug2 + ' ha dicho QUIERO')
      time.sleep(2)
      puntos1, puntos2 = self.sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)

    elif opcion == 3:                
      print(jug2 + ' ha dicho NO QUIERO.', jug1, 'suma', puntos_al_no, 'puntos')
      puntos1 += puntos_al_no
      time.sleep(2)
      
    return puntos1, puntos2

  def falta_envido (self,jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano):
    
    puntos_tanto = self.contar_puntos_falta (puntos1,puntos2)

    print(jug1,'ha cantado FALTA ENVIDO!')
    self.mostrar_cartas (cartasj2)
    print(jug2 + ', que desea hacer?')
    print('1. Quiero')
    print('2. No quiero')
    opcion = ValidarRTA (2)
    clear_terminal()

    if opcion == 1:                        
      print(jug2 + ' ha dicho QUIERO')
      time.sleep(2)
      puntos1, puntos2 = self.sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)

    if opcion == 2:                        
      print(jug2 + ' ha dicho NO QUIERO.', jug1, 'suma', puntos_al_no, 'puntos')
      puntos1 += puntos_al_no
      time.sleep(2)
    
    
    return puntos1, puntos2

  def contar_tanto(self,cartas):
      
      tanto_01 = 0
      tanto_02 = 0
      tanto_12 = 0
      n=0

      if cartas[1].palo == cartas[2].palo:
        tanto_12 = 20 + (int(cartas[1].jerarquia_envido) + int(cartas[2].jerarquia_envido))
        n += 1

      if cartas[0].palo == cartas[1].palo:
        tanto_01 = 20 + (int(cartas[1].jerarquia_envido) + int(cartas[0].jerarquia_envido))
        n += 1
          
      if cartas[0].palo == cartas[2].palo:
        tanto_02 = 20 + (int(cartas[0].jerarquia_envido) + int(cartas[2].jerarquia_envido))
        n += 1
          
      if n >= 1:
        tanto = max (tanto_01, tanto_02, tanto_12)

      if n == 0:
        tanto = (max (cartas[0].jerarquia_envido, cartas[1].jerarquia_envido, cartas[2].jerarquia_envido))
      
      return tanto

  def contar_los_tantos (self,cartasjug1, cartasjug2):
    
    tanto1 = self.contar_tanto(cartasjug1)
    tanto2 = self.contar_tanto(cartasjug2)
    
    return tanto1, tanto2

  def contar_puntos_falta (self,puntos1,puntos2):
    
    if puntos2 < puntos1:
      puntos_tanto = 30 - puntos1
    elif puntos2 > puntos1:
      puntos_tanto = 30 - puntos2
    else:
      puntos_tanto = 30 - puntos1
    
    return puntos_tanto

  def sumar_puntos_envido (self,jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano):
    
    tanto1, tanto2 = self.contar_los_tantos (cartasj1, cartasj2) 
    clear_terminal()

    if jug1 == mano:
      print(jug1 + ':',tanto1)

      if tanto2>tanto1:
        print(jug2 + ':', tanto2, 'son mejores!!')
        puntos2 += puntos_tanto
        print(jug2, 'suma', puntos_tanto, 'puntos de tanto')

      else:
        print(jug2 + ': son buenas.')
        puntos1 += puntos_tanto
        print(jug1, 'suma', puntos_tanto, 'puntos de tanto')

    elif jug2 == mano:
      print(jug2 + ':',tanto2)

      if tanto1 > tanto2:
        print(jug1 + ':', tanto1, 'son mejores!!')
        puntos1 += puntos_tanto
        print(jug1, 'suma', puntos_tanto, 'puntos')

      else:
        print(jug1 + ': son buenas.')
        puntos2 += puntos_tanto
        print(jug2, 'suma', puntos_tanto, 'puntos')

    time.sleep(4)
    return puntos1, puntos2

  def chequearganador(self,puntos1, puntos2):
    
    fin_partida = False

    if puntos1 >= 30:
      fin_partida = True
    
    if puntos2 >= 30:
      fin_partida = True
    
    return fin_partida

  def mostrar_cartas (self,lista):
    cartas = "sus cartas son: "
    for i in lista:
      cartas += (str(i) + ', ')
    print(cartas)

  def tirar_3 (self,jugador, cartas):
    lista = []
    print("" + jugador + ", que carta desea tirar: ")
    print("1. " + str(cartas[0]))
    print("2. " + str(cartas[1]))
    print("3. " + str(cartas[2]))
    op = ValidarRTA (3)
    clear_terminal()

    for j in cartas:
      if j != cartas[op-1]:
        lista.append(j)

    return cartas[op-1], lista

  def tirar_2(self,jugador,cartas):
    
    lista = []
    
    print("" + jugador + ", que carta desea tirar: ")
    print("1. " + str(cartas[0]))
    print("2. " + str(cartas[1]))
    op = ValidarRTA (2)
    clear_terminal()
    
    for j in cartas:
      if j != cartas [op-1]:
        lista.append(j)
    
    return cartas[op-1],lista

  def tirar_1 (self,jugador, cartas):
    
    print(jugador + ", le queda una sola carta, presione 1 para tirarla: ")
    print("1." + str(cartas[0]))
    opcion = ValidarRTA (1)
    clear_terminal()

    return cartas[0], []
 
  def Jugar(self,p1,p2,p1_usuario,p2_usuario,lista,nombre1, apellido1, dni1, mail1, clave1, partidas_jug1, partidas_gan1, usuario1,nombre2, apellido2, dni2, mail2, clave2, partidas_jug2, partidas_gan2, usuario2):  
    ronda = 0

    jugador1 = UsuarioRegistrado (nombre1, apellido1, dni1, mail1, clave1, partidas_jug1, partidas_gan1, usuario1)
    jugador2 = UsuarioRegistrado (nombre2, apellido2, dni2, mail2, clave2, partidas_jug2, partidas_gan2, usuario2)

    puntos1 = 0
    puntos2 = 0

    clear_terminal()
    print("Se ha iniciado una nueva partida entre: " + p1 + " y " + p2)
    time.sleep(2)

    while puntos1 < 30 and puntos2 < 30:
      
      mazo=Mazo()       #Se crea el mazo

      cartas_en_juego = mazo.repartir()      #Se reparte el mazo
      ronda += 1
      mano, puntos_mano, pie, puntos_pie = mazo.quien_es_mano(ronda, p1, puntos1, p2, puntos2)        #Se determina que jugador es mano

      cartasmano = [cartas_en_juego[0], cartas_en_juego[2], cartas_en_juego[4]]         #Se dan las cartas al mano y al pie
      cartas_pie = [cartas_en_juego[1], cartas_en_juego[3], cartas_en_juego[5]]

      clear_terminal()
      print('Comienza la ronda '+str(ronda)+'!')
      print('Recuerden que tienen 6 segundos para ver sus cartas, comienza',mano)
      time.sleep(4)
      clear_terminal()
      time.sleep(1)
      print(mano, 'es MANO.')
      self.mostrar_cartas(cartasmano)
      time.sleep(5)
      clear_terminal()
      time.sleep(1)
      print(pie, 'es PIE.')
      self.mostrar_cartas(cartas_pie)
      time.sleep(5)
      clear_terminal()
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

        puntos_mano, puntos_pie, puntos_truco, termino, hubo_envido, carta1_mano, cartas_mano, ganador, quiero, fin_partida  = self.JugarPrimera (mano, puntos_mano, cartasmano, pie, puntos_pie, cartas_pie, puntos_truco, quiero, mano)
        
        if termino == True and fin_partida == False:
          if quiero == '':
            puntos_truco = 2
          break
      
        if fin_partida == True:
          break
        
        if hubo_envido == True:
          puntos_mano, puntos_pie, puntos_truco, termino, carta1_pie, cartas_pie, ganador, quiero  = self.JugarPrimeraSinTanto (pie, cartas_pie, mano, puntos_truco, quiero, puntos_mano, puntos_pie)
      
          if termino == True: 
            break

        elif hubo_envido == False:
          puntos_pie, puntos_mano, puntos_truco, termino, hubo_envido, carta1_pie, cartas_pie, ganador, quiero, fin_partida  = self.JugarPrimera (pie, puntos_pie, cartas_pie, mano, puntos_mano, cartasmano, puntos_truco, quiero, mano)

          if termino == True:
            break

          if fin_partida == True:
            break

        clear_terminal()
        if carta1_pie > carta1_mano:
          ganador1 = pie
          print(pie, "ha ganado la mano")
          manos_pie += 1 
          time.sleep(3)

        elif carta1_mano > carta1_pie:
          ganador1 = mano 
          print(mano, "ha ganado la mano")
          manos_mano += 1

        elif carta1_mano == carta1_pie:
          parda1=True
          print('Se ha pardado')
        
        time.sleep(3)

        #Segunda Mano

        que_mano_es += 1

        if ganador1 == pie: #el pie gano primera arranca 2 el
          
          puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pie, ganador, quiero = self.Jugar_Segunda (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)

          if termino == True: 
            break

          puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador, quiero = self.Jugar_Segunda (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
          
          if termino == True: 
            break

        elif ganador1 == mano: #la mano gano primera arranca la 2 el
          
          puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador, quiero = self.Jugar_Segunda (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
          
          if termino == True: 
            break

          puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pie, ganador, quiero = self.Jugar_Segunda (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
          
          if termino == True: 
            break

        elif  parda1 == True: #Se juega la parda
          
          puntos_mano, puntos_pie, puntos_truco, termino, carta2_mano, cartas_mano, ganador, quiero = self.Jugar_Segunda (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
          
          if termino == True: 
            break
          
          puntos_pie, puntos_mano, puntos_truco, termino, carta2_pie, cartas_pie, ganador, quiero = self.Jugar_Segunda (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
          
          if termino == True: 
            break
          clear_terminal()
          if carta2_mano == carta2_pie: #Se pardo segunda
            parda2 = True
            print("Se ha pardado")

          elif carta2_mano > carta2_pie: #gano la mano
            ganador = mano
            break
          
          elif carta2_pie > carta2_mano: #gano el pie
            ganador = pie
            break 
          time.sleep(3)

        clear_terminal()  
        if carta2_mano > carta2_pie: #mano gana segunda
          ganador2 = mano
          print(mano, "ha ganado la mano")
          manos_mano += 1

        elif carta2_pie > carta2_mano: #pie gana segunda
          ganador2 = pie
          manos_pie += 1
          print(pie, "ha ganado la mano")

        elif carta2_pie == carta2_mano and parda1 == False: #se parda 2 y no esta pardada primera
          if ganador1 == pie:
            ganador = pie
            break

          elif ganador1 == mano:
            ganador = mano
        
        time.sleep(3)

        if manos_pie == 2:
          ganador = pie
          break

        if manos_mano == 2:
          ganador = mano
          break 

        # Tercera Mano 
        
        que_mano_es += 1

        if ganador2 == pie:                 #pie gana 2 arranca en 3
        
          puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pie, ganador, quiero = self.Jugar_Tercera (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)

          if termino == True: 
            break

          puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador, quiero = self.Jugar_Tercera (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
          
          if termino == True: 
            break

        elif ganador2 == mano: #mano gano 2 arranca en 3
          puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador, quiero = self.Jugar_Tercera (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
          
          if termino == True: 
            break

          puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pie, ganador, quiero = self.Jugar_Tercera (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
          
          if termino == True: 
            break
          
        elif  parda2 == True and parda1 == True: #Se juega la parda
          puntos_mano, puntos_pie, puntos_truco, termino, carta3_mano, cartas_mano, ganador, quiero = self.Jugar_Tercera (mano, puntos_mano, pie, puntos_pie, cartas_mano, puntos_truco, quiero)
          
          if termino == True: 
            break
          
          puntos_pie, puntos_mano, puntos_truco, termino, carta3_pie, cartas_pie, ganador, quiero = self.Jugar_Tercera (pie, puntos_pie, mano, puntos_mano, cartas_pie, puntos_truco, quiero)
          
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
      clear_terminal()
      if fin_partida == False:
        if ganador == mano:
          puntos_mano += puntos_truco
          print("Ha ganado: ", mano, " se le suman ", puntos_truco, " puntos")
          
        elif ganador == pie:
          puntos_pie += puntos_truco
          print("Ha ganado: ", pie, " se le suman ", puntos_truco, " puntos")
      time.sleep(3)

      if p1 == mano:
        puntos1 = puntos_mano
        puntos2 = puntos_pie
      elif p2 == mano:
        puntos2 = puntos_mano
        puntos1 = puntos_pie

      clear_terminal()
      print('Puntos de '+ p1 + ": " + str(puntos1))
      print('Puntos de ' + p2 + ": " + str(puntos2))
      print('------------------------------------------------------------------------------\n\n')

      time.sleep(5)

      fin_partida = self.chequearganador(puntos1, puntos2)

      if fin_partida == True:
        break
    

    if puntos1 < puntos2:
      ganador_final = p2
      perdedor_final = p1
      resultado = str(puntos2) + "-" + str(puntos1)
      clear_terminal()
      print('FELICITACIONES ' + p2 + ', USTED HA GANAD0!')
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
      clear_terminal()
      print('FELICITACIONES ' + p1 + ', USTED HA GANAD0!')
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
    
    time.sleep(4)
    clear_terminal()

    return ganador_final, perdedor_final, resultado, lista
    