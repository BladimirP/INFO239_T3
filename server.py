import socket
import random
import time

##### Configuración #####

# IMPORTANTE: VALIDATOR debe coincidir con el VALIDATOR de los clientes
VALIDATOR = 2       # Constante de Residuo

LOST = 0.3          # Probabilidad de perder un paquete
MIN = 500           # Minimo de tiempo de repuesta
MAX = 3000          # Max tiempo de respuesta
random.seed(1000) 

##### Funciones ######

# Valida si code word ( ASCII + Check Value ) es divisible por una constante definida:
# SI es divisible: Se asume que el bloque de datos se encuentra libre de errores
# NO es divisible: El bloque de datos fue modificado (SE DAÑO).
def CRC_Server(msg):
    ascii = ord(msg[0]) + int(msg[1:])
    if (ascii % VALIDATOR == 0):
        return 0
    else:
        return 1


def main():
    localIP     = "127.0.0.1"
    localPort   = 20001
    bufferSize  = 1024
    #msgFromServer       = "Caracter Aceptado"
    #bytesToSend         = str.encode(msgFromServer)


    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))

    print("SERVER DISPONIBLE")

    # Listen for incoming datagrams
    while(True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0].decode()
        address = bytesAddressPair[1]
        
        if (random.random() < LOST):
            print("EL mensaje se perdido")

        elif(CRC_Server(message)):
            print('EL mensaje se daño')

        else:
            print("Message from Client: {}".format(message[0]))
            retardo = random.randint(MIN,MAX) / 1000
            print(f"RETARDO : {retardo} sec")
            time.sleep(retardo)

            # Sending a reply to client
            UDPServerSocket.sendto(str.encode(message[0]), address)
            print("PUERTO DISPONIBLE \n")

            # Problema de Recepcion
            
            # Solucion 1:
            #UDPServerSocket.close()
            #UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            #UDPServerSocket.bind((localIP, localPort))
            
            # Solucion 2:
main()