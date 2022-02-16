# import socket module
from socket import *
import sys  # In order to terminate the program

# Prepare a sever socket
serverPort = 25565
connectionSocket = socket(AF_INET,SOCK_STREAM)
connectionSocket.bind(('',serverPort))
connectionSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    sock, addr = connectionSocket.accept()
    try:
        message = sock.recv(1024).decode()
        print("HTTP Request recieved: \n", message)
        filename = message.split()[1]

        f = open(filename[1:])
        outputdata = []
        outputdata = f.read().splitlines()
        f.close()


        # Send one HTTP header line into socket
        sock.send("HTTP/1.1 200 OK\n\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            sock.send(outputdata[i].encode())
        sock.send("\r\n".encode())
        sock.close()
        sys.exit()

    except IOError:
        errMsg = "HTTP/1.1 404 NOT FOUND\n\n404 - Not Found"
        sock.send(errMsg.encode())
        sock.close()
        sys.exit()
