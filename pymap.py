#   About:       A quick no frills (yet) port scanner.  The service is just a guess based off of the port number, so no promises.  Needs some work,
#                but functions fairly well.  Tested against metasploitable, probably will not work against any Microsoft targets unless modified.
#   Author:      Jeff Schowe----Github: unfondoffondu-----E-mail jaschowe@gmail.com

#   Disclaimer:  This is made for educational purposes only and meant for use in a lab environment against willing targets.  The Author takes no
#                responsibility for how this is used.  Use at your own risk.

#   License:     Feel free to use it and modify and make it your own, redistribute it.

#   Bugs:        I am sure there are a lot of them.  Please report to me any you find, and I would *LOVE* any feedback at all.  The service
#                detection feature isn't necessarily accurate, and goes by common uses of the port in question.  I need to do more research
#                into the output of my connection to try to be more accurate and gather more information.  This is just a start.

import socket
import time
from clr import clr
def scan(target):
    clr()

    targetIP = socket.gethostbyname(target)

    port_low_range = int(input("enter lower limit of port range: "))
    port_high_range = int(input(("enter higher limit of port range: ")))
    print("-" * 60, "\n")

    print(f"target: {target}")
    total_open = 0
    open_ports = []
    print(f"\nport", " " * 5, "state", " " * 4, "service")
    start = time.time()

    for port in range(port_low_range, port_high_range + 1):
        service = ""
        formatter = len(str(port))
        if port != port_high_range-1:
            print(f"{port}", end="")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((targetIP, port))
        print(end="\r")
        if result == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "unknown"
            open_ports.append((port, service))
            total_open += 1
            print(f"\r{port}", " " * (10 - formatter) + "open", " " * 5, f"{service}")
        sock.close()

    print("\n")
    stop = time.time() - start
    print(f"{total_open} open ports in {round(stop)} earth time units.")
    print("\n", "-" * 60)

    return open_ports
