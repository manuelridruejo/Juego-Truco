from random import shuffle
from datetime import date

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
 
def Validar (lista, objeto, parametro):
  existe = False
  for jugador in lista:
    if jugador[parametro] == objeto:
      existe = True
  return existe

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
  
  def gano_partida(self):
    self.partidas_ganadas += 1
    self.partidas_jugadas += 1
  
  def jugo_partida (self):
    self.partidas_jugadas += 1

  def modificar(self, lista):
    print("Usted ha decidido modificar su usuario. Que atributo desea modificar?")
    print("\n1. Nombre")
    print("\n2. Apellido")
    print("\n3. DNI")
    print("\n4. Mail")
    print('\n5. clave')
    print('\n6. usuario')

    rta_valida = False
    while rta_valida == False:
      try:
        opcion = int(input('\nElija: '))
        while opcion not in [1, 2, 3, 4, 5, 6]: 
          opcion = int(input('\nElija 1, 2, 3, 4, 5 o 6 por favor: '))
        rta_valida = True
      except:
        rta_valida = False

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
      dni_nuevo = PedirDNI ()
      existe = Validar (lista, dni_nuevo, 2)
      while existe == True:
        print('DNI ya existente. Vuelva a intentarlo.')
        dni_nuevo = PedirDNI ()
        existe = Validar (lista, dni_nuevo, 2)
      self.dni = dni_nuevo
      print('\nDNI cambiado con exito.')
      
    elif opcion == 4:
      print("Usted ha elegido modificar su mail.")
      mail_nuevo = PedirMail()
      existe = Validar (lista, mail_nuevo, 3)
      while existe == True:
        print('mail ya existente. Vuelva a intentarlo.')
        mail_nuevo = PedirMail ()
        existe = Validar (lista, mail_nuevo, 3)
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
      usuario_nuevo = input('Ingrese su usuario: ')
      existe = Validar (lista, usuario_nuevo, 7)
      while existe == True:
        print('Nombre de usuario ya existente. Vuelva a intentarlo.')
        usuario_nuevo = input('Ingrese su usuario: ')
        existe = Validar (lista, usuario_nuevo, 7)
      self.usuario = usuario_nuevo
      print('\nUsuario cambiado con exito.')
  
  def __str__ (self):
    return "Usuario: {}\nNombre: {}\nApellido: {}\nMail: {}\nPartidas jugadas: {}\nPorcentaje de victoria: {}".fromat(self.usuario, self.nombre, self.apellido, self.mail, self.partidas_jugadas, float(self.partidas_ganadas/self.partidas_jugadas))
  


class Jugadores():

  def __init__ (self, lista_jugadores) -> None:
    self.lista_jugadores = lista_jugadores

  def agregar_jugadores (self,jugador):
    self.lista_jugadores.append (jugador.nombre_usuario)


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
  