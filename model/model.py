import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._all_airports = []
        self._id_map = {}
    def crea_grafo(self, x):
        # pulizia
        self._grafo.clear()
        #edges
        self._all_airports = DAO.getAllAirports()
        #mappa id per velocizzare collegamento
        self._id_map = {a['ID']: a for a in self._all_airports}
        #aggiungiamo i nodi
        self._grafo.add_nodes_from(self._all_airports)
        #archi
        rotte = DAO.getAllEdgesPesati(x)
        for id1, id2, peso in rotte:
            u = self._id_map[id1]
            v = self._id_map[id2]
            self._grafo.add_edge(u, v, weight=peso)
    def get_num_nodes(self):
        return self._grafo.number_of_nodes()
    def get_num_edges(self):
        return self._grafo.number_of_edges()

    def get_edges_details(self):
        lista = []
        for u, v, d in self._grafo.edges(data=True):
            lista.append(key=lambda x: x[2], reverse=True)
        return lista