#!/usr/bin/python3

import socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# conectando ao servidor

tcp.connect(("IP",21))

banner = tcp.recv(1024)
print(banner)

# enviando usuario
tcp.send("USER ftp\r\n")
user = tcp.recv(1024)
print(user)

# enviando a senha
tcp.send("PASS ftp\r\n")
password = tcp.recv(1024)
print(password)

# enviando comando HELP
tcp.send("HELP\r\n")

# enviando comando PWD
tcp.send("PWD\r\n")
cmd = tcp.recv(2048)
print(cmd)
