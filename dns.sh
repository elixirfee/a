#!/bin/bash

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

