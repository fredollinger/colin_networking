from colin_networking.Network import Network
from colin_networking.ECU import ECU

from typing import List

class NetworkInventory:

    """Network and ECU Inventory class."""

    def __init__(self):
        """Constructor."""
        self.networks: List[Network] = {}
        self.ecu_list: List[ECU] = []

    def add_network(self, network: Network):
        """Add a New Network."""

        # All networks have names so add to a dict by name
        self.networks[network.name] = network
