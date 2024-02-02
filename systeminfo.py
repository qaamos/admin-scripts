import psutil
import socket

def main():
    # Get hostname and IP address using socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    # Get memory and CPU info using psutil
    memStatus = str(psutil.virtual_memory())
    cpuPercentage = str(psutil.cpu_percent())
    cpuCores = str(psutil.cpu_count())
    cpuFrequency = str(psutil.cpu_freq())

    # Store this information in variable info
    info = ""
    info += "Hostname: " + hostname + "\n"
    info += "IP address: " + IPAddr + "\n"
    info += "Memory status: " + memStatus + "\n"
    info += "CPU percentage: " + cpuPercentage + "\n"
    info += "CPU cores: " + cpuCores + "\n"
    info += "CPU frequency: " + cpuFrequency
    
    # Write information to file Info.txt
    f = open("Info.txt", "w")
    f.write(info)
    f.close()

    return 1

if __name__ == "__main__":
    main()
