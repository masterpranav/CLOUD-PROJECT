#!/usr/bin/python
import os,socket,getpass
name=raw_input("Enter username : ")
passw=raw_input("Enter password : ") 
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.sendto(name,("192.168.0.93",9999))
client_socket.sendto(passw,("192.168.0.93",9999))
'''while 5 > 4 : 
ans=client_socket.recvfrom(100)
if ans[0]=="OKAY" : '''
print   "press  1   For   firefox  :   "
print   "press  2   For   gedit  :   "
print   "press  3   For   vlc  :   "
print   "press  4   For   docker  :   "
ch=int(raw_input("Enter your choice : "))
if ch==1 :
	'''os.system("ssh -X -l "+name+" 192.168.0.93 firefox")'''
	os.system("sshpass -p "+passw+" ssh -X "+name+"@192.168.0.93 firefox" )
	print 1
if ch==2 :
	'''os.system("ssh -X -l "+name+" 192.168.0.93 gedit")'''
	os.system("sshpass -p "+passw+" ssh -X  "+name+"@192.168.0.93 firefox" )
	print 2
if ch==3 :
	'''os.system("ssh -X -l "+name+" 192.168.0.93 vlc")''' 
	os.system("sshpass -p "+passw+" ssh -X "+name+"@192.168.0.93 firefox" )
	print 3
print "Done"
