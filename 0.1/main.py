'''
Author: Dean Emmet/rootfinlay
Version: 0.1
Description: concordia crypto
'''
import os
import random
import sys
import string
import hashlib
import socket
import uuid
import requests

def Main():
    #Chooses option for concordia
    print(
    "=================\n"
    "=   CONCORDIA   =\n"
    "=================\n"
    "1) Mine\n"
    "2) View Balence\n"
    "s) Setup\n"
    "e) Exit\n"
    )

    choice = input("\n> ")

    if choice == '1':
        Mine()
    elif choice == '2':
        bal_view()
    elif choice == 's':
        setupVerif()
    elif choice == "e":
        os.system('exit')
    else:
        print("Choice incompatible")
        Main()

def Mining():
    alphabet = string.ascii_letters

    newAddr = ''.join(random.choice(alphabet) for x in range(number))

def bal_view():
    os.syetem('clear')
    balance = open('balance.txt', 'r+').read()
    print("Your balence is: " + balance)

def setupVerif():
    #Init check, checks to see if string is in file before commiting to setup, meaning previous data isn't lost. If string isn't in the text file,
    if "aFbHzDlK" in open('setup.txt').read():
        s_token = "1"
    else:
        s_token = "2"

    if s_token == "1":
        print("Everything already set up, use different option")
        Main()
    elif s_token == "2":
        FinalSetup()
    else:
        print("Error")
        os.system('exit')

def FinalSetup():
    os.system('clear')
    print("Now setting your wallet and node registration up")
    #Final setup, wallet gen, node registration
    #wallet
    alphabet = string.ascii_letters
    newAddr = ''.join(random.choice(alphabet) for x in range(256))

    if 'newAddr' in open('checkAddr.txt').read():
        #DEBUGGING
        print("1")


        FinalSetup()
    else:
        #DEBUGGING
        print("2 - FOR DEBUGGING PURPOSES")

        #Writes address to checkAddr.txt and you.txt
        open('checkAddr.txt', 'a+').write(newAddr + "\n")
        print("Your new crypto address is: ", newAddr)
        password = input("\nPlease enter a password:\n> ")
        passwordToBeHashed = bytes(password, 'utf-8')

        #Hash function for password, will be needed to check balence, make transaction or start mining.
        m = hashlib.sha256()
        m.update(passwordToBeHashed)
        finalPassword = m.hexdigest()
        print(finalPassword)

        open('password.txt', 'w+').write(finalPassword)

        '''
        Node registration
        Gets Computer name, IP address, MAC address and then gives unique id to add to node list.
        '''
        #Retreives necessary information for node registration
        hostname = socket.gethostname()
        ipAddr = requests.get('https://checkip.amazonaws.com').text.strip()
        oneMacAddr = uuid.getnode()
        finMacAddr = ':'.join(("%012X" % oneMacAddr) [i:i+2] for i in range(0,12,2))

        #FOR TESTING:
        print(hostname)
        print(ipAddr)
        print(finMacAddr)

        open('you.txt', 'w').write("Your hostname: " + hostname + "\nYour IP address during setup: " + ipAddr + "\nYour MAC address: " + finMacAddr + "\n" + "Your address: " + newAddr + "\n")

        #ONLY TURN ON IN PRODUCTION
        open('setup.txt', 'w+').write("aFbHzDlK")


if __name__ == '__main__':
    Main()
