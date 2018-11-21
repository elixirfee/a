#!/usr/bin/python
#-*- coding: utf-8 -*-
import paramiko
import threading
import commands
#['192.168.56.101','user','pwd',['alunch --info']]
address_list = [\
['192.168.8.5', '08',['alunch --info'],'lava','bingo123'],\
['192.168.8.9', '08',['alunch --info'],'lava','bingo123'],\
['192.168.8.10','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.11','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.12','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.16','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.17','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.18','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.19','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.20','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.21','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.22','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.23','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.24','04',['alunch --info'],'lava','bingo123'],\
['192.168.8.25','04',['alunch --info'],'lava','bingo123'],\
['192.168.8.26','40',['alunch --info'],'lava','bingo123'],\
['192.168.8.27','12',['alunch --info'],'lava','bingo123'],\
['192.168.8.28','24',['alunch --info'],'lava','bingo123'],\
['192.168.8.29','48',['alunch --info'],'lava','bingo123'],\
['192.168.8.30','24',['alunch --info'],'lava','bingo123'],\
['192.168.8.31','24',['alunch --info'],'lava','bingo123'],\
['192.168.8.32','24',['alunch --info'],'lava','bingo123'],\
['192.168.8.33','24',['alunch --info'],'lava','bingo123'],\
['192.168.8.34','24',['alunch --info'],'lava','bingo123'],\
['192.168.8.35','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.36','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.37','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.56','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.57','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.58','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.59','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.62','08',['alunch --info'],'luxiangqian','luxiangqian'],\
['192.168.8.63','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.64','08',['alunch --info'],'seapig','12345678'],\
['192.168.8.66','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.69','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.71','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.72','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.73','08',['alunch --info'],'guangming','123456'],\
['192.168.8.75','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.79','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.81','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.82','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.83','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.84','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.85','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.86','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.87','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.88','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.89','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.90','08',['alunch --info'],'weijun','junwei123'],\
['192.168.8.91','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.92','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.93','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.94','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.97','08',['alunch --info'],'lava','bingo123'],\
['192.168.8.98','08',['alunch --info'],'lava','bingo123'], \
['192.168.8.100','04',['alunch --info'],'lava','bingo123'], \
['192.168.10.23','8',['alunch --info'],'lava','bingo123'],\
['192.168.10.24','40',['alunch --info'],'lava','bingo123'] \
]

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
    #threads = []      
    print "Begin+"
    for server in address_list:
        ip          = server[0]
        username    = server[3]
        psw         = server[4]
        cmd         = server[2]
        ssh2(ip,username,psw,cmd)    
    print "Begin-"
    
