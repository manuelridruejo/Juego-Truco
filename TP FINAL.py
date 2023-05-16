########################################################## CLASES ########################################################################





import csv
from random import shuffle, randint
from datetime import date
 
PALOS = ["Oro", "Espada", "Copa", "Basto"] # Variable global en mayúsculas Guía PEP-8
NUMEROS = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
JERARQUIAS = {
  ("Oro", 1): 7,
  ("Oro", 2): 8,
  ("Oro", 3): 9,
  ("Oro", 4): 0,
  ("Oro", 5): 1,
  ("Oro", 6): 2,
  ("Oro", 7): 10,
  ("Oro", 10): 4,
  ("Oro", 11): 5,
  ("Oro", 12): 6,
  ("Espada", 1): 13,
  ("Espada", 2): 8,
  ("Espada", 3): 9,
  ("Espada", 4): 0,
  ("Espada", 5): 1,
  ("Espada", 6): 2,
  ("Espada", 7): 11,
  ("Espada", 10): 4,
  ("Espada", 11): 5,
  ("Espada", 12): 6,
  ("Basto", 1): 12,
  ("Basto", 2): 8,
  ("Basto", 3): 9,
  ("Basto", 4): 0,
  ("Basto", 5): 1,
  ("Basto", 6): 2,
  ("Basto", 7): 3,
  ("Basto", 10): 4,
  ("Basto", 11): 5,
  ("Basto", 12): 6,
  ("Copa", 1): 7,
  ("Copa", 2): 8,
  ("Copa", 3): 9,
  ("Copa", 4): 0,
  ("Copa", 5): 1,
  ("Copa", 6): 2,
  ("Copa", 7): 3,
  ("Copa", 10): 4,
  ("Copa", 11): 5,
  ("Copa", 12): 6
}

JERARQUIAS_ENVIDO = {
  ("Oro", 1): 1,
  ("Oro", 2): 2,
  ("Oro", 3): 3,
  ("Oro", 4): 4,
  ("Oro", 5): 5,
  ("Oro", 6): 6,
  ("Oro", 7): 7,
  ("Oro", 10): 0,
  ("Oro", 11): 0,
  ("Oro", 12): 0,
  ("Espada", 1): 1,
  ("Espada", 2): 2,
  ("Espada", 3): 3,
  ("Espada", 4): 4,
  ("Espada", 5): 5,
  ("Espada", 6): 6,
  ("Espada", 7): 7,
  ("Espada", 10): 0,
  ("Espada", 11): 0,
  ("Espada", 12): 0,
  ("Basto", 1): 1,
  ("Basto", 2): 2,
  ("Basto", 3): 3,
  ("Basto", 4): 4,
  ("Basto", 5): 5,
  ("Basto", 6): 6,
  ("Basto", 7): 7,
  ("Basto", 10): 0,
  ("Basto", 11): 0,
  ("Basto", 12): 0,
  ("Copa", 1): 1,
  ("Copa", 2): 2,
  ("Copa", 3): 3,
  ("Copa", 4): 4,
  ("Copa", 5): 5,
  ("Copa", 6): 6,
  ("Copa", 7): 7,
  ("Copa", 10): 0,
  ("Copa", 11): 0,
  ("Copa", 12): 0
}


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

  
class Jugador():

  def __init__ (self, nombre : str, apellido : str, DNI: int, mail: str, clave: str, partidas_jugadas: int, partidas_ganadas: int, usuario: str):
    self.nombre = nombre
    self.apellido = apellido
    self.DNI = DNI
    self.mail = mail
    self.clave = clave
    self.partidas_jugadas = partidas_jugadas
    self.partidas_ganadas = partidas_ganadas
    self.usuario = usuario
  
  def modificar(self):
    print("Usted ha decidido modificar su usuario. Que atributo desea modificar?")
    print("\n1. Nombre")
    print("\n2. Apellido")
    print("\n3. DNI")
    print("\n4. Mail")
    print('\n5. clave')
    print('\n6. usuario')

    opcion = ValidarRTA (6)

    if opcion == 1:
      print("Usted ha elegido modificar su nombre")
      nombre_nuevo = input("Ingrese la informacion nueva")
      self.nombre = nombre_nuevo
      print('\nNombre cambiado con exito.')

    elif opcion == 2:
      print("Usted ha elegido modificar su apellido.")
      apellido_nuevo = input("Ingrese la informacion nueva.")
      self.apellido = apellido_nuevo
      print('\nApellido cambiado con exito.')

    elif opcion == 3:
      print("Usted ha elegido modificar su DNI.")
      dni_nuevo = PedirDNI()
      self.dni = dni_nuevo
      print('\nDNI cambiado con exito.')
      
    elif opcion == 4:
      print("Usted ha elegido modificar su mail.")
      mail_nuevo = PedirMail()
      self.mail = mail_nuevo
      print('\nMail cambiado con exito.')
    
    elif opcion == 5:
      print("Usted ha solicitado modificar su clave")
      nueva_clave =  input("Ingrese su nueva clave: ")
      confirmar_clave = input("Por favor confirme su nueva clave: ")

      while nueva_clave != confirmar_clave:
        print("Las claves no coinciden intente de nuevo: ")
        nueva_clave =  input("Ingrese su nueva clave: ")
        confirmar_clave = input("Por favor confirme su nueva clave: ")

      self.clave = nueva_clave
      print('\nContraseña cambiada con exito.')
    
    elif opcion == 6:


