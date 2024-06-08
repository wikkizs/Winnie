import socket
import time
import socket
import ssl


# Certificat à copier afin de pouvoir l'éxecuter en .exe
ca_cert = """
-----BEGIN CERTIFICATE-----
MIIFXzCCA0egAwIBAgIUL2MTGc3qvWASsP8zX5H1eOhDlggwDQYJKoZIhvcNAQEL
BQAwPzELMAkGA1UEBhMCRlIxDTALBgNVBAgMBG9pc2UxITAfBgNVBAoMGEludGVy
bmV0IFdpZGdpdHMgUHR5IEx0ZDAeFw0yNDA1MjMyMDAxMjJaFw0yNTA1MjMyMDAx
MjJaMD8xCzAJBgNVBAYTAkZSMQ0wCwYDVQQIDARvaXNlMSEwHwYDVQQKDBhJbnRl
cm5ldCBXaWRnaXRzIFB0eSBMdGQwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIK
AoICAQCWfgz+cH5eJmKBKYON7HlXluiqCVvDuTCAnJXfn4LU7k7v7w6ZM7mmsHBf
6zuuLlwFZN45WiNPl4ZFcIFsLKlSYzzm69zhHsfIOdpv17xH8qlnwQQ0U/Tj4ouq
ZXjkJ/4yaijBIwlznkIx+J23HGWg3HbDomAcuhhhv8TgUg9poXaKdG6SNsH8+OTD
aJ5g+KvUtV+4DelgaQiPexFhJsB16lzb/8nvAJ8m04SFkOd0LCdhMLrUjP9N2UEQ
XKDRs14WtXAjhJYnBBUGMRErRRtYkt06gUnUczwn0k4cDezXqbrp08cr11m7M704
RckI6bJthaDkVS5q7dAA9jwBeIoMJtJm1DCWFCN/850ktWTbH98TOkX0pvV4a2kO
HMSxtPUMMwRII2RkcWZZ5s0iJb7Qk4RscyFerIjX7dQhE1IpRhnXk3WQhJjoAKxc
AGrnigdXkO1Cg+TYJLiwoVvzSsTT2BT7T4ZgNdDKOgFJewCXbCJB+FVTgarTOXwm
RjawuMO8NN8jRY6BHb5crqaGfv0Mft6u+4agGfvpC4gvBxIQg1KIyUQnq7z4xtIQ
o01rdwWs0waMTlI/RcD44fuIhDN/9IlIdrBV46uT10xd9DmLqSh1LnQblmR1kaJK
oYxLXJFWJpR+qKIUFTErkd8CfSA/7p8ep8pTD91QKjSyYxqWFQIDAQABo1MwUTAd
BgNVHQ4EFgQUctLzw2H/Xu7diFZ7axG+bNfAIJ8wHwYDVR0jBBgwFoAUctLzw2H/
Xu7diFZ7axG+bNfAIJ8wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOC
AgEAXFolVflsJ1YgwnwwSjTakFEBlJ3Y2KPw1j5KRWtxeZoys9YFy2cDFOMMSEh9
KjNfU9j0CTwHF9EschM5chDfIc8lMOWut+tE0/1pL2WlMajcEE6+xv3KuYHEu1BC
FIyumxCN1tSk9O7keMmoZvamePwx7BXITZP24weDwdyLw0yzGA8kond4Pe4JOLO1
vFQ6AYhUw1CqJbNx/6PgJb8YOCKvJonf4TI/rSugh2egNH7C8/1PkVU+glkW3oQi
6I+KroQ/5JeVeX/ZeHiAXDuuQtpTyhSw0D0u/8jhoLwLtklkn3x7HUx73LLdg6sQ
D3y1G0yNotEl2aEum29ucCBx5E6o6v3apW1mpFw8OUelFk9/jB3NECr5RPkhfBsS
Oa/K34BWQ4QspEbW2ScNsi9dhR37K4EeEQP7urTwIFtBM+CvdwvYCMZDwpLmWbvm
XYDEi41xtyAzujKFOgDJM5cQvzNkESHZYMyVbCSZ9FakN8G+m+4xG9ScZ4v5M+kf
WI+rVGHBXhQrfEt7z62lc9UizdOBY09Do1xrLNNfMk5N456PU7m3awDdoTinjVVN
Ifu42XvHOe4iive3iPjep1nLm1/Dpr/99kdqzrduzRt5NDmndveMhnd0MHnuzx9B
XeU5Q95o1pyN8+5bnRxWCGWZuNj4ux6eX0muWrd9HXIXq2g=
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