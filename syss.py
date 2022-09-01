#!/usr/bin/env python3

# while this should theoretically work on all platforms, it has only been tested on linux

import sys
import socket

# helper function that reads a socket line by line
def s_readline(s):
	# zero the buffer
	buf=""
	while True:
		# read a byte from the socket into the buffer array
		c = s.recv(1)
		c=c.decode()
		if c == "\n":
			break
		buf+=c
	return buf

# usage
if len(sys.argv) != 3:
	print("USAGE: python3 "+sys.argv[0]+" <host> <port>")
	exit()

# create socket
s = socket.socket()
print("connecting to "+sys.argv[1]+":"+sys.argv[2])
# connect to server
s.connect((sys.argv[1], int(sys.argv[2])))
prompt=""
rbuf=""

# read prompt
prompt=s_readline(s)
# read mail
mail = input(prompt)
# add \n to mail and send to server
s.sendall((mail+"\n").encode())

# do the thing
while True:
	line = s_readline(s)
	if line.strip() == "Hello world":
		print("Got "+line.strip())
		s.sendall("hell world\n".encode())
		print("Sent hell world")
	elif line.startswith("FLAG"):
		print("Got flag")
		print(line)
		break
	else:
		print("ERROR")
		break