class Jugadores():

  def __init__ (self, lista_jugadores) -> None:
    self.lista_jugadores = lista_jugadores

  def agregar_jugadores (self,jugador):
    self.lista_jugadores.append (jugador.nombre_usuario)


class Partida():

    def __init__ (self, resultado : str, jugadores, lista_partidas):
        self.fecha = date.today()
        self.codigo_partida = self.asignar_codigo (lista_partidas)
        self.resultado = resultado
        self.jugadores = jugadores

    def asignar_codigo (self, lista_partidas):
        return max(lista_partidas) + 1

    def __str__ (self):
        return "La partida {} entre {} y {} , {} y ocurrio el dia: {}".format(self.codigo_partida, self.jugadores[0], self.jugadores[1], self.resultado, self.fecha)
    

class Partidas():
    def __init__ (self) -> None:
      self.lista_partidas = []
    def agrega_partida (self, ):
       self.lista_partidas.append (Partida.codigo_partida)






############################################################## TRUCO ######################################################################







def CantarTruco (p1, p2): 

  termino = False
  ganador = ''

  print('\n' + p1, 'ha cantado TRUCO!')
  print('\n' + p2 + ', que desea hacer?')
  print('1. Retruco')
  print('2. Quiero')
  print('3. No quiero')
  opcion = ValidarRTA (3)

  if opcion == 1:
    puntos_truco, termino, ganador, quiero = CantarReTruco (p2, p1)
  
  elif opcion == 2:
    print('\n' + p2 + ', ha dicho QUIERO')
    puntos_truco = 2
    quiero = p2
          
  elif opcion == 3:
    print('\n' + p2 + ', ha dicho NO QUIERO')
    puntos_truco = 1
    termino = True
    ganador = p1
    quiero = 'no'
  
  return puntos_truco, termino, ganador, quiero

def CantarReTruco (p1, p2):

  termino = False
  ganador = ''

  print('\n' + p1, 'ha cantado RE TRUCO!')
  print('\n' + p2 + ', que desea hacer?')
  print('1. Vale cuatro')
  print('2. Quiero')
  print('3. No quiero')
  opcion = ValidarRTA (3)

  if opcion == 1:
    puntos_truco, termino, ganador, quiero = CantarValeCuatro (p2, p1)
  
  elif opcion == 2: 
    print('\n' + p2 + ', ha dicho QUIERO')
    puntos_truco = 3
    quiero = p2

  elif opcion == 3:
    print('\n' + p2 + ', ha dicho NO QUIERO')
    puntos_truco = 2
    termino = True
    ganador = p1
    quiero = 'no'

  return puntos_truco, termino, ganador, quiero

