#!/bin/python3

import sys #allow us to enter command line argument, among other thing
import socket
from datetime import datetime

#Define Our Targer
if len(sys.argv) == 2:
	targer = socket.gethostbyname(sys.argv[1]) # translate a hostname to IPV4
else:
	print("Invalid amount of arguments")
	print("syntax: python3 scanner.py <ip>")
	sys.exit()

#Add a pretty banner
print("-" * 50)
print("scanning targer "+ targer)
print("Time Started :"+ str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) # is a float
		result = s.connect_ex((targer,port)) # return error indicator
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\n Exiting program")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved .")
	sys.exit()
	
except socket.error:
	print("Couldn't connect to server .")
	sys.exit()