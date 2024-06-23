import socket
import time
import socket
import ssl


# Certificat à copier afin de pouvoir l'éxecuter en .exe
ca_cert = """
-----BEGIN CERTIFICATE-----
MIIFXzCCA0egAwIBAgIUXvTjadcF+3ivyKON2yNWuGnwtGcwDQYJKoZIhvcNAQEL
BQAwPzELMAkGA1UEBhMCRlIxDTALBgNVBAgMBG9pc2UxITAfBgNVBAoMGEludGVy
bmV0IFdpZGdpdHMgUHR5IEx0ZDAeFw0yNDA2MjMxNDI0NDNaFw0yNTA2MjMxNDI0
NDNaMD8xCzAJBgNVBAYTAkZSMQ0wCwYDVQQIDARvaXNlMSEwHwYDVQQKDBhJbnRl
cm5ldCBXaWRnaXRzIFB0eSBMdGQwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIK
AoICAQDTMug7Q1MYnAG1f+7w0+gAYcuy2GO7DORkYAqBRYCYN1arvEoCvHII1Z6j
L8JYHsXxMhpzWb5GcxwVbCr6Ry7uKAVE7nCbc4XiUPGRuOI8m3yE1HkY2xr7TzTr
5/6wOVUlATl5k0jCHPMsI3/HGbx8TRRDHXKvDOgl8Za7AhXisNQ/OV/cUFGr3Pao
wrEIk9BHVh25lwwk6yRG/DeVFjhOzbK6IZMljRf0SukaIxwPk+ALJnHEFTcz6RDh
Xg1AfHwP8k0mIe/xGqHMZrVePCFACfJdcH16njfWMHc1yvt0RA6WgVPVrCet1ePp
YeL4ScW+IqeVimEhEujYR7sKgyroln9Ypp8i1ZXfYnYFVU4flGrEMulPlNWWGKVW
6R2wEY7l+ilhxiVf5pqArpV+kltRVkvdr2ywkCrcq9LQ5GgU1XHc2WBdkP5zjILo
SWGvyFKBPPG84eHCJio4jbQyelOoM3zX5S0VqdicfbpBQiIP4Bz7WvJFNlcZGPnj
DqBN+I4CQqHjKfkyQuoFvcKnJkB+D1XYkDcOK+KgEwRfV3CajljGe3TjSpg2JS+G
tYAzrceehLDzRSGaDfOYz6EeT9GYvdKTkzByS7pdtCM3FAvQTeZaOmKlVGhqn5PI
bR69FsxQsq/c/U/YMiG4jmIkVMDDcuPJt5UBDjnA/JH3KSYRQQIDAQABo1MwUTAd
BgNVHQ4EFgQU0x4n0fQIpdhoNut68lYo5U4aS38wHwYDVR0jBBgwFoAU0x4n0fQI
pdhoNut68lYo5U4aS38wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOC
AgEATlj72CabKINnw3BppeSnC+2SkuLNDS2brSswNLUdC4kNwPR02r+wVI94baNS
0oE6BoPN0ByjLz8tdK6PjPtZjGqPTw3Vgu0Pczi8U9eIC10oG98XH/Nqgp+8crTR
a8IRf1xZUwK6oAB002t3K/wPY6wg3j/2TY5n/o9bT7CIJEkT//rgRtQ+aOL+1EIi
5lDAXKwhgid0Ipz0HGbe0Fs6/Q8S0b2syL2xk6GgoQLbOnHoRNGMuziIghmfI+sk
GGM1nAXf023NJlhzZTnLYr0yuuBdn8cN6fk+CgcL8BOgDrdjSOQKyjog1mXbzOsf
1HI15MsRRWO7soi7v39uz1NVAruBdfb5Re41pBY3cucTOhskp+iu6InTjJf5sehX
J9ETOAW+Ksdb1OubpZ4CpuH1yqgYQZDRp9P8hnHL/N0jldmRTL4qPQyQUcmSXYKf
RGqGLNAJG3a97qHHjfLwvmlt7myZGqPuv8GlVx2fI3ZW6Uq0s39qBSVgAn+gWqgz
I2IqbAQ9cUakseJ3EKuIxxXBCsYSrnEhYsCjbf1mthUFKsKPRtXFoZjtC62GF7eo
lYeqWVBT0hJP6aykXPPNMUElMuoN7D7IPJ2UhiAdRaw+Igsp5mp+ZF6RdwRiG1Po
Pex5o3ubqNKStSuuX/9HGQ1jIIuTK0LM8R1osqUkCq/Eqlw=
-----END CERTIFICATE-----
"""

def create_socket(adresse_serveur,port) : 
    
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

    server_socket.bind((adresse_serveur,port))
    server_socket.listen(5)

    return server_socket


def accept_connexion(server_socket) : 

    client_socket,addr_info = server_socket.accept()

    # On récupère l'adresse de l'utilisateur qui c'est connecté
    client_ip = addr_info[0]

    # On récupère le nom de sa machine
    try : 
        client_hostname = socket.gethostbyaddr(client_ip)[0]

    except : 
        client_hostname = "Inconnu"
    
    return client_socket , client_ip , client_hostname 


def creation_socket_ssl(addresse_serveur,port) :
    
    #Creation de la socket client
    socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #Creation du context SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(cadata=ca_cert)

    #Creation de la socket SSL
    socket_client_ssl = context.wrap_socket(socket_client,server_hostname=addresse_serveur)

    return socket_client_ssl
    
def connect(socket_client_ssl,addresse_serveur_envoie,port_envoie) : 
    while True :
        try :
            print("3.1\n") 
            socket_client_ssl.connect((addresse_serveur_envoie,port_envoie))
            return socket_client_ssl
        except Exception as e : 
            print(e)
            time.sleep(1)

# Fonction qui envoie le fichier de capture au serveur
def send_message(socket_client_ssl,message) :
    bytes_message = message.encode()
    socket_client_ssl.sendall(bytes_message)