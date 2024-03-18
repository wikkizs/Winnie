import paramiko
import threading 
 
from Utils import server

addresse_ip = "192.168.1.26"
port = 22
server_key = paramiko.RSAKey.from_private_key_file('ssh_key')

class SSHServer (paramiko.ServerInterface) : 

    def check_auth_password(self, username: str, password: str) -> int:
        print(f"{username}:{password}")
        return paramiko.AUTH_FAILED

def ssh_connection (client_socket) : 
    transport = paramiko.Transport(client_socket)
    transport.add_server_key(server_key)
    server_ssh = SSHServer()
    transport.start_server(server=server_ssh)

def main() : 
    
    server_socket = server.create_socket(addresse_ip , port)
    
    while True : 
        client_socket , client_ip , client_hostname = server.accept_connexion(server_socket)
        print(f"{client_hostname} essaye de se connecter avec l'adresse IP {client_ip}")

        ssh_server = threading.Thread(target=ssh_connection, args=(client_socket,))
        ssh_server.start()


if __name__ == "__main__" : 
    main()