grafo = {
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Timisoara': {'Lugoj': 111, 'Arad': 118},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Pitesti': 138, 'Rimnicu Vilcea': 146},
    'Arad': {'Timisoara': 118, 'Sibiu': 140, 'Zerind': 75},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Oradea': {'Sibiu': 151, 'Zerind': 71},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
}

heuristica_distancia = {
    'Lugoj': 244,
    'Timisoara': 329,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Arad': 366,
    'Sibiu': 253,
    'Oradea': 380,
    'Fagaras': 178,
    'Rimnicu Vilcea': 193,
    'Pitesti': 100,
    'Zerind': 374,
    'Bucharest': 0
}

def busca_gulosa(origem, grafo, destino, heuristica):
    fila = [(heuristica[origem], origem)]
    visitados = set()
    caminho_dict = {}

    while fila:
        _, cidade = fila.pop(0)

        if cidade == destino:
            caminho = [cidade]
            pai = caminho_dict[cidade]
            while pai:
                caminho.append(pai)
                pai = caminho_dict.get(pai)
            return caminho

        visitados.add(cidade)

        for vizinha, distancia in grafo[cidade].items():
            if vizinha not in visitados:
                estimativa_vizinha = heuristica[vizinha]
                fila.append((estimativa_vizinha, vizinha))
                caminho_dict[vizinha] = cidade

origem = 'Mehadia'
destino = 'Pitesti'
caminho = busca_gulosa(origem, grafo, destino, heuristica_distancia)
print("Caminho encontrado:", " -> ".join(reversed(caminho)))
