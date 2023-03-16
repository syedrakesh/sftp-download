import fnmatch
import pysftp

# Set up the SFTP connection parameters
host = 'localhost'
username = 'root'
password = 'password'

# Remote Directory Path
remote_directory = '/usr/sap/tmp/DAM'
# Local Directory Path
local_directory = '/home/rakesh/Desktop/Rakesh'
# File Pattern
pattern = 'ASSET_DUMP*'
# File Type
file_type = '.txt'

try:
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    # Establish a connection using the above parameters
    # with pysftp.Connection(host=host, username=username, password=password) as sftp:
    with pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts) as sftp:
        try:
            # change the directory
            sftp.chdir(remote_directory)

            # get a list of all files in the remote directory
            file_list = sftp.listdir()

            # create a list of files that match the pattern
            pattern = pattern + file_type
            matched_files = fnmatch.filter(file_list, pattern)

            # if the file list is empty, print a message and exit
            if not matched_files:
                print("No matched files found in the remote directory.")
                exit()

            # download each matched file to the local directory
            for file_name in matched_files:
                try:
                    # download the file
                    print(file_name, '-> Start Downloading.')
                    sftp.get(file_name, f'{local_directory}/{file_name}')
                    print(file_name, '-> Successfully Downloaded.')

                except Exception as e:
                    # print an error message
                    print(f"Error downloading {file_name}: {e}")
        except Exception as e:
            # handle any other exceptions that may occur
            print(f"An Directory error occurred: {e}")

except Exception as e:
    # handle the exception here
    print(f"An SFTP error occurred: {e}")
