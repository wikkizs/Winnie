import socket
from Utils import server


adresse_serveur = '192.168.1.26'
port = 100


def main() : 
    port = 100 
    server_socket = server.create_socket(adresse_serveur,port)
    client_socket , client_ip , client_hostname = server.accept_connexion(server_socket)
    print(f"{client_hostname} essaye de se connecter avec l'adresse IP {client_ip}")
    server_socket.close()


if __name__ == "__main__" : 
    main()