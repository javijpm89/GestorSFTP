from os import chmod
from Crypto.PublicKey import RSA

key = RSA.generate(2048)

with open("/tmp/id_rsa",'w') as content_file:
    chmod("/tmp/id_rsa", 0600)
    content_file.write(key.exportKey('PEM'))

with open("/tmp/id_rsa.pub",'w') as content_file:
    content_file.write(key.publickey().exportKey())
