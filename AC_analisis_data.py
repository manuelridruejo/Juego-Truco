import csv
from AB_Clases_Juego import *



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

    usuario_nuevo = True
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


def FiltrarJugador (lista):
  existe = False
  while existe == False:
    us = input('\nIngrese el usuario que desea buscar: ')
    for jugador in lista:
      if jugador[7] == us:
        p = Jugador(jugador[0],jugador[1],jugador[2],jugador[3],jugador[4],jugador[5],jugador[6],jugador[7])
        print(p)
        existe = True
    if existe == False:
      print('Jugador no encontrado. Vuelva a intentarlo por favor.')


def PartidaxJugador (lista, usuario):
  historial = ''       #Busca las partidas que haya jugado un jugador X, haya ganado o perdido
  for i in range(len(lista)):
    if lista[i][1] == usuario or lista[i][2] == usuario:
      historial += 'Codigo: {}, ganador: {}, vencedor: {}, resultado: {}, fecha: {}\n'.format(lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4])

  return historial

def PartidaxFecha (lista, fecha):         #Busca todas las partidas que hayan sucedido despues de una cierta fecha
  historial = ''
  for i in range(len(lista)):
    if datetime.strptime(lista[i][4], '%Y-%m-%d').date() >= fecha :
      historial += 'Codigo: {}, ganador: {}, vencedor: {}, resultado: {}, fecha: {}\n'.format(lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4])

  return historial


def PartidaParticular (lista, filtro, parametro):
  
  historial = ''       #Filtra las partidas que compartan un parametro en comun (ej: fecha, codigo, etc)
  for i in range(len(lista)):
    if lista[i][parametro] == filtro:
      historial += 'Codigo: {}, ganador: {}, vencedor: {}, resultado: {}, fecha: {}\n'.format(lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4])

  return historial


def UltimasNPartidas (lista, N):
  historial = ''
  cont = 0
  if N > len(lista):
    print('\nNo hay tal cantidad de partidas. Aqui mostraremos todas las disponibles.')
  for i in range(len(lista)-1,-1,-1):
    while cont < N:
      historial += 'Codigo: {}, ganador: {}, vencedor: {}, resultado: {}, fecha: {}\n'.format(lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4])
      cont += 1
      break #buscar si se puede hacer de otra forma
  return historial


def TodasLasPartidas (lista):
  historial = ''
  for i in range(len(lista)):
    historial += 'Codigo: {}, ganador: {}, vencedor: {}, resultado: {}, fecha: {}\n'.format(lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4])
  return historial


def BuscarPartidaParticular (lista):
  print('Bienvenido al buscador de partidas, como desea filtrar su busqueda?')
  print('1. Por codigo de partida')
  print('2. Por usuario')
  print('3. Por fecha')
  print('4. Buscar partidas del dia de hoy')
  opcion = ValidarRTA (4)

  if opcion == 1:
    print('Usted ha elegido filtrar por codigo de partida.')
    codigo = PedirCodigo ()
    historial = PartidaParticular (lista, codigo, 0)

  elif opcion == 2:
    print('Usted ha elegido filtrar por usuario. Recuerde que apareceran todas las partidas de dicho usuario. Tambien puede buscar las de invitados anteponiendo el prefijo *Invitado *.')
    usuario = input('Ingrese el nombre de usuario: ')
    historial = PartidaxJugador (lista, usuario)
    if historial == '':
      historial = '\nNo se han encontrado partidas para dicho usuario.'
  
  elif opcion == 3:
    fecha = ValidarFecha()
    historial = PartidaParticular (lista, fecha, 4)

  elif opcion == 4:
    fecha = date.today()
    historial = PartidaParticular (lista, fecha, 4)
    if historial == '':
      historial = '\nNo se encontraron partidas el dia de hoy'
  
  if historial == '':
    historial = '\nNo se encontraron partidas bajo tales parametros'

  return historial

def RegistroPartidas (lista):
  print('\nBienvenido al registro de partidas, que desea buscar?')
  print('1. Ultimas N partidas')
  print('2. Partidas a partir de DD/MM/YY')
  print('3. Ver todo el registro de partidas')
  opcion = ValidarRTA (3)

  if opcion == 1:
    print('Cuantas partidas desea ver?')
    n = ValidarEntero ()
    historial = UltimasNPartidas (lista, n)

  elif opcion == 2:
    fecha = ValidarFecha()
    historial = PartidaxFecha (lista, fecha)

  elif opcion == 3:
    historial = TodasLasPartidas (lista)
  
  if historial == '':
    historial = '\nNo se encontraron partidas bajo tales parametros'
  
  return historial


def RankingMensual (lista):
  pass