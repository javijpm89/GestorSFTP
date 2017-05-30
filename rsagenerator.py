import os
from Crypto.PublicKey import RSA

# Función que genera una llave RSA en el home del usuario
def generateRSAKEY(homeDir, user):
    key = RSA.generate(2048)
    homeSSH = homeDir + '/.ssh'

    if not (os.path.exists(homeDir+'/.ssh')):
        print "Creando directorio > " + homeDir + '/.ssh'
        os.mkdir(homeSSH)

        print "Obteniendo uid y gid del usuario nuevo"
        uid = os.system("id -u "+user)
        gid = os.system("id -g "+user)

        print "Cambiando permisos y grupo al nuevo directorio"
        os.chown(homeSSH,uid,gid)
        os.chmod(homeSSH,0600)
    else:
        print "El directorio ya existe, generamos las llaves RSA"

    with open(homeSSH+"/id_rsa", 'w') as content_file:
        os.chmod(homeSSH+"/id_rsa", 0600)
        content_file.write(key.exportKey('PEM'))

    with open(homeSSH + "/id_rsa.pub", 'w') as content_file:
        content_file.write(key.publickey().exportKey())