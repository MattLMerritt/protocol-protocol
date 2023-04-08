from generate_json import GenerateJson
from device import Device
from wire import Wire
import networkx as nx


if __name__ == "__main__":
    # G = nx.Graph()
    
    
    # G = nx.complete_graph(6)
    # G = nx.complete_bipartite_graph(2, 5)
    # G = nx.barbell_graph(10, 10)
    # G = nx.lollipop_graph(5, 5)
    # G = nx.erdos_renyi_graph(10, 0.5)
    G = nx.watts_strogatz_graph(50, 4, 0.5)
    # G = nx.barabasi_albert_graph(50, 2)
    # G = nx.random_lobster(7, 0.7, 0.7)
    
    time_steps = 10
    world_devices = {}
    world_wires = {}
    
    num_devices = len(G)
    num_wires = 0
    
    for node in G:
        world_devices[node] = Device(node)
    
    for node in G:
        for edge in G[node]:
            world_wires[num_wires] = Wire(num_wires, node, edge, world_devices, 0)
            num_wires += 1
    
    # export data
    gen_json = GenerateJson(time_steps, world_devices, world_wires)
    gen_json.export_data_to_json()


















            
            