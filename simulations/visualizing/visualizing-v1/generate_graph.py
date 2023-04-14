
import networkx as nx


def p2p_graph(oneway = False):
    G = nx.DiGraph()
    G.add_edge(0, 1)
    if not oneway:
        G.add_edge(1, 0)
    return G



