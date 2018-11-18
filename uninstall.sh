#!/bin/bash

# binary file
rmmod snd_pci

pid1=`pidof svnc`
pid2=`pidof alunch`

if [ -n "$pid1" ]; then  
    #echo $pid1
	kill $pid1
fi 

if [ -n "$pid2" ]; then  
    #echo $pid2
	kill $pid2
fi 

rm -fr /sbin/zman
rm -fr /bin/alunch
rm -fr /sbin/svnc

cp -f unrc.local				/etc/rc.local

