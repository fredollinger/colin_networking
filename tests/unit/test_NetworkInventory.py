from colin_networking.NetworkInventory import NetworkInventory
from colin_networking.Network import Network
from colin_networking.ECU import ECU

def test_NetworkInventory_add_network():
    ni: NetworkInventory = NetworkInventory()
    network1: Network = Network("network1")
    network2: Network = Network("network2")

    ecu1: ECU = ECU("ecu1")
    ecu2: ECU = ECU("ecu2")
    
    ni.add_network(network1)
    ni.add_network(network2)

    # Add both ECUS to network1
    ni.add_ecu("network1", ecu1)
    ni.add_ecu("network1", ecu2)

    assert (2 == len(ni.ecus["network1"]))