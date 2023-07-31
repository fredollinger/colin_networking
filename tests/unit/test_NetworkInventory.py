from colin_networking.NetworkInventory import NetworkInventory
from colin_networking.Network import Network

def test_NetworkInventory_add_network():
    ni: NetworkInventory = NetworkInventory()
    network1: Network = Network("network1")
    network2: Network = Network("network2")
    ni.add_network(network1)
