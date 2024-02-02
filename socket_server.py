import socket
from netaddr import IPAddress

def main():

    # Define server address
    serverAddr = "127.0.0.1"
    port = 8080

    # Create server and bind to defined IP address
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((serverAddr,port))

    # Start listening for client
    server.listen(1)
    print("Server is listening...")

    # Connect to client
    clientConnection, clientAddress = server.accept()
    print("Connected!")

    # Receive user data and decode it
    userIP = clientConnection.recv(1024)
    userIP = userIP.decode()
    # Convert to netaddr IP address
    userIP = IPAddress(str(userIP))
    # Convert to binary
    userIPBin = userIP.bits()
    
    # Send response and close connection
    clientConnection.send(userIPBin.encode())
    clientConnection.close()
    server.close()

    return 1

if __name__ == "__main__":
    main()
