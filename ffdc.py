#!/usr/bin/python
import pickle
import os
from paramiko import SSHClient

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
        print "\nExecuting:", cmd
        stdin, stdout, stderr = ssh.exec_command(cmd)
