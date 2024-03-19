import socket
import threading
from Utils import server


adresse_serveur = '192.168.1.26'
port = 100

def tcp_connexion(server_socket) : 
    client_socket , client_ip , client_hostname = server.accept_connexion(server_socket)
    print(f"{client_hostname} essaye de se connecter avec l'adresse IP {client_ip}")
    server_socket.close()

def main() : 
    while True : 
        print("Test")
        server_socket = server.create_socket(adresse_serveur,port)

        thread_connexion = threading.Thread(target=tcp_connexion, args= (server_socket,))
        thread_connexion.start()
        thread_connexion.join()


if __name__ == "__main__" : 
    main()