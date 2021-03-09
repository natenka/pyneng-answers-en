# -*- coding: utf-8 -*-
"""
Task 12.1

Create a ping_ip_addresses function that checks if IP addresses are pingable.

The function expects a list of IP addresses as an argument.

The function must return a tuple with two lists:
* list of available IP addresses
* list of unavailable IP addresses

To check the availability of an IP address, use the ping command.


Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
import subprocess


def ping_ip_addresses(ip_addresses):
    reachable = []
    unreachable = []

    for ip in ip_addresses:
        result = subprocess.run(
            ["ping", "-c", "3", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)

    return reachable, unreachable


if __name__ == "__main__":
    print(ping_ip_addresses(["10.1.1.1", "8.8.8.8"]))
