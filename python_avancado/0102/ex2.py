import heapq

dados_grafo = {
    'A': {'B': 3, 'C': 2, 'D': 5},
    'B': {'A': 3, 'C': 1, 'E': 4},
    'C': {'A': 2, 'B': 1, 'D': 2, 'F': 6},
    'D': {'A': 5, 'C': 2, 'F': 1, 'G': 7},
    'E': {'B': 4, 'F': 3},
    'F': {'C': 6, 'D': 1, 'E': 3, 'G': 4},
    'G': {'D': 7, 'F': 4}
}

class GrafoPonderado:
    def __init__(self):
        self.grafo_dict = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo_dict:
            self.grafo_dict[vertice] = {}

    def adicionar_aresta(self, origem, destino, peso):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.grafo_dict[origem][destino] = peso
        self.grafo_dict[destino][origem] = peso

    def dijkstra(self, origem):
        fila_prioridade = [(0, origem)]
        distancia = {vertice: float('infinity') for vertice in self.grafo_dict}
        distancia[origem] = 0

        while fila_prioridade:
            (dist_atual, vertice_atual) = heapq.heappop(fila_prioridade)

            for vizinho, peso in self.grafo_dict[vertice_atual].items():
                nova_distancia = dist_atual + peso
                if nova_distancia < distancia[vizinho]:
                    distancia[vizinho] = nova_distancia
                    heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

        return distancia


grafo_ponderado = GrafoPonderado()

for origem, destinos in dados_grafo.items():
    for destino, peso in destinos.items():
        grafo_ponderado.adicionar_aresta(origem, destino, peso)

resultados_dijkstra = grafo_ponderado.dijkstra('A')
print("Distâncias mínimas:", resultados_dijkstra)
