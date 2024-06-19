from ftplib import FTP

def get_ftp_files(hostname, username, password):
    # Connect to the FTP server
    ftp = FTP(hostname)
    ftp.login("", "")

    # Get list of files and directories
    files_and_dirs = ftp.nlst()
    ftp.voidcmd('TYPE I')
    # Filter out only the files
    files = [f for f in files_and_dirs if ftp.size(f) >= 0]  # Files have a size >= 0

    # Print or process the list of files
    print("Files on the FTP server:")
    for file in files:
        print(file)

    # Close the FTP connection
    ftp.quit()

# Replace with your FTP server details
hostname = 'localhost'
username = 'hirthik'
password = '12345'

get_ftp_files(hostname, username, password)

