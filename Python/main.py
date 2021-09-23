import os
import time
import random
from msvcrt import getch
opcion = 0
global n
n = 0

sensor = {}
sensor["nombre"] = ' '
sensor["medicion"] = 0
sensor["unidad"] = ' '
sensor["prioridad"] = 0
sensor["medicion"]
sensor0 = [sensor["nombre"], sensor["medicion"], sensor["unidad"], sensor['prioridad']]
sensor1 = [sensor["nombre"], sensor["medicion"], sensor["unidad"], sensor['prioridad']]
sensor2 = [sensor["nombre"], sensor["medicion"], sensor["unidad"], sensor['prioridad']]
sensor3 = [sensor["nombre"], sensor["medicion"], sensor["unidad"], sensor['prioridad']]
sensor4 = [sensor["nombre"], sensor["medicion"], sensor["unidad"], sensor['prioridad']]
sensor5 = [sensor["nombre"], sensor["medicion"], sensor["unidad"], sensor['prioridad']]
sensor6 = [sensor["nombre"], sensor["medicion"], sensor["unidad"], sensor['prioridad']]
sensor7 = [sensor["nombre"], sensor["medicion"], sensor["unidad"], sensor['prioridad']]
sensor8 = [sensor["nombre"], sensor["medicion"], sensor["unidad"], sensor['prioridad']]
sensor9 = [sensor["nombre"], sensor["medicion"], sensor["unidad"], sensor['prioridad']]
listasensores = [sensor0, sensor1, sensor2, sensor3, sensor4, sensor5, sensor6, sensor7,sensor8 ,sensor9]

#listasensores [n][elemento a modificar].  en los corchetes van numeros o variables de numeros, es una matriz.

def altasensor():
    global n
    (listasensores[n][0]) = str(input("Ingrese el nombre del sensor: "))
    (listasensores[n][3]) = int(input("Ingrese el numero de prioridad (1-10): "))
    (listasensores[n][1]) = str(input("Ingrese la unidad de medicion: "))
    n += 1
    os.system("cls")
    menu()
def eliminar():
    for a in range(10):
        if (listasensores[a][3] != 0):
            print("Sensor - ", ',', listasensores[a][0])
    senselim = str(input("Seleccione el sensor a eliminar: "))
    for b in range (10):
        if (senselim == listasensores[b][0]):
            listasensores[b][0] = ' '
            listasensores[b][3] = 0
            listasensores[b][2] = ' '
    print("Se ha eliminado el sensor: ", senselim)
    os.system("pause")
    os.system("clear")
    menu()
def modsens():
    for a in range(10):
        if (listasensores[a][3] != 0):
            print("Sensor - ", ',', listasensores[a][0])
    sensmod = str(input("Seleccione el sensor a modificar: "))
    for b in range(10):
        if (sensmod == listasensores[b][0]):
            listasensores[b][0] = str(input("Ingrese el nuevo nombre del sensor: "))
            listasensores[b][3] = int(input("Ingrese el nuevo numero de prioridad: "))
            listasensores[b][2] = str(input("Ingrese la nueva unidad de medida: "))
    print("Se guardo el sensor: ", sensmod)
    print("Con el nombre: ", listasensores[b][0])
    print("Numero de prioridad: ", listasensores[b][3])
    print("Y unidad: ", listasensores[b][2])
    os.system("pause")
    os.system("cls")
    menu()
def visual():
    while (True):
        for a in range(10):
            listasensores[a][1] = random.randint(10, 99)
            if (listasensores[a][3] != 0):
                print("""                Nombre del sensor | Medicion | Unidad | Prioridad""")
                print("Sensor - ", a, "                ", listasensores[a][0], "|   ", listasensores[a][1], "   |   ",  listasensores[a][2], "  |", listasensores[a][3])
        print("Presione ESC para volver al menu anterior")
        time.sleep(1)
    menu()
def menu():
    global opcion
    print("""
            1- Añadir sensor
            2- Eliminar sensor
            3- Modificar sensor
            4- Visualizar sensores
            5- Salir
            """)
    while (opcion != 5):
        opcion = int(input("Ingrese opcion: "))
        if (opcion == 1):
            altasensor()
        elif (opcion == 2):
            eliminar()
        elif (opcion == 3):
            modsens()
        elif (opcion == 4):
            visual()
        elif (opcion == 5):
            print("""Seguro que desea salir?
        Si        No""")
            salir = (str(input("Opción: ")))
            if (salir == 'si' or salir == 'Si' or salir == 'SI' or salir == 'sI'):
                print("MAIAMEEEE")
                quit()
            else:
                menu()
        else:
            print('opcion incorrecta')
            time.sleep(1)
            menu()
print ( """
    Menú tipo ABM - CRUD simple by Tomás Cosentino""")
menu()