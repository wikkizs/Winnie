import socket 
import ssl
import time

MAX_RECV = 4096


# Création de la socket TCP
def creation_socket_serveur() : 

    #Creation de la socket TCP 
    socket_serveur = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    

    # Permet de réutiliser plus vite une adresse et un port
    socket_serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    return socket_serveur


# Création de la socket SSL
def creation_socket_serveur_ssl (socket_serveur, adresse_serveur, port) : 


    #Creation du context SSL 
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("SSL/CERT/cert-server.pem","SSL/CERT/cert-key.pem")

    # Ouvrir le serveur 
    socket_serveur.bind((adresse_serveur,port))
    socket_serveur.listen(5)

    socket_serveur_ssl = context.wrap_socket(socket_serveur, server_side= True)

    return socket_serveur_ssl

# Accepte la connection avec le client
def accepter_connection(socket_serveur_ssl) : 
 
    try :
        socket_client , addr_client = socket_serveur_ssl.accept()
        return socket_client , addr_client
    except : 
        time.sleep(1)
    return None , None

# Envoie au client un message 
def envoie(socket_client, message) :
    message = message.encode()
    socket_client.send(message)


# Réceptionne l'envoie du client 
def reception_contenu(socket_client) : 

    contenu = b''
    while True : 
        
        message_recu = socket_client.recv(MAX_RECV)
        contenu += message_recu

        if len(message_recu) < MAX_RECV : 
            break

    return contenu 