from Utils import gestion_fichier , connection, bdd


# Adresse du serveur
# Mettre l'adresse de votre serveur
adresse_serveur = '0.0.0.0' 
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
            print(contenu)
            connection_db = bdd.create_connection()
            bdd.add_data(connection_db, contenu)
            socket_serveur_ssl.close()
            socket_client.close()
        else : 
            pass
        socket_serveur.close()





if __name__ == "__main__" :
    main()

