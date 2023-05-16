import csv
from Clases_Juego import *


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
    existe = Validar (lista, dni, 2)
    while existe == True:
      print('DNI ya ingresado. Vuelva a intentarlo.')
      dni = PedirDNI ()
      existe = Validar (lista, dni, 2)
    
    mail = PedirMail ()
    existe = Validar (lista, mail, 3)
    while existe == True:
      print('mail ya ingresado. Vuelva a intentarlo.')
      mail = PedirMail ()
      existe = Validar (lista, mail, 3)
    
    usuario = PedirUsuario ()
    existe = Validar (lista, usuario, 7)
    while existe == True:
      print('Nombre de usuario ya existente. Vuelva a intentarlo.')
      usuario = PedirUsuario ()
      existe = Validar (lista, usuario, 7)

  
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

  while inicio == False:
    usuario = PedirUsuario ()
    clave = Pedirclave ()
    for jugador in lista:
      if jugador[7] == usuario and jugador[4] == clave:
        inicio = True
        nombre = jugador[0]
        apellido = jugador[1]
        dni = jugador[2]
        mail = jugador[3]
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
