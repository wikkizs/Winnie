# Winnie

## Description

Winnie est une application de surveillance réseau qui surveille les connexions TCP et SSH entrantes sur un serveur. Les informations de connexion sont capturées, envoyés sur un autre serveur où elles sont enregistrées dans une base de données MariaDB.
## Installation

Pour utiliser ce honeypot, suivez les étapes suivantes :

1. Clonez le dépôt depuis GitHub :

    ```bash
    git clone https://github.com/wikkizs/Winnie.git
    cd votre-projet
    ```

2. Installez les dépendances nécessaires à l'aide de `pip` et du fichier `requirements.txt` :

    ```bash
    pip install -r requirements.txt
    ```
## Contenu du Dossier

- **Port_surveillance :**
  - **get_ip_hostname.py**: Script principal gérant la surveillance des connexions TCP.
  - **Utils :**
    - **date.py**: Module pour obtenir la date et l'heure actuelles.
    - **server.py**: Module contenant des fonctions pour la gestion des sockets et SSL.
- **Serveur :**
  - **key_gen.py**: Script pour générer les clés SSL nécessaires.
  - **serveur.py**: Script principal du serveur qui accepte les connexions et les enregistre dans la base de données.
  - **Utils :**
    - **bdd.py**: Module pour la gestion de la base de données MySQL.
    - **connection.py**: Module contenant des fonctions pour la création et la gestion des sockets.
- **SSH :**
  - **ssh_honeypots.py**: Script pour simuler un serveur honeypot SSH qui enregistre les tentatives de connexion et les mots de passe rentrées.
  - **Utils :**
    - **server.py**: Module contenant des fonctions pour la gestion des sockets et SSL.
    - **date.py**: Module pour obtenir la date et l'heure actuelles.

## Utilisation

Pour utiliser le projet :

1. **Configuration du Serveur** :
   - Remplacez les adresses IP et les ports dans les scripts `get_ip_hostname.py`, `serveur.py` et `ssh_honeypots.py` par les informations de votre serveur.
   - Remplacez le certificat SSL dans `server.py` par le cerficate du serveur cible. 

2. **Génération des Clés SSL** :
   - Lancez `key_gen.py` pour générer les clés SSL nécessaires pour la communication sécurisée.

3. **Base de Données** :
   - Configurez les informations de connexion à la base de données MariaDB dans `bdd.py`.

4. **Exécution** :
   - Lancez les scripts principaux `get_ip_hostname.py` et `ssh_honeypots.py` sur le serveur que vous souhaitez surveiller. 
   - Lancer le script `serveur.py` sur le serveur où se trouve votre base de données.

## Notes

- Assurez-vous d'avoir installé les packages Python nécessaires, tels que `paramiko`, `mysql-connector-python`, `openSSL`, etc.