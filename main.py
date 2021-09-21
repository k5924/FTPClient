from ftplib import FTP
import sys

while True:

    print("Press CTRL+C to quit the program\n")
    host = input("Enter a host to connect to> ")
    user = input(
        "Enter the username to use when connecting to that host> ")
    password = input("Enter the password to connect to that host> ")

    operation = input(
        "What would you like to do\nRead data from local text file to remote text file (rb)\nWrite data from remote text file to local text file (wb)\n> ")

    if operation == 'rb' or operation == 'wb':
        localFileName = input("Enter the local file name> ")
        remoteFileName = input("Enter the remote file name> ")
        try:
            with FTP(host) as ftp:
                ftp.login(user=user, passwd=password)
                print(ftp.getwelcome())

                if operation == 'rb':
                    with open(localFileName, operation) as file:
                        ftp.storbinary('STOR ' + remoteFileName, file)
                else:
                    with open(localFileName, operation) as file:
                        ftp.retrbinary(
                            'RETR ' + remoteFileName, file.write, 1024)
                        # if not all data is written from the remote file to the local file increase from 1024 bytes to a larger value

            ftp.quit()
            sys.exit()
        except Exception as e:
            print(e)
            sys.exit(1)
    else:
        print("Invalid Operation Please Try Again")
