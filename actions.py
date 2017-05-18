# -*- coding: utf-8 -*-
# Autor: Javier Pérez Martin
# (c) Plataforma de Negocio
# actions.py
# Descripcion -> Fichero con la lógica de la aplicación

import os
import getpass


# Función para crear un usuario
def createUser(nombre):
    print "Creación de usuario SFTP"
    newUser = raw_input("Nombre de usuario >> ")

    homeNewUser = raw_input("Home para el usuario " + newUser + "(relativa a (/app/sftp/) >> ")

    command = "useradd -d " + "/app/sftp/" + homeNewUser + " -G sftponly -s /usr/sbin/nologin -N " + newUser
    print "Ejecutando " + command
    command2 = "passwd " + newUser

    try:
        os.system(command)
        os.system("passwd " + newUser)
    except OSError:
        print "Error al crear el usuario"
