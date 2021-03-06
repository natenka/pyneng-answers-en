# -*- coding: utf-8 -*-

"""
Task 23.1

In this task, you must create an IPAddress class.

When creating an instance of a class, the IP address and mask are passed
as an argument, and the correctness of the address and mask must be checked:
* The address is considered to be correctly specified if it:
    - consists of 4 numbers separated by a dot
    - every number in the range from 0 to 255
* the mask is considered correct if the mask is a number and a number in
  the range from 8 to 32 inclusiveA


If the mask or address fails validation, you must raise a ValueError
with the appropriate text (output below).

Also, when creating a class, two instance variables must be created: ip and mask,
which contain the address and mask, respectively.

An example of creating an instance of a class:
In [1]: ip = IPAddress('10.1.1.1/24')

ip and mask attributes
In [2]: ip1 = IPAddress('10.1.1.1/24')

In [3]: ip1.ip
Out[3]: '10.1.1.1'

In [4]: ip1.mask
Out[4]: 24

Checking the correctness of the address (traceback is shortened)
In [5]: ip1 = IPAddress('10.1.1/24')
---------------------------------------------------------------------------
...
ValueError: Incorrect IPv4 address

Checking the correctness of the mask (traceback is shortened)
In [6]: ip1 = IPAddress('10.1.1.1/240')
---------------------------------------------------------------------------
...
ValueError: Incorrect mask

"""
import ipaddress


class IPAddress:
    def __init__(self, ipaddress):
        ip, mask = ipaddress.split("/")
        self._check_ip(ip)
        self._check_mask(mask)
        self.ip, self.mask = ip, int(mask)

    def _check_ip(self, ip):
        octets = ip.split(".")
        correct_octets = [
            octet for octet in octets if octet.isdigit() and 0 <= int(octet) <= 255
        ]
        if len(octets) == 4 and len(correct_octets) == 4:
            return True
        else:
            raise ValueError("Incorrect IPv4 address")

    def _check_mask(self, mask):
        if mask.isdigit() and 8 <= int(mask) <= 32:
            return True
        else:
            raise ValueError("Incorrect mask")
