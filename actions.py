# -*- coding: utf-8 -*-
# Autor: Javier Pérez Martin
# (c) Plataforma de Negocio
# actions.py
# Descripcion -> Fichero con la lógica de la aplicación

import os
import subprocess
import rsagenerator as rsagen

## Funciones de listados ##

# Funcion de listado de usuarios y grupos

def listUsers():
    print "Listando los usuarios registrados en el sistema"
    print (subprocess.check_output("cat /etc/passwd | grep '/usr/sbin/nologin' | grep home | awk -F ':' {'print $1'}",
                                   shell=True))


def listGroups():
    for group in (subprocess.check_output("cat /etc/group | grep sftp", shell=True).split("\n")):
        print (group.strip().split(":")[0])


## Funcionaes de creación de usuarios ##

# Función para crear un usuario
def createUser(nombre):
    print "Creación de usuario SFTP"
    new_user = raw_input("Nombre de usuario >> ")

    home_new_user = raw_input("Home para el usuario " + new_user + "(relativa a (/app/sftp/) >> ")

    command = "useradd -d " + "/app/sftp/" + home_new_user + " -G sftponly -s /usr/sbin/nologin -N " + new_user
    command3 = "mkdir -p -m 700 " + home_new_user

    try:
        print "Ejecutando " + command
        os.system(command)
        print "Ejecutando " + command3
        os.system(command3)
        print "Creando directorio home del nuevo usuario"
        os.makedirs(home_new_user)
        uid = os.system("cat /etc/passwd | grep " + new_user + " | awk -F ':' {'print $3'}")
        gid = os.system("cat /etc/group | grep sftponly | awk -F ':' {'print $3'}")
        os.chown(home_new_user, int(uid), int(gid))
        os.chmod(home_new_user, int(700))

        print "¿Generar llave RSA para el nuevo usuario?"
        requiresKEY = 'Y'
        requiresKEY = raw_input("[Y/n] >> ")

        if requiresKEY == 'Y':
            rsagen.generateRSAKEY(home_new_user, nombre)

    except OSError:
        print "Error al crear el usuario"




## Funciones de búsqueda ##

# Función para buscar un usuario
def findUser(_nombre):
    nombre = _nombre
    found = False
    for user in (
            subprocess.check_output("cat /etc/passwd | grep '/usr/sbin/nologin' | awk -F ':' {'print $1'}",shell=True).split('\n')):
        if (user.lower == nombre.lower) and (found == False):
            found = True
            print "Se ha encontrado >> " + user

        if (found == False):
            print "No se ha encontado ningún usuario " + nombre


