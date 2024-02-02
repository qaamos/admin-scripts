import socket

def main():

    # Define server address
    server = "127.0.0.1"
    port = 8080

    # Connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server,port))

    # Get IP address from user
    userIPAddress = input("Enter IP address: ")

    # Send IP address to server
    client.send(userIPAddress.encode())
    # Receive answer from server
    answer = client.recv(1024)
    # Decode and print the answer
    print(answer.decode())

    # Close the connection
    client.close()

    return 1

if __name__ == "__main__":
    main()
