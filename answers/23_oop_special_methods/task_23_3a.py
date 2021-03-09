# -*- coding: utf-8 -*-

"""
Task 23.3a

In this task, you need to make sure that instances of the Topology class
are iterables. The base of the Topology class can be taken from either
task 22.1x or task 23.3.

After creating an instance of a class, the instance should act like
an iterable object. Each iteration should return a tuple that describes
one connection. The order of output of connections can be any.


An example of how the class works:

In [1]: top = Topology(topology_example)

In [2]: for link in top:
   ...:     print(link)
   ...:
(('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
(('R2', 'Eth0/0'), ('SW1', 'Eth0/2'))
(('R2', 'Eth0/1'), ('SW2', 'Eth0/11'))
(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
(('R3', 'Eth0/2'), ('R5', 'Eth0/0'))

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

    def __add__(self, other):
        return Topology({**self.topology, **other.topology})

    def __iter__(self):
        return iter(self.topology.items())
