import threading
from Utils import server


adresse_serveur = '0.0.0.0'
port = 100
filename = "ip_hostname.txt"

addresse_serveur_envoie = "20.199.78.243"
port_envoie = 8080

def send_message(message) :
    client_socket_ssl = server.creation_socket_ssl(addresse_serveur_envoie,port_envoie)
    client_socket_ssl = server.connect(client_socket_ssl,addresse_serveur_envoie,port_envoie)
    server.send_message(client_socket_ssl,message)
    client_socket_ssl.close()

def tcp_connexion(server_socket) : 
    
    while 1 : 
        client_socket , client_ip , client_hostname = server.accept_connexion(server_socket)
        print(f"{client_hostname} essaye de se connecter avec l'adresse IP {client_ip} sur le port {port}.")
        info_connexion = f"[TCP,{client_hostname},{client_ip},{port}]"
        client_socket.close()
        send_message(info_connexion)
        


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