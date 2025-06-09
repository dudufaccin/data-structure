class GrafoOrientado:
    def __init__(self):
        self.lista_adjacencia = {
            "vertice_1": {"vertice_2": True},
            "vertice_2": {"vertice_3": True},
            "vertice_3": {"vertice_2": True},
        }

    def __str__(self):
        if self.lista_adjacencia:
            result = ""
            for n, v1 in enumerate(self.lista_adjacencia):
                result += str(v1) + " : [ "
                for m, v2 in enumerate(self.lista_adjacencia[v1]):
                    result += str(v2)
                    if m < len(self.lista_adjacencia[v1]) - 1:
                        result += " , "
                result += " ] "
                if n < len(self.lista_adjacencia) - 1:
                    result += "\n"
            return result
        return "{}"

    def possuiVertice(self, v):
        return v in self.lista_adjacencia

    def possuiAresta(self, v1, v2):
        return v2 in self.lista_adjacencia[v1]

    def adicionarVertice(self, v):
        if not self.possuiVertice(v):
            self.lista_adjacencia[v] = {}

    def removerVertice(self, v):
        if self.possuiVertice(v):
            del self.lista_adjacencia[v]

    def adicionarAresta(self, v1, v2):
        if self.possuiVertice(v1) and self.possuiVertice(v2):
            self.lista_adjacencia[v1][v2] = True

    def removerAresta(self, v1, v2):
        if self.possuiVertice(v1) and self.possuiVertice(v2):
            del self.lista_adjacencia[v1][v2]

    def grauDeEntrada(self, v):
        if not self.possuiVertice(v):
            return 0
        contador_arestas = 0
        for v_origem in self.lista_adjacencia:
            if v in self.lista_adjacencia[v_origem]:
                contador_arestas += 1
        return contador_arestas

    def grauDeSaida(self, v):
        if self.possuiVertice(v):
            return len(self.lista_adjacencia[v])


# Imprime o grafo
print("Grafo:")
grafo = GrafoOrientado()
print(grafo)

# Verifica se o grafo possui vértices
print("\nPossui vértice?")
print(grafo.possuiVertice("vertice_1"))

# Verifica se os vértices possuem arestas
print("\nPossui aresta?")
print(grafo.possuiAresta("vertice_1", "vertice_2"))

# Adiciona um vértice no grafo
print("\nAdicionando um vértice:")
grafo.adicionarVertice("vertice_4")
grafo.adicionarVertice("vertice_5")
print(grafo)

# Remove um vértice no grafo
print("\nRemovendo um vértice:")
grafo.removerVertice("vertice_5")
print(grafo)

# Adiciona uma aresta
print("\nAdicionando uma aresta:")
grafo.adicionarAresta("vertice_1", "vertice_4")
print(grafo)

# Remove uma aresta
print("\nRemovendo uma aresta:")
grafo.removerAresta("vertice_1", "vertice_4")
print(grafo)

# Grau de entrada
print("\nGrau de entrada:")
print(grafo.grauDeEntrada("vertice_2"))

# Grau de saida
print("\nGrau de saida:")
grafo.grauDeSaida("vertice_1")
print(grafo)
