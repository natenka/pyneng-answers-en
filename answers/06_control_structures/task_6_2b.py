# -*- coding: utf-8 -*-
"""
Task 6.2b

Make a copy of the code from the task 6.2a.

Add this functionality: If the address was entered incorrectly, request the address again.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

while True:
    ip_address = input("Enter IP address: ")
    octets = ip_address.split(".")
    correct_ip = True

    if len(octets) == 4:
        for octet in octets:
            if not (octet.isdigit() and int(octet) in range(256)):
                correct_ip = False
                break
    else:
        correct_ip = False
    if correct_ip:
        break
    print("Invalid IP address")

first_octet = int(octets[0])

if 1 <= first_octet <= 223:
    print("unicast")
elif 224 <= first_octet <= 239:
    print("multicast")
elif ip_address == "0.0.0.0":
    print("unassigned")
elif ip_address == "255.255.255.255":
    print("local broadcast")
else:
    print("unused")

# second version

while True:
    ip = input("Enter IP address: ")
    octets = ip.split(".")
    valid_ip = len(octets) == 4

    for i in octets:
        valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip

    if valid_ip:
        break
    print("Invalid IP address")

if 1 <= int(octets[0]) <= 223:
    print("unicast")
elif 224 <= int(octets[0]) <= 239:
    print("multicast")
elif ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
else:
    print("unused")

