import socket
import random
import time

msgFromClient       = "Bladimir"
#bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

for i in msgFromClient:
    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket
    print("Intentando enviar")

    #Retardo del medio
    retardo = random.randint(500,3000)/1000
    time.sleep(retardo)

    #Perdida aleatoria de 30%
    if (random.randint(1,100) < 30):
        print('Me perdi, soy {caracter}'.format(caracter=i))
    else:
        UDPClientSocket.sendto(str.encode(i), serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)