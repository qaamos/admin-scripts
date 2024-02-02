import os

def main():
    
    # 1.
    # Add user Jane belonging to group finance
    os.system("useradd -G finance Jane")

    # Change owner of /Accounts to Jane
    os.system("chown Jane /Accounts")

    # Change owner's (aka Jane's) permissions of /Accounts to read/write/execute
    os.system("chmod -R u=rwx /Accounts")

    # 2.
    # Add user John belonging to group logistics
    os.system("useradd -G logistics John")

    # Change owner of /Transport to John
    os.system("chown John /Transport")

    # Change owner's (aka John's) permissions of /Transport to read/write
    os.system("chmod -R u=rw /Transport")

    # 3.
    # Remove all owner's (aka John's) permissions of /Transport
    os.system("chmod -R u= /Transport")

    return 1

if __name__ == "__main__":
    main()
