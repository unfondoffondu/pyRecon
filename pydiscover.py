#   About:          Simple script that uses fping to scan a subnet quickly with a decent output.
#
#   Author:         Jeff Schowe
#
#   Disclaimer:     This is meant to be used in a lab setting against willing targets and should not ever be used against anything ever.  For educational purposes only.
#                   There is no warranty, use at your own risk, I am not responsible for your actions etc.
#
#   License:        Feel free to use and do whatever you want with this software.  Make it better, but if you enjoy it or want to help make it better or just wanna provide
#                   some feedback, that would make my day.  Cheers!
#
#   Bugs:           Probably lots.  Seems to work okay, needs further testing.
import subprocess as sp

def scan(ip):

    print(f"Scanning range {ip}1/24")
    hosts = []
    ip_address = ip
    for i in range(255):

        ip_address = ip + str(i)
        ip_response = sp.getoutput(f"fping -t100 -c 1 {ip_address} &").split()
        if ip_response[3] == "64":
            hosts.append(ip_address)
            print(f"Host responded: {ip_address}")

    print(f"finished scanning subnet, added {len(hosts)} host(s)..")

    return hosts

if __name__ == "__main__":
    ip = input("Enter first 3 octets of network to scan followed by a . like such 10.0.2.")
    scan(ip)
