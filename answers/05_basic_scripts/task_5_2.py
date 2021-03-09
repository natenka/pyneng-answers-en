# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

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

print(ip_output.format(oct1, oct2, oct3, oct4))
print(mask_output.format(mask, m1, m2, m3, m4))
