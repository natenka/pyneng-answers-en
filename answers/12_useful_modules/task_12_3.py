# -*- coding: utf-8 -*-
"""
Task 12.3

Create a function print_ip_table that prints a table of available
and unavailable IP addresses.

The function expects two lists as arguments:
* list of available IP addresses
* list of unavailable IP addresses

The result of the function is printing a table to the stdout:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate


def print_ip_table(reach_ip, unreach_ip):
    table = {"Reachable": reach_ip, "Unreachable": unreach_ip}
    print(tabulate(table, headers="keys"))


if __name__ == "__main__":
    reach_ip = ["10.1.1.1", "10.1.1.2"]
    unreach_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]
    print_ip_table(reach_ip, unreach_ip)
