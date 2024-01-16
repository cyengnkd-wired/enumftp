#!/usr/bin/python3

import socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(("IP",21))
banner = tcp.recv(1024)
print(banner)

tcp.send("USER ftp\r\n")
user = tcp.recv(1024)
print(user)

tcp.send("PASS ftp\r\n")
password = tcp.recv(1024)
print(password)

tcp.send("HELP\r\n")
tcp.send("PWD\r\n")
cmd = tcp.recv(2048)
print(cmd)
