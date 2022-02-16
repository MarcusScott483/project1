from socket import *
import sys

serverName = 'localhost'
serverPort = 25565
clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    clientSocket.connect((serverName,serverPort))
except ConnectionRefusedError:
    print("Socket connection did not work. (is the server active?)")
    sys.exit()

print("Connected to: ", serverName, ":", serverPort)

message = ("GET /index.html HTTP/1.1")
clientSocket.send(message.encode())

response = clientSocket.recv(1024)
clientSocket.close()

print("Response from webserver: ")
print(response)
