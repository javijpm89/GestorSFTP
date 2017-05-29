# -*- coding: utf-8 -*-
# Autor: Javier Pérez Martin
# (c) Plataforma de Negocio
# actions.py
# Descripcion -> Fichero con la lógica de la aplicación

import os
import subprocess

# Funcion de listado de usuarios
def listUsers():
    print "Listando los usuarios registrados en el sistema"
    print (subprocess.check_output("cat /etc/passwd | grep '/usr/sbin/nologin' | grep home | awk -F ':' {'print $1'}",shell=True))



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
        os.chown(home_new_user,int(uid),int(gid))
        os.chmod(home_new_user,int(700))

    except OSError:
        print "Error al crear el usuario"



listUsers()