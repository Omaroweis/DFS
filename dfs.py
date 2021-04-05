import networkx as nx
def dfs(grafo, vertice):
    visitados = set()
    GResultado = nx.Graph()
    GResultado.add_node(1)
    GResultado.add_node(2)
    GResultado.add_node(3)
    GResultado.add_node(4)
    GResultado.add_node(5)
    GResultado.add_node(6)
    
    
    def dfs_recursiva(grafo, vertice, visitados):
        visitados.add(vertice)
        
        for i in grafo[vertice]:
            if i not in visitados:
                GResultado.add_edge(vertice, i)
                dfs_recursiva(grafo, i, visitados)
                
    dfs_recursiva(grafo, vertice, visitados)
    return GResultado
  
