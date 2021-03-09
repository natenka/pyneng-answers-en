# -*- coding: utf-8 -*-
"""
Task 12.2

The ping_ip_addresses function from task 12.1 only accepts a list of addresses,
but it would be convenient to be able to specify addresses using a range,
for example 192.168.100.1-10.

In this task, you need to create a function convert_ranges_to_ip_list that
converts a list of IP addresses in different formats into a list where each
IP address is listed separately.

The function expects as an argument a list containing IP addresses
and/or ranges of IP addresses.

List items can be in the format:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

If the address is specified as a range, the range must be expanded into
individual addresses, including the last address in the range.
To simplify the task, we can assume that only the last octet of the
address changes in the range.

The function returns a list of IP addresses.

For example, if you pass the following list to the convert_ranges_to_ip_list function:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

The function should return a list like this:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress


def convert_ranges_to_ip_list(ip_addresses):
    ip_list = []
    for ip_address in ip_addresses:
        if "-" in ip_address:
            start_ip, stop_ip = ip_address.split("-")
            if "." not in stop_ip:
                stop_ip = ".".join(start_ip.split(".")[:-1] + [stop_ip])
            start_ip = ipaddress.ip_address(start_ip)
            stop_ip = ipaddress.ip_address(stop_ip)
            for ip in range(int(start_ip), int(stop_ip) + 1):
                ip_list.append(str(ipaddress.ip_address(ip)))
        else:
            ip_list.append(str(ip_address))
    return ip_list
