import csv

def lectura(file):
    lista = []
    with open(file, newline='') as archivo:  
        jugadores = csv.reader(archivo)
        for jugador in jugadores:
            lista += [jugador]
        lista.pop(0)
    return lista
    
def escritura(archivo,datos):
    File = open(archivo, 'w')
    with File:
        writer = csv.writer(File)
        writer.writerows(datos)
    
