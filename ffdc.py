#!/usr/bin/python
from paramiko import SSHClient
#from scp import SCPClient

class ffdcConnection(object):
    def __init__(self, ip, uname, passwd):
        self.uname  = uname
        self.passwd = passwd
        self.ip     = ip

    def ffdc_cmd(self, cmd):
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(self.ip, username=self.uname, password=self.passwd)
        print "\nExecuting:", cmd
        stdin, stdout, stderr = ssh.exec_command(cmd)
        lines = stdout.readlines()
        for line in lines:
            print line
        ssh.close()

    def my_ffdc(self):
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(self.ip, username=self.uname, password=self.passwd)
        print "\nExecuting:/usr/bin/ffdc"
        stdin, stdout, stderr = ssh.exec_command("/usr/bin/ffdc")
        lines = stdout.readlines()
        for line in lines:
            print line
            if '/tmp/ffdc_' in line:
                ffdc_name = line.replace('Contents in /tmp/','')
                print "FFDC Tar file:",ffdc_name
        ssh.close()
        cmd = 'ls -larth ' + ffdc_name
        self.ffdc_cmd(cmd)
        #self.scp_file(ffdc_name)

    def scp_file(self, ffdc_name):
        ffdc_name_path = '/home/root' + ffdc_name
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(self.ip, username=self.uname, password=self.passwd)
        scp = SCPClient(ssh.get_transport())
        scp.get(ffdc_name_path)