def CantarValeCuatro (p1, p2):
  
  termino = False
  ganador = ''

  print('\n' + p1, 'ha cantado QUIERO VALE CUATRO!')
  print('\n' + p2 + ', que desea hacer?')
  print('1. Quiero')
  print('2. No quiero')
  opcion = ValidarRTA (2)

  if opcion == 1:
    print('\n' + p2 + ', ha dicho QUIERO')
    puntos_truco = 4
    quiero = p2
  
  elif opcion == 2:
    print('\n' + p2 + ', ha dicho NO QUIERO')
    puntos_truco = 3
    termino = True
    ganador = p1
    quiero = 'no'

  return puntos_truco, termino, ganador, quiero







########################################################### ENVIDO ######################################################################







def real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano):
  
  print('\n' + jug1, 'ha cantado REAL ENVIDO')
  mostrar_cartas (cartasj2)
  print('\n' + jug2 + ', que desea hacer?')
  print('1. Falta envido')
  print('2. Quiero')
  print('3. No quiero')
  opcion = ValidarRTA (3)

  if opcion == 1:                   
    puntos_al_no=puntos_tanto
    puntos1, puntos2 = falta_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_al_no, mano)
    
  elif opcion == 2:                    
    print('\n' + jug2 + ' ha dicho QUIERO')
    puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
    
  elif opcion == 3:                
    print('\n' + jug2 + ' ha dicho NO QUIERO.', jug1, 'suma', puntos_al_no, 'puntos')
    puntos1 += puntos_al_no
    
  return puntos1, puntos2


def falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano):
  
  puntos_tanto = contar_puntos_falta (puntos1,puntos2)

  print('\n'+jug1,'ha cantado FALTA ENVIDO!')
  mostrar_cartas (cartasj2)
  print('\n' + jug2 + ', que desea hacer?')
  print('1. Quiero')
  print('2. No quiero')
  opcion = ValidarRTA (2)

  if opcion == 1:                         
    print('\n' + jug2 + ' ha dicho QUIERO')
    puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)
          
  if opcion == 2:                         
    print('\n' + jug2 + ' ha dicho NO QUIERO.', jug1, 'suma', puntos_al_no, 'puntos')
    puntos1 += puntos_al_no
   
  
  return puntos1, puntos2


def contar_tanto(cartas):
    
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
        
    if n >= 1:
      tanto = max (tanto_01, tanto_02, tanto_12)

    if n == 0:
      tanto = (max (cartas[0].jerarquia_envido, cartas[1].jerarquia_envido, cartas[2].jerarquia_envido))
    
    return tanto


def contar_los_tantos (cartasjug1, cartasjug2):
  
  tanto1 = contar_tanto(cartasjug1)
  tanto2 = contar_tanto(cartasjug2)
  
  return tanto1, tanto2


def contar_puntos_falta (puntos1,puntos2):
  
  if puntos2 < puntos1:
    puntos_tanto = 30 - puntos1
  elif puntos2 > puntos1:
    puntos_tanto = 30 - puntos2
  else:
    puntos_tanto = 30 - puntos1
  
  return puntos_tanto


def sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano):
  
  tanto1, tanto2 = contar_los_tantos (cartasj1, cartasj2) 

  if jug1 == mano:
    print('\n' + jug1 + ':',tanto1)

    if tanto2>tanto1:
      print(jug2 + ':', tanto2, 'son mejores!!')
      puntos2 += puntos_tanto
      print(jug2, 'suma', puntos_tanto, 'puntos de tanto')

    else:
      print(jug2 + ': son buenas.')
      puntos1 += puntos_tanto
      print(jug1, 'suma', puntos_tanto, 'puntos de tanto')

  elif jug2 == mano:
    print('\n' + jug2 + ':',tanto2)

    if tanto1 > tanto2:
      print(jug1 + ':', tanto1, 'son mejores!!')
      puntos1 += puntos_tanto
      print(jug1, 'suma', puntos_tanto, 'puntos')

    else:
      print(jug1 + ': son buenas.')
      puntos2 += puntos_tanto
      print(jug2, 'suma', puntos_tanto, 'puntos')

  return puntos1, puntos2
  

def envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano):
  
  print('\nQue desea cantar?')
  print('1. Envido')
  print('2. Real envido')
  print('3. Falta envido')
  opcion = ValidarRTA (3)

  if opcion == 1:          
    puntos_tanto = 2
    puntos_al_no = 1
    print('\n' + jug1,'ha cantado ENVIDO')
    print('\n' + jug2 + ', que desea hacer?')
    mostrar_cartas (cartasj2)
    print('1. Envido')
    print('2. Real envido')
    print('3. Falta envido')
    print('4. Quiero')
    print('5. No quiero')
    opcion = ValidarRTA (5)

    if opcion == 1:             
      puntos_al_no = puntos_tanto
      puntos_tanto = 4
      print('\n' + jug2, 'ha cantado ENVIDO')
      mostrar_cartas (cartasj2)
      print('\n' + jug1 + ', que desea hacer?')
      print('1. Real envido')
      print('2. Falta envido')
      print('3. Quiero')
      print('4. No quiero')
      opcion = ValidarRTA (4)

      if opcion == 1:            
        puntos_al_no = puntos_tanto
        puntos_tanto = 7
        puntos1, puntos2 = real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano)
        
      elif opcion == 2:                 
        puntos_al_no=4
        puntos1, puntos2 = falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
      
      elif opcion == 3:                 
        print('\n' + jug1 + ' ha dicho QUIERO')
        puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)
      
      elif opcion == 4:                 
        print('\n' + jug1 + ' ha dicho NO QUIERO.', jug2, 'suma', puntos_al_no, 'puntos')
        puntos2 += puntos_al_no
        
    
    elif opcion == 2:                  
      puntos_al_no = puntos_tanto
      puntos_tanto=5
      puntos1, puntos2 = real_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_tanto, puntos_al_no, mano)
      
    elif opcion == 3:          
      puntos_al_no=2
      puntos1, puntos2 = falta_envido (jug2, puntos2, cartasj2, jug1, puntos1, cartasj1, puntos_al_no, mano)
    
    elif opcion == 4:               
      print('\n' + jug2 + ' ha dicho QUIERO')
      puntos1, puntos2 = sumar_puntos_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, mano)
    
    elif opcion == 5:                  
      print('\n' + jug2 + ' ha dicho NO QUIERO.',jug1,'suma',puntos_al_no,'puntos')
      puntos1 += puntos_al_no
      
    
  elif opcion == 2:                    
    puntos_al_no = 1
    puntos_tanto = 32
    puntos1, puntos2 = real_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_tanto, puntos_al_no, mano)
  
  elif opcion == 3:
    puntos_al_no=1
    puntos1, puntos2 = falta_envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_al_no, mano)
  
  return puntos1, puntos2






################################################################# FUNCIONES #############################################################








def mostrar_cartas (lista):
  cartas = "sus cartas son: "
  for i in lista:
    cartas += (str(i) + ', ')
  print(cartas)


def tirar_3 (jugador, cartas):
  lista = []
  print("\n" + jugador + ", que carta desea tirar: ")
  print("1. " + str(cartas[0]))
  print("2. " + str(cartas[1]))
  print("3. " + str(cartas[2]))
  op = ValidarRTA (3)

  for j in cartas:
    if j != cartas[op-1]:
      lista.append(j)

  return cartas[op-1], lista


