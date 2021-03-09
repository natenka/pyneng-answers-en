# -*- coding: utf-8 -*-
"""
Task 5.2a

Copy and modify the script from task 5.2 so that, if the user entered a host address
rather than a network address, convert the host address to a network address
and print the network address and mask, as in task 5.2.

An example of a network address (all host bits are equal to zero):
* 10.0.1.0/24
* 190.1.0.0/16

Host address example:
* 10.0.1.1/24 - host from network 10.0.1.0/24
* 10.0.5.195/28 - host from network 10.0.5.192/28

If the user entered the address 10.0.1.1/24, the output should look like this:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different host/mask combinations, for example:
    10.0.5.195/28, 10.0.1.1/24

Hint:
The network address can be calculated from the binary host address and the netmask.
If the mask is 28, then the network address is the first 28 bits host addresses + 4 zeros.
For example, the host address 10.1.1.195/28 in binary will be:
bin_ip = "00001010000000010000000111000011"

Then the network address will be the first 28 characters from bin_ip + 0000
(4 because in total there can be 32 bits in the address, and 32 - 28 = 4)
00001010000000010000000111000000

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

network = input("Введите адрес сети: ")

ip, mask = network.split("/")
ip_list = ip.split(".")
mask = int(mask)

oct1, oct2, oct3, oct4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3]),
]
bin_ip_str = "{:08b}{:08b}{:08b}{:08b}".format(oct1, oct2, oct3, oct4)
bin_network_str = bin_ip_str[:mask] + "0" * (32 - mask)

net1, net2, net3, net4 = [
    int(bin_network_str[0:8], 2),
    int(bin_network_str[8:16], 2),
    int(bin_network_str[16:24], 2),
    int(bin_network_str[24:32], 2),
]

bin_mask = "1" * mask + "0" * (32 - mask)
m1, m2, m3, m4 = [
    int(bin_mask[0:8], 2),
    int(bin_mask[8:16], 2),
    int(bin_mask[16:24], 2),
    int(bin_mask[24:32], 2),
]

ip_output = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

mask_output = """
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(ip_output.format(net1, net2, net3, net4))
print(mask_output.format(mask, m1, m2, m3, m4))
