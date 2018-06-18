import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.24.4.4', username='cirros', key_filename='/home/devstack/Desktop/Sensor_login/test2.pem')
stdin, stdout, stderr = ssh.exec_command('cat new.txt')
o = str(stdout.readlines())
#s = o.find('u')
#e = o.find('n')
print(str(o[o.find('u')+2:o.find('n')-1]))

