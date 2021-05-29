'''
Concordia Testnet Infrastructure
Author: Dean Emmet/rootfinlay
Description: Concordia Blockchain testnet
'''
import socket
import uuid
import os

def Main():
    if "nodeRegistered" not in open("nodes.txt", 'r+').read():
        nodeRegistration()
    else:
        print("Node already registered")


def nodeRegistration():
    #All necessary information for node verification
    hostname = socket.gethostname()
    ipAddr = requests.get('https://checkip.amazonaws.com').text.strip()
    oneMacAddr = uuid.getnode()
    finMacAddr = ':'.join(("%012X" % oneMacAddr) [i:i+2] for i in range(0,12,2))

    #Writes to file to verify node registration
    open('you.txt', 'w+').write("Your hostname: " + hostname + "\nYour IP address during setup: " + ipAddr + "\nYour MAC address: " + finMacAddr + "\n" )
    open('nodes.txt', 'w+').write("nodeRegistered")

if __name__ == "__main__":
    Main()
