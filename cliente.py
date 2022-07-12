import socket
import random
import time


##### Configuración #####

# IMPORTANTE: VALIDATOR debe coincidir con el VALIDATOR del Server
VALIDATOR = 2           # Constante de Residuo
WAIT_TIME = 2000        # Tiempo de espera de Respuesta
random.seed(1000)

##### Funciones ##### 
def CRC_Client(msg):
    ascii = ord(msg)
    return msg + str(ascii % VALIDATOR)


def main():
    msgFromClient       = "Bladimir"
    #bytesToSend         = str.encode(msgFromClient)
    serverAddressPort   = ("127.0.0.1", 20001)
    bufferSize          = 1024

    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    #Asignando Tiempo de Espera
    UDPClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, WAIT_TIME)

    # Send to server using created UDP socket
    print("INICIANDO PROCESO DE ENVIO")

    i = 0       # Puntero del caracter a enviar 
    cont = 0    # Cantidad de Reintentos

    while (i < len(msgFromClient)):
        UDPClientSocket.sendto(str.encode(CRC_Client(msgFromClient[i])), serverAddressPort)
        try:
            inicio = time.time()
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            ACK = msgFromServer[0].decode()
            fin = time.time()
            print("ACK(): {msg}, Tiempo de Respuesta: {t} \n".format(msg=ACK, t = fin-inicio))
            i += 1
            cont = 0
        except:
            cont += 1
            print("TIMEOUT. Letra : {c} , Reintento : {n}".format(c=msgFromClient[i], n = cont))

main()