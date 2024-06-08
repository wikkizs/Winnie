from Utils import gestion_fichier , connection


# Adresse du serveur
# Mettre l'adresse de votre serveur
adresse_serveur = '192.168.194.135' 
port = 8080  
MAX_RECV = 4096 


def main() : 
    while True :
        global addr_client , socket_client 
        gestion_fichier.creation_repertoire("fichier_recu")
        socket_serveur = connection.creation_socket_serveur()    
        socket_serveur_ssl = connection.creation_socket_serveur_ssl(socket_serveur,adresse_serveur ,port)
        socket_client , addr_client = connection.accepter_connection(socket_serveur_ssl)

        if socket_client is not None :
            contenu = connection.reception_contenu(socket_client)
            gestion_fichier.print_file(addr_client,contenu)
            socket_serveur_ssl.close()
            socket_client.close()
        else : 
            pass
        socket_serveur.close()





if __name__ == "__main__" :
    main()

