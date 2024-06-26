import threading
from Utils import server, date

# Remplacer par les informations de votre serveur
adresse_serveur = '0.0.0.0'
port = 100

#Remplacer par l'adresse de votre serveur
addresse_serveur_envoie = "20.199.78.243"
port_envoie = 8080

# Envoie message vers le serveur via une socket SSL
def send_message(message) :
    client_socket_ssl = server.creation_socket_ssl(addresse_serveur_envoie,port_envoie)
    client_socket_ssl = server.connect(client_socket_ssl,addresse_serveur_envoie,port_envoie)
    server.send_message(client_socket_ssl,message)
    client_socket_ssl.close()

# Fonction qui gère les connexions TCP et récupère les informations sur les connexions
def tcp_connexion(server_socket) :     
    while 1 : 
        client_socket , client_ip , client_hostname = server.accept_connexion(server_socket)
        jour, heure = date.get_current_time()
        info_connexion = f"[TCP,{jour},{heure},{client_hostname},{client_ip},{port}]"
        client_socket.close()
        send_message(info_connexion)
        


def main() : 
    # Création de la socket  
    server_socket = server.create_socket(adresse_serveur,port)
    
    # Gère les connexions via un Thread
    thread_connexion = threading.Thread(target=tcp_connexion, args= (server_socket,))
    thread_connexion.start()
    thread_connexion.join()

    server_socket.close()


if __name__ == "__main__" : 
    main()