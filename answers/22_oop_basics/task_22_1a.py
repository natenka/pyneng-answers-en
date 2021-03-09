# -*- coding: utf-8 -*-

"""
Task 22.1a

Copy the Topology class from task 22.1 and modify it.

Transfer the functionality of removing "duplicates" to the _normalize method.
In this case, the __init__ method should look like this:
"""

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        return {
            min(local, remote): max(local, remote)
            for local, remote in topology_dict.items()
        }

