"""
Fake Proxy Server [ Python ]
 
Writt3n By : Ashish kunwar
Email : dorkerdevil280@gmail.com
with this script you can set a proxy server which anyone goes through it and logged and managed !
To Make this script work, you need to first change proxy settings in your browser as script conf.
"""

import socket

local_ip="127.0.0.1"; #! local ip to bind server on.
local_port=int(8080); #! port to install server on.

def server(server,lhost,lport):
	server=server.socket(server.AF_INET,server.SOCK_STREAM);
	server.bind((lhost,lport));
	server.listen(80); #! listen max for 80 req.
	print "\n\t[$] SERVER RUNNING ( %s : %s )\n\n"%(lhost,lport);
	while True:
		c,address=server.accept();
		reqdata = c.recv(8080);
		website=reqdata.split("Host:")[1];
		website=website.split("User-Agent")[0]
		print "[!] Server Request Website  ( %s )"%(website.strip());


while True:
	try:
		server(socket,local_ip,local_port);
	except KeyboardInterrupt:
		print "\n[!] Ctrl + C Pressed By You.";
