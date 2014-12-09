#!/bin/sh
. ./cgi_lib.cgi
error=false

IFS="&"
set -- $QUERY_STRING

for i in $@; do 
    IFS="="
    set -- $i
    if [ "$1" = "hostname" ] ; then
	new_hostname=`urldecode $2`
    fi
done

if [ "$new_hostname" = "" ]; then
	show_msg "Invalid hostname"
	exit 0
fi

echo "$new_hostname" > /config/hostname.conf

show_msg "Saving settings" /

