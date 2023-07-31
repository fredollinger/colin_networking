from colin_networking.Network import Network
from colin_networking.ECU import ECU

from typing import Dict

class NetworkInventory:

    """Network and ECU Inventory class."""

    def __init__(self):
        """Constructor."""

        """
        networks

        key = name of network
        value = Network
        """
        self.networks: Dict[str, Network] = {}
        """ecu_list

        Pair up each ECU with a network

        key = name_of_network
        value = ECU
        
        """
        self.ecus: Dict[str, ECU] = {}

    def add_network(self, network: Network):
        """Add a New Network."""

        # All networks have names so add to a dict by name
        self.networks[network.name] = network

    def add_ecu(self, network_name: str, ecu: ECU):
        self.ecus[network_name] = ecu