import paramiko

paramiko.util.log_to_file("paramiko.log")

# Open a transport
host, port = '127.0.0.1', 22
transport = paramiko.Transport((host, port))

# Auth
username, password = "Me", ""
transport.connect(None, username, password)

# Go!
sftp = paramiko.SFTPClient.from_transport(transport)

files = sftp.listdir()
print(files)
sftp.get('Downloads\AmiCo.txt', 'ami')

# Download
# filepath = "/etc/passwd"
# localpath = "/home/remotepasswd"
# sftp.get(filepath,localpath)
#
# # Upload
# filepath = "/home/foo.jpg"
# localpath = "/home/pony.jpg"
# sftp.put(localpath,filepath)

# Close
if sftp: sftp.close()
if transport: transport.close()
