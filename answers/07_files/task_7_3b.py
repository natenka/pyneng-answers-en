# -*- coding: utf-8 -*-
"""
Task 7.3b

Make a copy of the code from the task 7.3a.

Add this functionality:
- Ask the user to enter the VLAN number.
- Print information only for the specified VLAN.

Output example:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
user_vlan = input("Enter VLAN number: ")

with open("CAM_table.txt", "r") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit() and words[0] == user_vlan:
            vlan, mac, _, intf = words
            print(f"{vlan:9}{mac:20}{intf}")
