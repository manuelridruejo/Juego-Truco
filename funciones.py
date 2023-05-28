from Clases_Juego import *
import csv
from datetime import *

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
      n += 1
        
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
  
  fin_partida = chequearganador(puntos1, puntos2)

  return puntos1, puntos2, fin_partida


def chequearganador(puntos1, puntos2):
  
  fin_partida = False

  if puntos1 >= 30:
    fin_partida = True
  
  if puntos2 >= 30:
    fin_partida = True
  
  return fin_partida


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
  
  return cartas[op-1],lista


def tirar_1 (jugador, cartas):
  
  print('\n' + jugador + ", le queda una sola carta, presione 1 para tirarla: ")
  print("1." + str(cartas[0]))
  opcion = ValidarRTA (1)

  return cartas[0], []


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


def CrearUsuario (lista):
  
  nombre = input('Ingrese su nombre: ')
  apellido = input('Ingrese su apellido: ')
  
  usuario_nuevo = False
  while usuario_nuevo == False:
    
    dni = PedirDNI ()
    existe = Validar (lista, dni, 2)
    while existe == True:
      print('DNI ya existente. Vuelva a intentarlo.')
      dni = PedirDNI ()
      existe = Validar (lista, dni, 2)
    
    mail = PedirMail ()
    existe = Validar (lista, mail, 3)
    while existe == True:
      print('mail ya existente. Vuelva a intentarlo.')
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


def IniciarSesion (lista):

  print('Usted ha decidido iniciar sesion. ')

  inicio = False

  while inicio == False:
    usuario = input('Usuario: ')
    clave = input('Contraseña: ')
    for jugador in lista:
      if jugador[7] == usuario and jugador[4] == clave:
        inicio = True
        nombre = jugador[0]
        apellido = jugador[1]
        dni = int(jugador[2])
        mail = jugador[3]
        partidas_jug = int(jugador[5])
        partidas_gan = int(jugador[6])

    if inicio == False:
      print('El nombre de usuario o contraseña son incorrectos. Por favor, vuelva a intentarlo.')
  
  return nombre, apellido, dni, mail, clave, partidas_jug, partidas_gan, usuario


def lectura_jugadores (file):
    lista = []
    with open(file, newline = '') as archivo:  
      jugadores = csv.reader(archivo)
      for jugador in jugadores:
        lista += [jugador]
    
    for jugador in lista:
      jugador[2] = int(jugador[2])
      jugador[5] = int(jugador[5])
      jugador[6] = int(jugador[6])

    return lista


def lectura_partidas (file):
  lista = []
  with open(file, newline = '') as archivo:  
    jugadores = csv.reader(archivo)
    for jugador in jugadores:
      lista += [jugador]
  return lista


def escritura(archivo:str, matriz):
    
    with open(archivo, "w", newline = "") as file:
        writer = csv.writer(file, delimiter = ",")
        writer.writerows(matriz)
    return


def Historial (lista, opcion, filtro, parametro):
  historial = ''
  if opcion == 0:
    for i in range(len(lista)):
      historial += 'Codigo: {}, ganador: {}, vencedor: {}, resultado: {}, fecha: {}\n'.format(lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4])
    
  if opcion == 1:
    for i in range(len(lista)):
      if lista[i][parametro] == filtro:
        historial += 'Codigo: {}, ganador: {}, vencedor: {}, resultado: {}, fecha: {}\n'.format(lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4])

  if opcion == 2:
    for i in range(len(lista)):
      if lista[i][1] == filtro or lista[i][2] == filtro:
        historial += 'Codigo: {}, ganador: {}, vencedor: {}, resultado: {}, fecha: {}\n'.format(lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4])

  return historial

def ValidarFecha ():
  rta_valida = False
  while rta_valida == False:
    try:
      anio = int(input('Ingrese el anio: '))
      while anio > 2023:
        anio = int(input('Anio invalido, vuelva a intentarlo: '))  #usar date
      rta_valida = True
    except:
      print('Error. Vuelva a intentarlo.')
  
  rta_valida = False
  while rta_valida == False:
    try:
      mes = int(input('Ingrese el mes: '))
      while mes > 12 or mes < 1:
        mes = int(input('Mes invalido, vuelva a intentarlo: '))  #usar date
      rta_valida = True
    except:
      print('Error. Vuelva a intentarlo.')
  
  rta_valida = False
  while rta_valida == False:
    try:
      
      dia = int(input('Ingrese el dia: '))

      if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        while dia > 31 or dia < 0:
          anio = int(input('Dia invalido, vuelva a intentarlo: '))  #usar date
      
      elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        while dia > 30 or dia < 0:
          anio = int(input('Dia invalido, vuelva a intentarlo: '))  #usar 
        
      elif mes == 2:
        while dia >28 or dia < 0:
          anio = int(input('Dia invalido, vuelva a intentarlo: '))  #usar 

      rta_valida = True

    except:
      print('Error. Vuelva a intentarlo.')
  
  fecha = str(anio) + '/' + str(mes) + '/' + str(dia)
  fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')     #Falta, ni idea

def BuscarPartida (lista):
  print('Bienvenido al buscador de partidas, como desea filtrar su busqueda?')
  print('1. Por codigo de partida')
  print('2. Por usuario')
  print('3. Por fecha')
  opcion = ValidarRTA (3)

  if opcion == 1:
    print('Usted ha elegido filtrar por codigo de partida.')
    rta_valida = False
    while rta_valida == False:
      try:
        cod = int(input('\nIngrese el numero de codigo: '))
        rta_valida = True
      except:
        print('Recuerde que el codigo debe ser un numero.')
    
    aux=''
    largo = len(cod)
    for i in range(7-largo):
      aux += '0'
    codigo = aux + cod

    historial = Historial (lista, 1, codigo, 0)

  elif opcion == 2:
    print('Usted ha elegido filtrar por usuario. Recuerde que apareceran todas las partidas de dicho usuario. Tambien puede buscar las de invitados anteponiendo el prefijo *Invitado *.')
    usuario = input('Ingrese el nombre de usuario: ')
    historial = Historial (lista, 2, usuario, 0)
    if historial == '':
      historial += 'No se han encontrado partidas para dicho usuario.'
  
  elif opcion == 3:
    rta_valida = False
    while rta_valida == False:
      try:
        anio = int(input('Ingrese el anio: '))
        while anio > 2023:
          anio = int(input('Anio invalido, vuelva a intentarlo: '))  #usar date
        rta_valida = True
      except:
        print('Error. Vuelva a intentarlo.')
    

  

  return historial
        