#!/usr/bin/python

import  os,socket
print   "Press  1  for  NFS  based  Storage : "
print   "Press  2  for  SSHFS  based  Storage : "
print   "Press  3  for  SMB  based  Storage : "
print   "Press  4  for  GFS  based  Storage : "


ch=raw_input()


if ch  ==  '1'  :
	size=raw_input("enter  your drive  size in MB :  ")
	name=raw_input("enter  your  drive  name :  ")
	client_stass_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	client_stass_socket.sendto(size,("192.168.0.181",8888))
	client_stass_socket.sendto(name,("192.168.0.181",8888))
	'''while 5>2:	
		a=client_socket.recvfrom(2)
		if a == "OK" :'''
	raw_input("Press 1 to mount")
	os.system("setenforce 0")
	os.system("setenforce 0")
	os.system("iptables -F")
	os.system("systemctl disable Firewalld")
	'''os.system("yum install nfs-utils")'''
	os.system("systemctl restart nfs-server")
	'''dir_name=raw_input("Enter the name of your file or directory: ")'''
	os.system("mkdir /media/"+name)
	os.system("mount 192.168.0.181:/media/"+name+" /media/"+name)
	os.system("echo 192.168.0.181:/media/"+name+" /media/"+name+" nfs _netdev,defaults 0 0 >> /etc/fstab")
if ch  ==  '2'  :
	size=raw_input("enter  your drive  size in MB :  ")
	name=raw_input("enter  your  drive  name :  ")
	client_stass_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	client_stass_socket.sendto(size,("192.168.0.181",8888))
	client_stass_socket.sendto(name,("192.168.0.181",8888))
	'''client_socket.bind(("",9999))
	while 5>2:	
		a=client_socket.recvfrom(2)
		if a == "OK" :'''
	raw_input("Press 1 to mount")
	os.system("setenforce 0")
	os.system("iptables -F")
	os.system("systemctl disable Firewalld")
	os.system("yum install openssh-clients")
	os.system("systemctl restart sshd")
	dir_name=raw_input("Enter the name of your file or directory: ")
	'''os.system("mkdir /media/"+dir_name)'''
	os.system("sshfs root@192.168.0.181:/media/cl /media/"+name)
	os.systemctl("echo root@192.168.0.181:/media/cl /media/"+name+" nfs _netdev,defaults 0 0 >> /etc/fstab")
if ch  ==  '3'  :
	size=raw_input("enter  your drive  size in MB :  ")
	name=raw_input("enter  your  drive  name :  ")
	client_stass_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	client_stass_socket.sendto(size,("192.168.0.181",8888))
	client_stass_socket.sendto(name,("192.168.0.181",8888))
	'''client_socket.bind(("",9999))
	while 5>2:	
		a=client_socket.recvfrom(2)
		if a == "OK" :'''
	raw_input("Press 1 to mount")
	os.system("setenforce 0")
	os.system("iptables -F")
	os.system("systemctl disable Firewalld")
	os.system("yum install cifs-utils samba-client")
	dir_name=raw_input("Enter the name of your file or directory: ")
	'''os.system("mkdir /media/"+dir_name)'''
	os.system("mount -o username=  //192.168.0.181/media/cl /media/"+name)
	os.systemctl("echo //192.168.0.181/media/cl /media/"+name+" nfs _netdev,username="+usr_name+" password="+usr_name+"  0 0 >> /etc/fstab")
				
if ch  ==  '4'  :
	size=raw_input("enter  your drive  size in MB :  ")
	name=raw_input("enter  your  drive  name :  ")
	client_stass_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	client_stass_socket.sendto(size,("192.168.0.181",8888))
	client_stass_socket.sendto(name,("192.168.0.181",8888))
	'''client_socket.bind(("",9999))
	while 5>2:	
		a=client_socket.recvfrom(2)
		if a == "OK" :'''
	raw_input("Press 1 to mount")
	os.system("setenforce 0")
	os.system("iptables -F")
	os.system("systemctl disable Firewalld")
	dir_name=raw_input("Enter the name of your file or directory: ")
	os.system("mkdir /media/"+dir_name)
	os.system("mount 192.168.0.181:/media/cl /media/"+name)
	os.systemctl("echo 192.168.0.181:/media/cl /media/"+name+" nfs _netdev,defaults 0 0 >> /etc/fstab")
			
