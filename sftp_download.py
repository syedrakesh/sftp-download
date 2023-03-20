import fnmatch
import pysftp
import datetime

# Set up the SFTP connection parameters
host = '127.0.0.1'
username = 'rakesh'
password = 'password'

# Remote Directory Path
remote_directory = '/home/rakesh/Desktop/Rakesh/remote'
# Local Directory Path
local_directory = '/home/rakesh/Desktop/Rakesh/local'
# File Pattern
pattern = 'dam*'
# File Type
# file_type = '.txt'
file_type = ''

# Current Time and Date
now = datetime.datetime.now()

try:
    print('Trying To Connect with', host, ' at ', now.strftime("%Y-%m-%d %H:%M:%S"))

    # cnopts = pysftp.CnOpts()
    # cnopts.hostkeys = None

    # Establish a connection using the above parameters
    # with pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts) as sftp:
    with pysftp.Connection(host=host, username=username, password=password) as sftp:
        print('Connected Successfully at ', now.strftime("%d-%m-%Y %H:%M:%S"), '\n')
        try:
            # change the directory
            sftp.chdir(remote_directory)
            print('Entered Target Directory Successfully.')

            # get a list of all files in the remote directory
            file_list = sftp.listdir()
            # print(file_list)

            # Create a list of files that match the pattern
            pattern = pattern + file_type
            matched_files = fnmatch.filter(file_list, pattern)
            print('Number of Matched Files -> ', len(matched_files), '\n')

            # if the file list is empty, print a message and exit
            if not matched_files:
                print("No matched files found in the remote directory.")
                exit()

            # Download each matched file to the local directory
            counter = 1
            for file_name in matched_files:
                try:
                    # Download the file
                    print(++counter, '. Matched File Name -> ', file_name)
                    print(file_name, '-> Start Downloading at ', now.strftime("%d-%m-%Y %H:%M:%S"), '\n')
                    sftp.get(file_name, f'{local_directory}/{file_name}')
                    print(file_name, '-> Successfully Downloaded at ', now.strftime("%d-%m-%Y %H:%M:%S"), '\n')

                except Exception as e:
                    # Print an error message
                    print(f"Error downloading {file_name}: {e}")

                print('All Matched Files Downloaded Successfully! at ', now.strftime("%d-%m-%Y %H:%M:%S"), '\n')

        except Exception as e:
            # Handle any other exceptions that may occur
            print(f"An Directory error occurred: {e}")

    print('Connection Closed.')
    sftp.close()

except Exception as e:
    # Handle the exception here
    print(f"An SFTP error occurred: {e}")
