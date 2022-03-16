"""
/* Authorized: Ahmed Yousri, email: ahmed.yousri@aiactive.com */
"""

import csv
import os
import platform
from datetime import datetime

def logg(data,ty):
    global datetime
    now = datetime.now() # current date and time
    with open("logger.log","a") as log :
        time = now.strftime("%m/%d/%Y, %H:%M:%S")
        log.write(ty+" :  "+data+"           "+time)
        log.write("\n")
        log.close()
        #


plat = platform.system()

#server = "localhost"     #example for single host
#servers = {"192.168.1.21"}     # example of Host/IPaddress using Dictionary

# Import the list of hosts/servers/ipaddress from CSV file
with open('ipaddress-list.csv', 'r') as servers_list:
    servers = csv.DictReader(servers_list)
    for vm in servers_list:
        print "---- Trying to Ping a Server with IPAddress ----", vm
        # Check for Windows and Linux Platforms
        if plat == "Windows":
            response = os.system("ping -n 1 " + vm.strip())
            pass

        elif plat == "Linux":
            response = os.system("ping -c 1 -W 3 " + vm.strip())
            pass

        # Check for response status code
        if response == 0:
                print "********************************************************************"
                print(vm.strip(), 'is UP and reachable!')
                print "********************************************************************"
                print "\n"
                logg(vm.strip()+" Is live","info")
        elif response == 2 or 256 or 512:
                print "********************************************************************"
                print(vm.strip(), 'is DOWN and No response from Server!')
                print "********************************************************************"
                print "\n"
                logg(vm.strip()+" Is Down","Error")
        else:
                logg(vm.strip()+" Is Down","Error")
                print "*********************************************************************"
                print(vm.strip(), 'is DOWN and Host Unreachable!')
                print "*********************************************************************"
                print "\n"
