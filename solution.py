# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start

    # Fill in end
    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr = serverSocket() # Fill in start      #Fill in end
        try:
            try:
                    message = connectionSocket.recv(1024).decode() # Fill in start    #Fill in end
                message.decode().upper()
                filename = message.split()[1]
                print ("File name is: "), filename
                f = open(filename[1:])
                outputdata = f.read() # Fill in start     #Fill in end

                # Send one HTTP header line into socket.
                # Fill in start
                connectionSocket.send("HTTP/1.1 200 OK".encode()) # Prints the 200 OK requirement
                # Fill in end

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                # Send response message for file not found (404)
                # Fill in start
                print("404 Not Found")
                connectionSocket.send("HTTP/1.1 404 Not Found".encode())
                # Fill in end

                # Close client socket
                # Fill in start
                connectionSocket.close()
                # Fill in end
        except (ConnectionResetError, BrokenPipeError):
            pass
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)

