import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Remplacer les valeurs suivantes par les informations de votre base de données
host_name = "localhost"
user_name = "honeypots"
user_password = "tcmbddhonneypot"
db_name = "Honeypots"

# Création des tables
create_tcp_table = """
CREATE TABLE IF NOT EXISTS TCP (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Jour DATE NOT NULL,
    Heure TIME NOT NULL,
    Hostname VARCHAR(255) NOT NULL,
    IP VARCHAR(255) NOT NULL,
    Port INT NOT NULL
);
"""

create_ssh_table = """
CREATE TABLE IF NOT EXISTS SSH (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Jour DATE NOT NULL,
    Heure TIME NOT NULL,
    Hostname VARCHAR(255) NOT NULL,
    IP VARCHAR(255) NOT NULL,
    Mdp VARCHAR(255) NOT NULL
);
"""

# Création de la connection avec la base de données
def create_connection() :
    
    connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        passwd = user_password,
        database = db_name
    )
    
    return connection

# Fonction qui exécute une requête dans la base de données liée à connection
def execute_query(connection, query, data=None) :
    cursor = connection.cursor()
    try:
        if data :
            cursor.execute(query, data)
        else :
            cursor.execute(query)
        connection.commit()
    except Error as e :
        print(e)

# Fonction qui transforme les données reçues et les insère dans la base de données
def add_data(connection,data) :
    data = data.decode()
    data = data.strip("[]")
    data_list = data.split(',')
    
    if data_list[0] == "TCP":
        
        insert_query = """
        INSERT INTO TCP (Jour, Heure, Hostname, IP, Port)
        VALUES (%s, %s, %s, %s, %s)
        """
        tcp_data = (data_list[1], data_list[2], data_list[3], data_list[4], int(data_list[5]))
        execute_query(connection, insert_query, tcp_data)
        
    elif data_list[0] == "SSH":
        
        insert_query = """
        INSERT INTO SSH (Jour, Heure, Hostname, IP, Mdp)
        VALUES (%s, %s, %s, %s, %s)
        """
        ssh_data = (data_list[1], data_list[2], data_list[3], data_list[4], data_list[5])
        execute_query(connection, insert_query, ssh_data)
        
    else:
        print("Donnees non reconnues.")