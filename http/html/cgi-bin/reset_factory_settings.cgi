#!/bin/sh
. ./cgi_lib.cgi

if [ -f /config/cookie ] && [ "$QUERY_STRING" = "cookie=$(cat /config/cookie)" ]; then
	show_msg "Reset to factory defaults. System will reboot." / 12000
	rm -f /config/*
	sh -c "sleep 1 && reboot" >/dev/null 2>/dev/null </dev/null &
	exit
fi

COOKIE=$RANDOM

echo -n $COOKIE > /config/cookie

sed -e "
s!#%#COOKIE#%#!${COOKIE}!g
" < /www/tmpl/reset_factory_defaults.html_tmpl

