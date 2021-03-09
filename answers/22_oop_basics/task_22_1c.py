# -*- coding: utf-8 -*-

"""
Task 22.1c

Copy the Topology class from task 22.1b and modify it.

Add a delete_node method that deletes all connections to the specified device.

If there is no such device, the message "There is no such device" is printed.

Topology creation:
In [1]: t = Topology(topology_example)

In [2]: t.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Removing a device:
In [3]: t.delete_node('SW1')

In [4]: t.topology
Out[4]:
{('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

If there is no such device, the following message is printed:
In [5]: t.delete_node('SW1')
There is no such device

"""

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        normalized_topology = {}
        for box, neighbor in topology_dict.items():
            if not neighbor in normalized_topology:
                normalized_topology[box] = neighbor
        return normalized_topology

    def delete_link(self, from_port, to_port):
        if self.topology.get(from_port) == to_port:
            del self.topology[from_port]
        elif self.topology.get(to_port) == from_port:
            del self.topology[to_port]
        else:
            print("There is no such link")

    def delete_node(self, node):
        original_size = len(self.topology)
        for src, dest in list(self.topology.items()):
            if node in src or node in dest:
                del self.topology[src]
        if original_size == len(self.topology):
            print("There is no such device")

