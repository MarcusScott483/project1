from socket import *
import sys

serverName = 'localhost'
serverPort = 25565
clientSocket = socket(AF_INET, SOCK_STREAM)

file = input("File name to get from server: ")

try:
    clientSocket.connect((serverName,serverPort))
except ConnectionRefusedError:
    print("Socket connection did not work. (is the server active?)")
    sys.exit()

print("Connected to: ", serverName, ":", serverPort)

message = ("GET /" + file + "  HTTP/1.1")
clientSocket.send(message.encode())

response = clientSocket.recv(2048)
clientSocket.close()

print("Response from webserver: ")
print(response)
