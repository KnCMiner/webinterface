#!/bin/sh
if cmp -s /etc/shadow.default /etc/shadow; then
	exec /www/pages/setup.cgi
else
	quote_escaped_hostname=$(cat /config/hostname.conf 2>/dev/null | sed 's:&:\&amp;:g;s:'"'"':\&#39;:g;s:":\&quot;:g;s:<:\&lt;:g;s:>:\&gt;:g')
	escaped_hostname=$(printf '%s\n' "${quote_escaped_hostname}" | sed 's:[\/&"]:\\&:g;$!s/$/\\/')
	sed -e "
		s!#%#HOSTNAME#%#!${escaped_hostname}!g
	" < /www/tmpl/index.html_tmpl
fi
