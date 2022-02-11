# import os
# import paramiko
# host = os.environ['TALOS_IP_ADDRESS']
# port = os.environ['TALOS_PORT']
# username = os.environ['TALOS_USER']
# password = os.environ['TALOS_PASSWORD']


# command = "ls"

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(host, port, username, password)

# stdin, stdout, stderr = ssh.exec_command(command)
# lines = stdout.readlines()
# print(lines)


def splitDictByVals(d,n_splits=2):
    dicts=[{} for i in range(n_splits)]
    def _chunkify(lst,n):
     return [lst[i::n] for i in range(n)]
    for k,v in d.items():
        for i in range(n_splits):
            dicts[i][k]=_chunkify(v, n_splits)[i]
    return dicts
        
   
        
        
        


print(splitDictByVals({
    'first_neuron': [12, 24],
    'activation': ['relu', 'elu','selu'],
    'batch_size': [10, 20,12]
}
))
