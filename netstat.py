import os

def main():

    # Execute netstat, save output to netstat.txt
    os.system("netstat -s | cat > netstat.txt")

    # Extract summary of TCP protocol
    os.system("sed -n '/Tcp:/,/Udp:/{/Udp:/!p}' netstat.txt")

    return 1

if __name__ == "__main__":
    main()
