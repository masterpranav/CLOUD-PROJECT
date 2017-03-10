#!/usr/bin/python

import  os
u=raw_input("enter user name :  ")
p=raw_input("enter password :   ")

if   u ==  "vimal" and  p == "redhat" :

	print   "press  1  to  Access  SaaS Cloud :  "
	print   "Press  2  to access  STaaS  : "
	ch=raw_input()
	if  ch  ==  '1' :
		os.system('python /root/Desktop/CloudProject/SAAS/list.py')	
	elif  ch  ==  '2' :
		os.system('python /root/Desktop/cloudpr/STAAS/start.py')
		

else :
	print  "invalid  username and password : "




	




