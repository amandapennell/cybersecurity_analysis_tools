# PART 3: NETWORK SCANNING
# For this part, you will need to create a network scanner in Python. 
# Your scanner will attempt to discover all hosts within the network specified.
# Your scanner should operate in two different modes:
#   The first uses ICMP echo request packets
#   The second sends TCP SYN packets to a user supplied port

# Your program should meet the following specifications:

#   INPUT
#       Network address to scan (e.g. 192.168.2.0/24)
#       Mode (ICMP or TCP)
#       Port number to scan (if TCP scan is selected)

#   PROCESSING
#       Your program should send a packet to every possible IP address on the network.
#       The program should either send TCP or IMCP packets, depending on the mode selected.
#       You should record successful responses.

#   OUTPUT
#       Unique IP addresses that responded to the sent packets.
#       Each IP address should be printed on a separate line, e.g
#           192.168.2.1
#           192.168.2.10

# scapy installed using pip install scapy
# ip addr run in terminal to find IP address

# Import necessary modules
from scapy.all import *

# Define functions for ICMP and TCP scans
def icmp_scan(network):
  pkts = IP(dst=network) / ICMP() # create packet
  ans, unans = sr(pkts, timeout=10, retry=2) # send packet
  ans.summary(lambda s,r:r.sprintf("%IP.src%")) # print results

def tcp_scan(network, port): 
  pkts = IP(dst=network) / TCP(sport=RandShort(), dport=int(port), flags="S") # create packet
  ans, unans = sr(pkts, timeout=10, retry=2) # send packet
  ans.summary(lambda sICM,r:r.sprintf("%IP.src%")) # print results

# Print ASCII banner
print(""" __  _ ___ _____ _   _  __  ___ _  __    __   ___ __  __  _ __  _ ___ ___
|  \| | __|_   _| | | |/__\| _ \ |/ /  /' _/ / _//  \|  \| |  \| | __| _ \
| | ' | _|  | | | 'V' | \/ | v /   <   `._`.| \_| /\ | | ' | | ' | _|| v /
|_|\__|___| |_| !_/ \_!\__/|_|_\_|\_\  |___/ \__/_||_|_|\__|_|\__|___|_|_\  """)

print("=========================================")

# Prompt user for input and run corresponding function
type_scan = input("Specify TCP or ICMP: ") # Ask user for TCP or ICMP scan
network = input("Define target network: ") # Ask user for target network

if type_scan == "TCP": # If TCP scan is selected
  port = input("Specify a target port: ") # Ask user for target port
  tcp_scan(network, port) # Run TCP scan
else:
  icmp_scan(network) # Run ICMP scan

print("=========================================")
