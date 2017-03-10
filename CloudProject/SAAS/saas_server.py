#!/usr/bin/python
import os,socket,getpass
socket_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_server.bind(("192.168.0.93",9999))
i=0
while 5 > 4 : 
	if i==0 :		
		name=socket_server.recvfrom(100)
		print "data recieved is : "+name[0]
	if i==1 :	
		passw=socket_server.recvfrom(100)
		print "data recieved is : "+passw[0]	
		
	if i==2 :
		break	
	i+=1
os.system("useradd "+name[0])
os.system("echo "+passw[0]+" | passwd "+name[0] +" --stdin")

'''j=0
while j < 2 :
	socket_server.sendto("OKAY",("192.168.0.123",9999))
	j+=1'''
