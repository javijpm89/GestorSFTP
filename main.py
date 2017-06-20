# -*- coding: utf-8 -*-
# Autor: Javier Pérez Martin
# (c) Plataforma de Negocio
# main.py
# Descripcion -> Fichero de ejecución principal

import actions
import os
import threading
import time

seleccion = ''

def printMenu():


    print "################################"
    print "####### GESTOR SFTP ############"
    print "## (c) Plataforma de negocio  ##"
    print "## (c) Dpto. Gestion          ##"
    print "## (c) TELECOR S.A.           ##"
    print "## Version -> 0.1 [Alpha]     ##"
    print "################################"

    print "--> Menú Principal <--"
    print "1. Listar Usuarios SFTP"
    print "2. Listar Grupos SFTP"
    print "3. Cambiar password de usuario"
    print "4. Añadir usuario a grupo"
    print "5. Crear nuevo usuario SFTP"
    print "6. Crear nuevo usuario DISTRIBUIDOR"
    print "7. Crear nuevo usuario OPERADOR"
    print "8. Buscar usuario"
    print "EXIT -> Salir del programa"
    print "\n"
    print "Seleccionar una opción"
    seleccion = raw_input(">>")

    if (seleccion.lower() == 'exit'):
        exit(0)

def killproc(pid):
    print "Killing current process " + str(pid)
    os.system('kill -9 ' + str(pid))

def rootExecution():
    os.system('sudo python main.py')


def execute():
    while (seleccion != 'exit'):
        executionUser = os.getegid()

        executeAsRoot = 'y'
        if (executionUser != 0):
            print "Este softwre debe ejecutarse como root"
            executeAsRoot = raw_input("¿Desea ejecutar el programa como root?[Y/n]")
            if (executeAsRoot.lower() == 'y'):
                threadSudoStart = threading.Thread(name='Thread Arranque Sudo', target=rootExecution)
                threadSudoStart.start()

            else:
                print "Selección no válida"
                execute()
        else:
            printMenu()

threadMain = threading.Thread(name='Thread Principal',target=execute())
threadMain.start()




