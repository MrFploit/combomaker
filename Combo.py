# Code By it4min
# t.me/it4min
# t.me/LinuxArmy
# -- Combo List Maker v1 --
import time, os

os.system("clear")
banner = '''
\033[92m .o88b.  .d88b.  .88b  d88. d8888b.  .d88b.  
d8P  Y8 .8P  Y8. 88'YbdP`88 88  `8D .8P  Y8. 
8P      88    88 88  88  88 88oooY' 88    88 
8b      88    88 88  88  88 88~~~b. 88    88 
Y8b  d8 `8b  d8' 88  88  88 88   8D `8b  d8' 
 `Y88P'  `Y88P'  YP  YP  YP Y8888P'  `Y88P'  
                                             
                                             
.88b  d88.  .d8b.  db   dD d88888b d8888b.   
88'YbdP`88 d8' `8b 88 ,8P' 88'     88  `8D   
88  88  88 88ooo88 88,8P   88ooooo 88oobY'   
88  88  88 88~~~88 88`8b   88~~~~~ 88`8b     
88  88  88 88   88 88 `88. 88.     88 `88.   
YP  YP  YP YP   YP YP   YD Y88888P 88   YD   
                                             
                                             
'''
print(banner)
userf = input("\033[91m>>> \033[93mEnter the username address: ")
passf = input("\033[91m>>> \033[93mEnter the password address: ")
usrf = open(userf, "r").read().splitlines()
pasf = open(passf, "r").read().splitlines()

userlist = []
passlist = []

os.system("clear")
print ('\n'+"\033[94m      - Loading Data ...")
time.sleep(3)

for u in usrf:
    userlist.append(u.replace('\n',""))

for p in pasf:
    passlist.append(p.replace('\n',""))

os.system("clear")
print ('\n'+"      - Combo List Makeing ...")
time.sleep(3)

combof = open("ComboList.txt","a")

if len(userlist) > len(passlist):
    for num in range(len(passlist)):
        username = userlist[num]
        password = passlist[num]
        combo = username+":"+password
        combof.write(combo+'\n')
        print (combo)

elif len(userlist) < len(passlist):
    for num in range(len(userlist)):
        username = userlist[num]
        password = passlist[num]
        combo = username+":"+password
        combof.write(combo+'\n')
        print (combo)

if len(userlist) == len(passlist):
    for num in range(len(passlist)):
        username = userlist[num]
        password = passlist[num]
        combo = username+":"+password
        combof.write(combo+'\n')
        print (combo)
combof.close()

os.system("clear")
print ('\n'+"      - Combo List Maked ;")
