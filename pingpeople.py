import sys
import time
from pushbullet import Pushbullet
import wiringpi2 as wpi
import serial
import os, platform

pbList = []
pbList.append(Pushbullet(""))
pbList.append(Pushbullet(""))

def ping(host):
    """
    Returns True if host responds to a ping request
    """
    # Ping parameters as function of OS
    ping_str = "-n 1" if platform.system().lower()=="windows" else "-c 1"
    # Ping
    return os.system("ping " + ping_str + " " + host) == 0

def notify(text):
    for pb in pbList:
        push = pb.push_note("Home Pi", text)



class Users(object):
    def __init__(self, name=None, ip=None, pin=0):
        self.name = name
        self.ip = ip
        self.pin = pin
        self.status = 'out'
userList = []
userList.append(Users("NAME-NAME","IP.IP.IP.IP"))

try:
    #Code running here
    while True:
        print "Checking "+time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
        for user in userList:
            result = ping(user.ip)
            oldStatus = user.status
            if (result):
                #User is home
                if (oldStatus == 'out'):
                    notify(user.name+" is now home!")
#                    push = pb.push_note("Home Pi", user.name+" is now home!")
                    user.status = 'in'
                print user.name +" is home."
            else:
                if (oldStatus == 'in'):
#                    push = pb.push_note("Home Pi", user.name+" is not home any longer!")
                    notify(user.name+" is not home any longer!")
                    user.status = 'out'
                print user.name +" is not home."
                #User is not home
        print "Next check in 100 seconds"
        time.sleep(100)

except (KeyboardInterrupt, SystemExit):
    print "Exiting..."
    #Exiting script