def tirar_2(jugador,cartas):
  
  lista = []
  
  print("\n" + jugador + ", que carta desea tirar: ")
  print("1. " + str(cartas[0]))
  print("2. " + str(cartas[1]))
  op = ValidarRTA (2)
  
  for j in cartas:
    if j != cartas [op-1]:
      lista.append(j)
  
  return cartas[op],lista

def tirar_1 (jugador, cartas):
  
  print('\n' + jugador + ", le queda una sola carta, presione 1 para tirarla: ")
  print("1." + str(cartas[0]))
  opcion = ValidarRTA (1)

  return cartas[0], []


def quien_es_mano (ronda, p1, puntos1, p2, puntos2):
  
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


def JugarPrimera (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, puntos_truco, quiero, mano):                 #JUGAR PRIMERA
  
  termino = False
  hubo_envido = False
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
        puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True
        
        print('\n'+jug1+', que desea hacer?')
        mostrar_cartas(cartasj1)
        print('1. Cantar truco')
        print('2. Tirar carta')
        print('3. Irse al mazo')
        opcion = ValidarRTA (3)  

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
      print('1. Cantar envido')
      print('2. Cantar retruco')
      print('3. Tirar carta')
      print('4. Irse al mazo') 
      opcion = ValidarRTA (4)

      if opcion == 1:
        puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True
        
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
            print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
      
        elif opcion == 2:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
      
        elif opcion == 3:
          termino = True
          ganador = jug2

      elif opcion == 2:
        puntos_truco, termino, ganador, quiero = CantarReTruco (jug1, jug2)
      
        if termino != True:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 4:
        termino = True
        ganador = jug2
      
    elif puntos_truco == 3:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar envido')
      print('2. Cantar vale cuatro')
      print('3. Tirar carta')
      print('4. Irse al mazo') 
      opcion = ValidarRTA (4)

      if opcion == 1:
        puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True
        
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
            print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
      
        elif opcion == 2:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
        
        elif opcion == 3:
          termino = True
          ganador = jug2

      elif opcion == 2:
        puntos_truco, termino, ganador, quiero = CantarValeCuatro (jug1, jug2)
    
        if termino != True:
          carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        carta1_p1, cartasj1 = tirar_3(jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 4:
        termino = True
        ganador = jug2
      
    elif puntos_truco == 4:
      print('\n' + jug1 + ', que desea hacer?')
      mostrar_cartas (cartasj1)
      print('1. Cantar envido')
      print('2. Tirar carta')
      print('3. Irse al mazo') 
      opcion = ValidarRTA (3)

      if opcion == 1:
        puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
        hubo_envido = True
        
        print('\n' + jug1 + ', que desea hacer?')
        mostrar_cartas (cartasj1)
        print('1. Tirar carta')
        print('2. Irse al mazo')
        opcion = ValidarRTA (2)

        if opcion == 1:
          carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
          print("\n{} ha tirado el {}".format (jug1, str(carta1_p1)))
        
        elif opcion == 2:
          termino = True
          ganador = jug2

      elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

      elif opcion == 3:
        termino = True
        ganador = jug2
  
  elif quiero == jug2:
    print('\n' + jug1 + ', que desea hacer?')
    mostrar_cartas (cartasj1)
    print('1. Cantar envido')
    print('2. Tirar carta')
    print('3. Irse al mazo') 
    opcion = ValidarRTA (3)

    if opcion == 1:
      puntos1, puntos2 = envido (jug1, puntos1, cartasj1, jug2, puntos2, cartasj2, mano)
      hubo_envido = True
        
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
    
    elif opcion == 2:
        carta1_p1, cartasj1 = tirar_3 (jug1, cartasj1)
        print("\n{} ha tirado el {}".format (jug1, carta1_p1))

    elif opcion == 3:
      termino = True
      ganador = jug2

  return puntos1, puntos2, puntos_truco, termino, hubo_envido, carta1_p1, cartasj1, ganador, quiero


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



def Jugar():

  print('\nUsted ha elegido jugar una partida de TRUCO!')
  
  print('\nJugador 1, desea ingresar como usuario o como invitado?') 
  print('1. Usuario')
  print('2. Invitado')
  opcion = ValidarRTA (2)

  if opcion == 1:
    nombre1, apellido1, dni1, mail1, clave1, partidas_jug1, partidas_gan1, usuario1 = IniciarSesion (lista_jugadores)
    jugador1 = Jugador (nombre1, apellido1, dni1, mail1, clave1, partidas_jug1, partidas_gan1, usuario1)
    p1 = jugador1.usuario
  
  else:
    nombre1 = input ('Ingrese su nombre por favor')
    p1 = 'Invitado '+nombre1
  
  puntos1 = 0

  print('\nJugador 2, desea ingresar como usuario o como invitado?') 
  print('1. Usuario')
  print('2. Invitado')
  opcion = ValidarRTA (2)

  if opcion == 1:
    nombre2, apellido2, dni2, mail2, clave2, partidas_jug2, partidas_gan2, usuario2 = IniciarSesion (lista_jugadores)
    jugador2 = Jugador (nombre2, apellido2, dni2, mail2, clave2, partidas_jug2, partidas_gan2, usuario2)
    p2 = jugador2.usuario
  
  else:
    nombre2 = input ('Ingrese su nombre por favor')
    p2 = 'Invitado '+nombre2
  
  puntos2 = 0

  if p1 == p2:
    p1 = jugador1.apellido
    p2 = jugador2.apellido
  
  if p1 == p2:
    p1 += '1'
    p2 += '2'

  escribir = "\nSe ha iniciado una nueva partida entre: " + p1 + " y " + p2

  print(escribir)

  while puntos1 < 30 and puntos2 < 30:
    
    mazo=Mazo()       #Se crea el mazo

    cartas_en_juego = mazo.repartir()      #Se reparte el mazo

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

      puntos_mano, puntos_pie, puntos_truco, termino, hubo_envido, carta1_mano, cartas_mano, ganador, quiero  = JugarPrimera (mano, puntos_mano, cartasmano, pie, puntos_pie, cartas_pie, puntos_truco, quiero, mano)
      
      if termino == True:
        if quiero == '':
          puntos_truco = 2
        break
      
      if hubo_envido == True:
        puntos_truco, termino, carta1_pie, cartas_pie, ganador, quiero  = JugarPrimeraSinTanto (pie, cartas_pie, mano, puntos_truco, quiero)
    
        if termino == True: 
          break

      elif hubo_envido == False:
        puntos_pie, puntos_mano, puntos_truco, termino, hubo_envido, carta1_pie, cartas_pie, ganador, quiero  = JugarPrimera (pie, puntos_pie, cartas_pie, mano, puntos_mano, cartasmano, puntos_truco, quiero, mano)

        if termino == True:
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

    if ganador == mano:
      puntos_mano += puntos_truco
      print("\nHa ganado: ", mano, " se le suman ", puntos_truco, " puntos")
      
    elif ganador == pie:
      puntos_pie += puntos_truco
      print("\nHa ganado: ", pie, " se le suman ", puntos_truco, " puntos")
       

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


  if puntos1 >= 30 and puntos2 >= 30:
          
    if puntos1 > puntos2:
      print('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
      ganador_final = "gano {}, {} a {}".format(p1, puntos1, puntos2) 
    elif puntos2 > puntos1:
      print('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')
      ganador_final = "gano {}, {} a {}".format(p2, puntos2, puntos1) 
    elif puntos2 == puntos1:
      print('\nHA HABIDO UN EMPATE.')
      ganador_final = "empate"
  elif puntos2 >= 30:
    print('\nFELICITACIONES ' + p2 + '!!! USTED HA GANADO LA PARTIDA!!!')
    ganador_final = "gano {}, {} a {}".format(p2, puntos2, puntos1) 

  elif puntos1 >= 30:
    print('\nFELICITACIONES ' + p1 + '!!! USTED HA GANADO LA PARTIDA!!!')
    ganador_final = "gano {}, {} a {}".format(p1, puntos1, puntos2)



  partida_jugada = Partida(ganador_final, [jugador1.nombre,jugador2.nombre], lista_codigos_existentes)
  escritura = "{};{};{};{};{};/".format(str(partida_jugada.codigo_partida), partida_jugada.jugadores[0], partida_jugada.jugadores[1], partida_jugada.fecha, partida_jugada.resultado)


def ValidarRTA (parametro):
  
  rta_valida = False

  if parametro == 1:
    while rta_valida == False:
      try:
        opcion = int(input('\nElija: '))
        while opcion not in [1]: 
          opcion = int(input('\nElija 1 por favor: '))
        rta_valida = True
      except:
        rta_valida = False
      
  elif parametro == 2:
    while rta_valida == False:
      try:
        opcion = int(input('\nElija: '))
        while opcion not in [1, 2]: 
          opcion = int(input('\nElija 1 o 2 por favor: '))
        rta_valida = True
      except:
        rta_valida = False
  
  elif parametro == 3:
    while rta_valida == False:
      try:
        opcion = int(input('\nElija: '))
        while opcion not in [1, 2, 3]: 
          opcion = int(input('\nElija 1, 2 o 3 por favor: '))
        rta_valida = True
      except:
        rta_valida = False
  
  elif parametro == 4:
    while rta_valida == False:
      try:
        opcion = int(input('\nElija: '))
        while opcion not in [1, 2, 3, 4]: 
          opcion = int(input('\nElija 1, 2, 3 o 4 por favor: '))
        rta_valida = True
      except:
        rta_valida = False
  
  elif parametro == 5:
    while rta_valida == False:
      try:
        opcion = int(input('\nElija: '))
        while opcion not in [1, 2, 3, 4, 5]: 
          opcion = int(input('\nElija 1, 2, 3, 4 o 5 por favor: '))
        rta_valida = True
      except:
        rta_valida = False
  
  return opcion


def PedirDNI ():
  dni_mal = True
  while dni_mal == True:
    try:
      dni = int(input("Ingrese el DNI: ")) 
      while dni < 10000000 or dni > 99999999:
        dni = int(input("DNI invalido. Por favor, ingrese el DNI (8 numeros): ")) 
      dni_mal = False
    except:
      dni_mal = True
  
  return dni



def Validar (lista, objeto, parametro):
  existe = False
  for jugador in lista:
    if jugador[parametro] == objeto:
      existe = True
  return existe



def PedirMail ():
  mail = input('Ingrese su mail: ')
  arroba = False
  com = False

  while com == False or arroba == False:
    arroba = False
    com = False
    
    for i in range(len(mail)):
      if mail[i] == '@':
        arroba = True
      if mail[i] == '.':
        try:
          if mail[i] + mail[i + 1] + mail[i + 2] + mail[i + 3] == '.com':
            com = True
        except:
          com = False
        if com == False:
          try:
            if mail[i] + mail[i + 1] + mail[i + 2] == '.ar':
              com = True
          except:
            com = False
    
    if arroba == False or com == False:
      mail = input('Email incorrecto. Ingreselo nuevamente: ')
  
  return mail


def Pedirclave ():
  contra = False
  while contra == False:
    clave = input('Elija su clave: ')
    clave2 = input('Vuelva a escribir su clave para validarla: ')
    
    if clave == clave2:
      print('clave validada correctamente.')
      contra = True

    else:
      print('Las claves no coinciden. Vuelvan a intentarlo.')
      contra = False
  
  return clave


def PedirUsuario ():
  usuario = input('Ingrese su usuario: ')
  return usuario


def PedirDatos (lista):
  
  nombre = input('Ingrese su nombre: ')
  apellido = input('Ingrese su apellido: ')
  
  usuario_nuevo = False
  while usuario_nuevo == False:
    
    dni = PedirDNI ()
    existe = Validar (lista_jugadores, dni, 2)
    while existe == True:
      print('DNI ya ingresado. Vuelva a intentarlo.')
      dni = PedirDNI ()
      existe = Validar (lista_jugadores, dni, 2)
    
    mail = PedirMail ()
    existe = Validar (lista_jugadores, mail, 3)
    while existe == True:
      print('mail ya ingresado. Vuelva a intentarlo.')
      mail = PedirMail ()
      existe = Validar (lista_jugadores, mail, 3)
    
    usuario = PedirUsuario ()
    existe = Validar (lista_jugadores, usuario, 7)
    while existe == True:
      print('Nombre de usuario ya existente. Vuelva a intentarlo.')
      usuario = PedirUsuario ()
      existe = Validar (lista_jugadores, usuario, 7)

  
    clave = Pedirclave ()

  return nombre, apellido, dni, mail, clave, usuario


def lectura(archivo):
  variable = ""
  lista_var = []
  for caracter in archivo:
    if caracter != "/":
      variable += caracter
    else:
      lista_var.append(variable)
      variable = ""

  var2 = ""
  lista_var_final = []

  for i in lista_var:
    aux = []
    for caracter in i:
      if caracter != ";":
        var2 += caracter
      else:
        aux.append(var2)
        var2 = ""
    lista_var_final += [aux]
    
  return lista_var_final


def IniciarSesion (lista):

  print('Usted ha decidido iniciar sesion. ')

  inicio = False

  while incio == False:
    usuario = PedirUsuario ()
    clave = Pedirclave ()
    for jugador in lista:
      if jugador[7] == usuario and jugador[4] == clave:
        inicio = True
        nombre = jugador[0]
        apellido = jugador[1]
        dni = jugador[2]
        partidas_jug = jugador[5]
        partidas_gan = jugador[6]

    
    if inicio == False:
      print('El nombre de usuario o contraseña son incorrectos. Por favor, vuelva a intentarlo.')
  
  return nombre, apellido, dni, mail, clave, partidas_jug, partidas_gan, usuario


def lectura(file):
    lista = []
    with open(file, newline='') as archivo:  
        jugadores = csv.reader(archivo)
        for jugador in jugadores:
            lista += [jugador]
        lista.pop(0)
    return lista


################################################################ MAIN ###################################################################



lista_jugadores = lectura ('archivo_jugadores.csv')
lista_partidas = lectura ('archivo_partidas.csv')


opcion2 = 1

while opcion != 4:

  print("\nBienvenido! Que desea hacer?")
  print("\n1. Buscar en la base de datos")
  print("\n2. Jugar un partido de Truco")
  print('\n3. Ajustes de usuario')
  print("\n4. Salir")
  opcion = input("\nElija: ")

  opcion = ValidarRTA(4)
  
  if opcion == 1:
    x = 10
  
  elif opcion == 2:
    Jugar()
  
  elif opcion == 3:
    print('Bienvenido al menu de ajustes. ')
    print('1. Crear un usuario')
    print('2. Modificar la informacion de un usuario existente')
    opcion = ValidarRTA (2)

    if opcion == 1:
      
      nombre, apellido, dni, mail, clave, usuario = PedirDatos (lista_jugadores)
      jugador = Jugador (nombre, apellido, dni, mail, clave, 0, 0, usuario)
    
      print('\nEl jugador ha sido ingresado con exito!')

    elif opcion == 2:
      print('Por favor, vamos a necesitar que ingrese con su usuario.')
      nombre_us, apellido_us, dni, mail, clave, partidas_jug, partidas_gan, usuario_sesion = IniciarSesion (lista_jugadores)
      usuario_en_sesion = Jugador (nombre_us, apellido_us, dni, mail, clave, partidas_jug, partidas_gan, usuario_sesion)
      usuario_en_sesion.modificar()
      #Falta cambiar lista de jug y archivo

  
  elif opcion == 4:
    print('\nGracias por usar nuestro codigo!')
    print('Saludos.')



