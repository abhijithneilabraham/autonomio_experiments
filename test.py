import os
import paramiko 
clients = paramiko.SSHClient()
with open('talos_sample/config.json','r') as f:
    import json
    config=json.load(f)["machines"][0]
host = config['TALOS_IP_ADDRESS']
port = config['TALOS_PORT']
username = config['TALOS_USER']
password = config['TALOS_PASSWORD']
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port, username, password)
# client.connect('162.255.116.98', username="root", password="@zIZVAPyMVOlQ3kWkSj8f$")
sftp_client = client.open_sftp()
localpath = 'talos_sample/'
remotepath = './diabetes/'
# sftp.get(remotepath, localpath)
# sftp.close()
# client.close()
sftp_client.chdir(remotepath)
for f in sorted(sftp_client.listdir_attr(), key=lambda k: k.st_mtime, reverse=True):
    sftp_client.get(f.filename,localpath+"/"+f.filename )
    break

sftp_client.close()
client.close()
