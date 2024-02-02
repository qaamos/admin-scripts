import socket

def main():
    # Retrieve and print IP address
    IPAddress = socket.gethostbyname("www.github.com")
    print(IPAddress)
    return 1

if __name__ == "__main__":
    main()
