#!/bin/sh
KNC_RELEASE=$(cat /etc/knc-release)
quote_escaped_hostname=$(cat /config/hostname.conf 2>/dev/null | sed 's:&:\&amp;:g;s:'"'"':\&#39;:g;s:":\&quot;:g;s:<:\&lt;:g;s:>:\&gt;:g')
escaped_hostname=$(printf '%s\n' "${quote_escaped_hostname}" | sed 's:[\/&"]:\\&:g;$!s/$/\\/')
sed -e "
s!#%#REMOTE_USER#%#!${REMOTE_USER}!g
s!#%#KNC_RELEASE#%#!${KNC_RELEASE}!g
s!#%#HOSTNAME#%#!${escaped_hostname}!g
" < /www/tmpl/system_management.html_tmpl
