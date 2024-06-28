import paramiko
import threading
 
from Utils import server, date

addresse_ip = "0.0.0.0"
port = 2222
server_key = paramiko.RSAKey.from_private_key_file('ssh_key')

addresse_serveur_envoie = "20.199.78.243"
port_envoie = 8080

class SSHServer (paramiko.ServerInterface) : 
    def __init__(self, client_hostname, client_ip):
        self.client_hostname = client_hostname
        self.client_ip = client_ip

    def check_auth_password(self, username: str, password: str) -> int:
        jour, heure = date.get_current_time()
        info_connexion = f"[SSH,{jour},{heure},{self.client_hostname},{self.client_ip},{password}]"
        send_message(info_connexion)
        return paramiko.AUTH_FAILED

def send_message(message) :
    client_socket_ssl = server.creation_socket_ssl(addresse_serveur_envoie,port_envoie)
    client_socket_ssl = server.connect(client_socket_ssl,addresse_serveur_envoie,port_envoie)
    server.send_message(client_socket_ssl,message)
    client_socket_ssl.close()

def ssh_connection (client_socket,client_hostname, client_ip) : 
    transport = paramiko.Transport(client_socket)
    transport.add_server_key(server_key)
    server_ssh = SSHServer(client_hostname, client_ip)
    transport.start_server(server=server_ssh)

def main() : 
    server_socket = server.create_socket(addresse_ip , port)
    
    while True : 
        client_socket , client_ip , client_hostname = server.accept_connexion(server_socket)
        ssh_server = threading.Thread(target=ssh_connection, args=(client_socket,client_hostname, client_ip))
        ssh_server.start()


if __name__ == "__main__" : 
    main()