
import networkx as nx
import random

def p2p_graph(oneway = False):
    G = nx.DiGraph()
    G.add_edge(0, 1)
    if not oneway:
        G.add_edge(1, 0)
    return G


def ring_graph(numnodes, oneway = False):
    if numnodes < 2:
        raise ValueError("To make a ring graph, you should have at least 2 nodes")
        
    G = nx.DiGraph()
    for i in range(numnodes):
        G.add_edge(i, (i + 1) % numnodes)
    
    if numnodes == 2 or oneway == True: 
        return G
    
    for i in range(numnodes):
        G.add_edge((i + 1) % numnodes, i)
    return G


def mesh_graph(numnodes):
    if numnodes < 2: 
        raise ValueError("To make a mesh graph, you should have at least 2 nodes")
    
    G = nx.DiGraph()
    for i in range(numnodes):
        for j in range(numnodes):
            if i == j: continue
            G.add_edge(i, j)
    
    return G



def merge_graph(G1, G2, rename = ("L", "R")):
    G = nx.union(G1, G2, rename = (rename[0], rename[1]))
    random_edge_G1 = str(random.choice(list(G1.edges()))[0])
    random_edge_G2 = str(random.choice(list(G2.edges()))[0])
    G.add_edge(rename[0]+random_edge_G1, rename[1]+random_edge_G2)
    return G


