Olá! Que bom que você está aprendendo sobre grafos em Python. Vamos entender esses métodos de forma bem simples:

possuiVertice(self, v)
Este método verifica se um vértice (pense em um ponto ou nó no seu grafo) já existe. Ele retorna True se o vértice v estiver na lista_adjacencia (que é basicamente onde seu grafo "guarda" os vértices e suas conexões), e False caso contrário.

possuiAresta(self, v1, v2)
Aqui, estamos checando se existe uma aresta (uma linha que conecta dois vértices) entre o vértice v1 e o vértice v2. Ele verifica se v2 está na lista de vizinhos de v1. Se sim, significa que há uma aresta de v1 para v2, e o método retorna True. Caso contrário, retorna False.

adicionarVertice(self, v)
Este método serve para incluir um novo vértice no seu grafo. Antes de adicionar, ele usa o possuiVertice para garantir que o vértice v ainda não exista. Se não existir, ele o adiciona à lista_adjacencia.

removerVertice(self, v)
Como o nome sugere, este método tira um vértice do grafo. Primeiro, ele verifica se o vértice v realmente existe usando possuiVertice. Se existir, ele remove esse vértice (e todas as suas conexões) da lista_adjacencia.

adicionarAresta(self, v1, v2)
Este método é para criar uma conexão (aresta) entre dois vértices, v1 e v2. Ele só adiciona a aresta se ambos os vértices já existirem no grafo (verificando com possuiVertice). Se ambos existirem, ele cria a ligação de v1 para v2.

removerAresta(self, v1, v2)
Este método desfaz uma conexão (aresta) entre v1 e v2. Assim como para adicionar, ele primeiro verifica se ambos os vértices existem. Se existirem, ele remove a ligação de v1 para v2.

grauDeEntrada(self, v)
Imagine um vértice v. O "grau de entrada" dele é o número de arestas que "chegam" nesse vértice v vindas de outros vértices. O método percorre todos os outros vértices no grafo e conta quantas vezes o vértice v aparece como destino de uma aresta.

grauDeSaida(self, v)
Para um vértice v, o "grau de saída" é o número de arestas que "partem" dele para outros vértices. É mais simples de calcular: se o vértice v existe, o método apenas conta quantas conexões ele tem com outros vértices.

Espero que essa explicação tenha sido útil! Se tiver mais alguma dúvida, é só perguntar.
