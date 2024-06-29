from Utils import connection, bdd


#Remplacer par les informations de votre serveur
adresse_serveur = '0.0.0.0' 
port = 8080  


def main() :
    # Création de la connection avec la base de données
    connection_db = bdd.create_connection()
    while True :
        global addr_client , socket_client 
        socket_serveur = connection.creation_socket_serveur()    
        socket_serveur_ssl = connection.creation_socket_serveur_ssl(socket_serveur,adresse_serveur ,port)
        socket_client , addr_client = connection.accepter_connection(socket_serveur_ssl)

        # Si le client est connecté, on récupère les données et on les ajoute à la base de données
        if socket_client is not None :
            contenu = connection.reception_contenu(socket_client)
            bdd.add_data(connection_db, contenu)
            socket_serveur_ssl.close()
            socket_client.close()
        else : 
            pass
        socket_serveur.close()

if __name__ == "__main__" :
    main()

