import threading
from Utils import server


adresse_serveur = '192.168.1.26'
port = 100

def tcp_connexion(server_socket) : 
    
    while 1 : 
        client_socket , client_ip , client_hostname = server.accept_connexion(server_socket)
        print(f"{client_hostname} essaye de se connecter avec l'adresse IP {client_ip} sur le port {port}.")

        client_socket.close() 
    

def main() : 
    # Création de la socket  
    server_socket = server.create_socket(adresse_serveur,port)
    
    # Gère les connexion via un Thread
    thread_connexion = threading.Thread(target=tcp_connexion, args= (server_socket,))
    thread_connexion.start()
    thread_connexion.join()

    server_socket.close()


if __name__ == "__main__" : 
    main()