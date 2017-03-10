#!/usr/bin/python
import os,socket,getpass
socket_stass_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_stass_server.bind(("192.168.0.181",8888))
i=0
while 5 > 4 : 
	if i==0 :		
		size=socket_stass_server.recvfrom(100)
		print "data recieved is : "+size[0]
	if i==1 :	
		name=socket_stass_server.recvfrom(100)
		print "data recieved is : "+name[0]	
		
	if i==2 :
		break	
	i+=1
os.system("lvcreate -V"+size[0]+"M --name "+ name[0]+ " --thin pk/pool1" )
os.system("mkfs.xfs /dev/pk/"+name[0])
os.system("mkdir /media/"+name[0])
os.system("mount /dev/pk/"+name[0]+" /media/"+name[0])

