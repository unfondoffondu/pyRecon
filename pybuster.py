#                   to implement a failsafe measure, but it needs further testing on different targets.  Once again, big thanks to my boy David Bombal and big shoutout to
#                   network Chuck for the inspiration.
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
#

import requests
import time
from clr import clr
def scan(target, scan_timer):
    returns = []
    with open("wordlist.txt") as file:
        words = file.read()

    words = words.split()
    positives = []

    print("starting subdirectory sweep...")
    start = time.time()
    for i in words:
        time.sleep(scan_timer)
        r = requests.get(f"http://{target}/{i}")
        response = str(r)[11:].strip("]>")
        if response != "404":
            print(i, response)
        if response == "200":
            positives.append(i)

    stop = time.time() - start
    print(f"found {len(positives)} positive responses in {round(stop)} human time factorials.")
    returns.append(positives)

    if input("brute directories found in initial sweep? ") == "y":

        r_positives = []
        start = time.time()
        print("Starting recursion sweep.....")
        for i in positives:
            response_limiter = 0
            for j in words:
                if response_limiter == 1:
                    print(f"/{i}/ responds to anything...")
                    break

                r = requests.get(f"http://{target}/{i}/{j}")
                response = str(r)[11:].strip("]>")
                if response == "200":
                    print(f"{i}/{j} {response}")
                    r_positives.append(j)
                    response_limiter += 1
        stop = time.time() - start
        print(f"found {len(r_positives)} subdirectories responses in {round(stop)} earth time modules.")
        returns.append(r_positives)
    else:
        print("have a nice day.")
        return returns
    return returns

if __name__ == "__main__":
    target = input("Enter target IP or Domain: ")
    scan_timer = float(input("Enter time between requests."))
    scan(target, scan_timer)
