#!/bin/sh
if cmp -s /etc/shadow.default /etc/shadow; then
	exec /www/pages/setup.cgi
else
	cat /www/pages/index.html
fi
