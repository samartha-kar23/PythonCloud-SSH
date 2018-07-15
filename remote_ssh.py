
import paramiko
import pymysql
moisture=22
waterl=400
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.24.4.15', username='ubuntu', key_filename='/home/devstack/Desktop/Sensor_login/test2.pem')
#stdin, stdout, stderr = ssh.exec_command('chmod 777 script2.sh')
#print stdout.readlines()
#print stderr.readlines()
stdin, stdout, stderr = ssh.exec_command('echo -e "moisture="%d"\nexport moisture">script2.sh' % moisture)
print stdout.readlines()
print stderr.readlines()
ssh2 = paramiko.SSHClient()
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect('172.24.4.15', username='ubuntu', key_filename='/home/devstack/Desktop/Sensor_login/test2.pem')
#stdin, stdout, stderr = ssh.exec_command('chmod 777 script2.sh')
#print stdout.readlines()
#print stderr.readlines()
stdin, stdout, stderr = ssh2.exec_command('echo -e "waterl="%d"\nexport waterl">script3.sh'%waterl)
print stdout.readlines()
print stderr.readlines()

ssh3 = paramiko.SSHClient()
ssh3.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh3.connect('172.24.4.15', username='ubuntu', key_filename='/home/devstack/Desktop/Sensor_login/test2.pem')
#stdin, stdout, stderr = ssh.exec_command('chmod 777 script2.sh')
#print stdout.readlines()
#print stderr.readlines()


#stdin, stdout, stderr = ssh3.exec_command('echo -e ". ./script2.sh\n. ./script3.sh\nhumidity=30\necho \$((moisture+waterl))">script.sh')
stdin, stdout, stderr = ssh3.exec_command('echo -e ". ./script2.sh\n. ./script3.sh\npump=0\nif [ \$moisture -lt 60 ]\nthen\nif [ \$waterl -lt 580 ]\nthen\npump=1\nfi\nelse\npump=0\nfi\necho \$pump">script.sh')

print stdout.readlines()
print stderr.readlines()

ssh4 = paramiko.SSHClient()
ssh4.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh4.connect('172.24.4.15', username='ubuntu', key_filename='/home/devstack/Desktop/Sensor_login/test2.pem')
stdin, stdout, stderr = ssh4.exec_command('bash script.sh')
result=stdout.readlines()
result=result[0].strip('\n\r')
print str(result)
print stderr.readlines()


conn = pymysql.connect(host='10.14.88.224', user='root', password='sensor_cloud', db='SENSORS')

a= conn.cursor()

sql = "UPDATE SENSOR SET Data=%s WHERE type=%s"

countrow = a.execute(sql,(str(result),'Pump'))
conn.commit()
conn.close()

#o = str(stdout.readlines())
#s = o.find('u')
#e = o.find('n')
#print(str(o[o.find('u')+2:o.find('n')-1]))
#"""

#import paramiko
#from time import sleep
#client = paramiko.SSHClient()
#client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#client.connect(hostname='172.24.4.15', username='ubuntu', key_filename='/home/devstack/Desktop/Sensor_login/test2.pem')

#channel = client.get_transport().open_session()
#command = 30
#command2 = 20
#channel.exec_command('/usr/bin/bash -c "%s"' % command)
#channel.exec_command('bash script.sh')

#channel.shutdown_write()

#stdout = channel.makefile().read()
#stderr = channel.makefile_stderr().read()
#exit_code = channel.recv_exit_status()

#channel.close()
#client.close()

#print 'stdout:', stdout
#print 'stderr:', stderr
#print 'exit_code:', exit_code
