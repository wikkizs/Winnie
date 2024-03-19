import socket

def create_socket(adresse_serveur,port) : 
    
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

    server_socket.bind((adresse_serveur,port))
    server_socket.listen(5)

    return server_socket


def accept_connexion(server_socket) : 

    client_socket,addr_info = server_socket.accept()

    # On récupère l'adresse de l'utilisateur qui c'est connecté
    client_ip = addr_info[0]

    # On récupère le nom de sa machine
    try : 
        client_hostname = socket.gethostbyaddr(client_ip)[0]

    except : 
        client_hostname = "Inconnu"
    
    return client_socket , client_ip , client_hostname 