import sys
import socket

def prPink(skk): print("\033[95m{}\033[00m" .format(skk))
def prRed(skk): print("\033[91m{}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk))

prPink("""
   ______  ____________  
  / __/  |/  /_  __/ _ \ 
 _\ \/ /|_/ / / / / ___/ 
/___/_/_ /_/_/_/_/_/  ___
  / __/ |/ / / / /  |/  /
 / _//    / /_/ / /|_/ / 
/___/_/|_/\____/_/  /_/               
""")

if len(sys.argv) != 3:
    prRed("[-] How to use -> python 10.0.0.10 25")
else:
    ip = sys.argv[1]
    port = sys.argv[2]

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((ip,int(port)))
    banner = mysocket.recv(1024)

    prPurple("[i] Server Banner")
    print(banner)

    prGreen("[+] Enum Users")
    mysocket.send("VRFY root\r\n")
    user = mysocket.recv(1024)
    print(user)
