import socket
import time
import socket
import ssl


# Certificat à copier afin de pouvoir l'éxecuter en .exe
ca_cert = """
-----BEGIN CERTIFICATE-----
MIIFXzCCA0egAwIBAgIUIocqWpx9UVKAeOa8gYnnTJXXm4YwDQYJKoZIhvcNAQEL
BQAwPzELMAkGA1UEBhMCRlIxDTALBgNVBAgMBG9pc2UxITAfBgNVBAoMGEludGVy
bmV0IFdpZGdpdHMgUHR5IEx0ZDAeFw0yNDA2MjMxNDMwMTVaFw0yNTA2MjMxNDMw
MTVaMD8xCzAJBgNVBAYTAkZSMQ0wCwYDVQQIDARvaXNlMSEwHwYDVQQKDBhJbnRl
cm5ldCBXaWRnaXRzIFB0eSBMdGQwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIK
AoICAQDQbBw7Nt/mcO/KLJ22Hd4ZF/QNv/Q+dfBlrtaXTRhFnIhwBN87guLVu2aQ
r/vrqqP07bP3CV9m98VDZwfpSEr0qwzY7FaVnJcpRaFzpzXuTsbTkn/JnxlRemjF
XLWrIrmsESbfg++Vu8vcsVMbc4Xhe2nUVSaNGiwEYIV+Fih5zRlomHntfNAZue4r
1hnydLelallovIlS7NsAXeE9QmYrDmdcDptR9kd8WCdB4/43TzMKH525RGgpG1pS
utUvpl14Dcs/89Yc+ph7kj7SY19cS32s+lzIjc5mhJTWwfHr+9Bh48/YkBG1Vr3M
//nq0+hGbvArJ7qaRutuoaMEXrFdWGUE/dyJRkZCX+F3A3W+0B0gTL4QXOxRfPXJ
SobRRgyQl5tGAg5Eht727vBgoFez4a8yURs77Dq7w1EsQhrOcGVkZR2XFQ3uZyU0
da8lRx0MOh/C2dX0i3uRxU8+AJ2jXC2wTzU+P68olg27znguIgA83j/I3MDOxDQ6
WaQYdhSEPmPwQa1b37YB7q7QP4ZeFxQ8pP0c1e47mgJ01yDophd7Fev8a26SdYqn
r8m7qckw2G5bArZM1qwzlrJsYgig7+MUTsYHeODN6JxzHuYEBA9YNjEqRC3kgvoa
oSjjZpjxkx2wcHLuDHTxnesjI98Hd6n1Jea1ciTfQ0WF9SbHIQIDAQABo1MwUTAd
BgNVHQ4EFgQUMzVjGiDVdW1/SoWkiCEh35vURZgwHwYDVR0jBBgwFoAUMzVjGiDV
dW1/SoWkiCEh35vURZgwDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOC
AgEAN3nDycHQMVDfo1mf/HaGWlR94xLYHiUXCbQHNkrKGYB4j+cefMXXBd/hNnEL
i5nSjV+HrPM0I/HJixEFe1WwmfZsCVHh49T84O0C9/8CMgIhOJM/QNi4HOk3P9vv
J7Y+PeZ5dvKyheBa0RbQs4BCeTzyxUfuIgs7GmDDCQfxwb1GiL3/K9cvDIt5lT7D
RAQRqdlyx04mMl7V5jIbxD4YHsVVkl8xIKgY8cgZXejL6GNmZnYj5ZWPwPKiaoe0
JMuxCLVlA2jm3TNfJRHlNMQs7i8lm+N1JrUs1T20EkPbw77AFA1lX3PjJjIJzEEk
K/VDPxAumYPv83hAExRnJBb9hrmIbgSydgMOAz9U434jmY3asBJFpFFXEzhAluns
X9lp/xStWSixJNTXNAz2cYrjRyZgtmEWxqiNoWf921g6RoeShns+fBU8FVqvHgYQ
fvjFtH+D1NYAt/MGEy815hqRBxfy+Ws9j5vvpp0xs9qZj4OLZZRdlrjIXPNwOm1y
AgnnjIYx0Jm/YYUhtfmzxx0QBMNyeQanUR8M1HB7G7Qqr8bNzsUDJY8vhE+FtSkT
NsnV/sYSR2zmsyg472cZ7NWn7JKu4OkEeIbkuaIN+5tPMGZCNOEz3ru4Z7b+Msz/
xMxzeWbx/gDQNUKpLN2p49WkHkiUNwgYIpYBt1sA2GEmbLs=
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
            socket_client_ssl.connect((addresse_serveur_envoie,port_envoie))
            return socket_client_ssl
        except Exception as e : 
            print(e)
            time.sleep(1)

# Fonction qui envoie le fichier de capture au serveur
def send_message(socket_client_ssl,message) :
    bytes_message = message.encode()
    socket_client_ssl.sendall(bytes_message)