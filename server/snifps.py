#!/usr/bin/python
#-*- coding: utf-8 -*-
import paramiko
import threading

def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            #stdin.write("Y")
            out = stdout.readlines()
            #stdout
            if len(out):
                for o in out:
                    print "[stdout]:%s\n[%s]: %s" %(m,ip,o)
            
            out = stderr.readlines()            
            #stderr
            if len(out):
                for o in out:
                    print "[stderr]:%s\n[%s]: %s" %(m,ip,o)
            
        print '%s OK'%(ip)
        ssh.close()
    except :
        print '%s\tError\n'%(ip)

		
if __name__=='__main__':    
    print "Begin+"
    for num in range(0,255):
        ip          = '192.168.1.%d' %(num)
        print 'ip:%s' %(ip)
        username    = 'lava'
        psw         = 'bingo123'
        cmd         = ['uname -r']
        ssh2(ip,username,psw,cmd)    
    print "Begin-"
