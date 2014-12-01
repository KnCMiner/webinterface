#!/bin/sh
. ./cgi_lib.cgi

cat <<EOT
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">
<html>
<head>
<title>Miner</title>
<meta charset="UTF-8" />
<link href="/style.css" rel="stylesheet" type="text/css">
<link href="/grid.css" rel="stylesheet" type="text/css">
<link href="/type/type.css" rel="stylesheet" type="text/css">
</head>
<body>
<div id="wrapper">
<header>
<div id="logo" class="col span_6_of_12">
<img src="/images/logo.png" alt="KnCMiner logo">
</div>
</header>
<div id="header" class="section">
<div class="span_12_of_12">
<div class="xbox box">
<div class="span_12_of_12">
<h1>Miner is shutting down</h1>
<p>Miner is shutting down. When all green LEDs are off, it is safe to turn off the PSUs. It should not take more then 30 s.</p>
</div>
</div>
</div>
</div>
</div>
</body>
</html>
EOT

sync
sleep 1
poweroff
