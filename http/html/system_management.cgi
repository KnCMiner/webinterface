#!/bin/sh
KNC_RELEASE=$(cat /etc/knc-release)
sed -e "
s!#%#REMOTE_USER#%#!${REMOTE_USER}!g
s!#%#KNC_RELEASE#%#!${KNC_RELEASE}!g
" < /www/tmpl/system_management.html_tmpl
