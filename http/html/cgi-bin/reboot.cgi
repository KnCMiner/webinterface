#!/bin/sh
. ./cgi_lib.cgi

show_msg "Rebooting System <br>(wait for approx. 60 seconds)" / 60000

sync
sleep 1
reboot

