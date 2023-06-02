from datetime import *


def Validar (lista, atributo, parametro): 
  '''
  atributo: Variable que quiero verificar es unica
  Lista: Matriz donde se encuentran el resto de objetos
  Parametro: Caracteristica del objeto que quiero analizar. es un entero que determina el indice
  
  por ej, si quiero verificar si existe un usuario que se llamen fojeda: 
  atributo = fojeda
  lista = lista_jugadores
  Parametro = 7, indice de la lista jugador donde se encuentra el nombre de usuario
  
  No esta estrictamente relacionada con la clase Jugador, puesto funcionaría con cualquier lista de listas con atributos en comun'''        

  existe = False
  for jugador in lista:
    if jugador[parametro] == atributo:
      existe = True
  return existe


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


def ValidarEntero ():
  num = False
  while num == False:
    try:
      n = int(input('Elija un numero: '))
      num = True
    except:
      print('Por favor, que sea un numero.')
  return n


def ValidarFecha ():
  rta_valida = False
  while rta_valida == False:
    try:
      anio = int(input('Ingrese el anio: '))
      while anio > date.today().year or anio < 2023:
        anio = int(input('Anio invalido. Las partidas datan del 2023 en adelante. Vuelva a intentarlo: ')) 
      rta_valida = True
    except:
      print('Error. Vuelva a intentarlo.')
  
  rta_valida = False
  while rta_valida == False:
    try:
      mes = int(input('Ingrese el mes: '))
      while mes > 12 or mes < 1:
        mes = int(input('Mes invalido, vuelva a intentarlo: '))
      if anio == date.today().year and mes > date.today().month:
        print('Recuerde que hoy es ',str(date.today()))
      else:
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

      if anio == date.today().year and mes == date.today().month and dia >date.today().day:
        print('Recuerde que hoy es ',str(date.today()))
      else:
        rta_valida = True 

    except:
      print('Error. Vuelva a intentarlo.')

  fecha = str(anio) + '-' + str(mes) + '-' + str(dia)
  fecha_dt = datetime.strptime(fecha, '%Y-%m-%d').date()    

  return fecha_dt


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


def PedirCodigo ():
  rta_valida = False
  while rta_valida == False:
    try:
      cod = int(input('\nIngrese el numero de codigo: '))
      rta_valida = True
      cod = str(cod)
    except:
      print('Recuerde que el codigo debe ser un numero.')
  
  aux=''
  largo = len(cod)
  for i in range(7-largo):
    aux += '0'
  codigo = aux + cod

  return 

