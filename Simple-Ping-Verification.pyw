# Ping_Verification.py
# Created a Simple Ping verification script in Python
# Author: Anthony Constant (AC)

################################# SOME NOTES #########################################

## Simple Ping automation script (specify the host using ip_list)

######################## HOW DOES IT WORK ##############################################

## Ping a list of devices to return whether the network status is successful or unsuccessful. 
## Specify the target IP address in the ip_list

############################# REFERENCES ###############################################

## https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-software-releases-121-mainline/12778-ping-traceroute.html

########################################################################################
############################ START PROJECT HERE #######################################
############################################################################################
import os 

ip_list = ["8.8.8.8", "192.168.1.1", "192.168.4.1"] ## plug in the list of IP addresses in which you want to check their status 

for ip in ip_list: ## create a for loop to go through the list of IP addresses
    response = os.popen(f"ping {ip}").read() ## create a response variable and store the ping response in read format. 
    if "Received = 4" in response: ## if this exact string is within the response, its up, otherwise down. 
        print(f"{ip} Ping was Successful! ")
    else:
        print(f"{ip} Ping was Unsuccessful! ")
