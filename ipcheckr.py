
#this is a ip checker by defonottea

#imports
import csv
import sys
import random
import re 
import json
from telnetlib import IP
from tkinter import YES
from urllib.request import urlopen
import os


def main():
    start() 
                                                                                    
def start(): 
    print(""" $$$$$$\ $$$$$$$\         $$$$$$\  $$\   $$\ $$$$$$$$\  $$$$$$\  $$\   $$\ $$$$$$$\  
\_$$  _|$$  __$$\       $$  __$$\ $$ |  $$ |$$  _____|$$  __$$\ $$ | $$  |$$  __$$\ 
  $$ |  $$ |  $$ |      $$ /  \__|$$ |  $$ |$$ |      $$ /  \__|$$ |$$  / $$ |  $$ |
  $$ |  $$$$$$$  |      $$ |      $$$$$$$$ |$$$$$\    $$ |      $$$$$  /  $$$$$$$  |
  $$ |  $$  ____/       $$ |      $$  __$$ |$$  __|   $$ |      $$  $$<   $$  __$$< 
  $$ |  $$ |            $$ |  $$\ $$ |  $$ |$$ |      $$ |  $$\ $$ |\$$\  $$ |  $$ |
$$$$$$\ $$ |            \$$$$$$  |$$ |  $$ |$$$$$$$$\ \$$$$$$  |$$ | \$$\ $$ |  $$ |
\______|\__|             \______/ \__|  \__|\________| \______/ \__|  \__|\__|  \__|  
                                                               created by defonottea  
                                                                                    """)
    checkr() 

def checkr(): 
    global ip 
    ip = input("enter your target ip address in form 0.0.0.0:        ")
    print(" ")

    response = urlopen('http://ipwho.is/'+ip)
    ipwhois = json.load(response)
    successful = str(ipwhois['success'])
    #output
    print("Pinged ip:     "+ ipwhois['ip'])
    print('Output:        '+ str(ipwhois['success']))
    
    if successful=="False":
        print('Reason:        '+ ipwhois['message'])
        print(" ")
        checkr()
    elif successful=="True":
        menu()
        
    else:
        print("unknown error")

def menu():
    #this is the menu print
    print()

    choice = input("""
                                          
    Menu:
    
    1: IP Ping (do this to check if ip went down)
    2: IP Geolocator
    3: IP Connection
    
    
    more to come..
    
    enter number:        """)

    
#this is the option detector
    if choice=="1":
        ping()
    elif choice=="2":
        locator()
    elif choice=="3":
        connection()
    else:
        print("this is not an option")
        print("test work")
        menu()

def ping():
    print(" ")
    #ask for ip to ping
    response = urlopen('http://ipwho.is/'+ip)
    ipwhois = json.load(response)
    successful = str(ipwhois['success'])
    #output
    print("Pinged ip:     "+ ipwhois['ip'])
    print('Output:        '+ str(ipwhois['success']))
    
    if successful=="False":
        print('Reason:        '+ ipwhois['message'])
        print(" ")
    #return?
    ret()

def locator():
    print("running ip geolocator...")
    response = urlopen('http://ipwho.is/'+ip)
    ipwhois = json.load(response)
    #output
    print(" ")
    print ("Continent:   "+ ipwhois['continent'], ipwhois['continent_code'])
    print ("Country:     "+ ipwhois['country'])
    print ("Region:      "+ ipwhois['region'], ipwhois['region_code'])
    print ("City:        "+ ipwhois['city'])
    print ("ZIP:         "+ ipwhois['postal'])

    print(" ")
    #return to menu?
    ret()


def connection():
    print("")
    response = urlopen('http://ipwho.is/'+ip)
    ipwhois = json.load(response)
    #output
    print(" ")
    print('Asn:     '+ str(ipwhois['connection']['asn']))
    print('Org:     '+ str(ipwhois['connection']['org']))
    print('Isp:     '+ str(ipwhois['connection']['isp']))
    print('Domain:  '+ str(ipwhois['connection']['domain']))
    print(" ")
    ret()
    



#ret 
def ret(): 
    print("")
    print("")
    print("")
    retinput = input("""
                        1: return to menu
                        2: exit""")
    if retinput=='1':
        menu()
    elif retinput=='2':
        exit()
    else:
        print("not a valid input")
        ret()

        
main()
