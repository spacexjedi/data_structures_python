# -*- coding: utf-8 -*-

import json
import requests
import struct

class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()

    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

    def getVertices(self):
        return list(self.gdict.keys())

    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []

def preprocessing(file):
    
    pokemons = []

    for i in range(1, 151):
        numPokemon = str(i)
        url = "https://pokeapi.co/api/v2/pokemon/"+ numPokemon +"/"

        response = requests.get(url)
        todos = json.loads(response.text)

        num = i
        name = str(todos["forms"][0]["name"])
        xp = todos["base_experience"]

        pokemons.append([num,name,xp])

    with open(file, 'w') as outfile:
        json.dump(pokemons, outfile)

def populate(graph, pokemons):
    for i in range(0, 151):
        graph.addVertex(pokemons[i][1])

    return graph

def readFile(file):

    with open(file) as json_data:
        array = json.load(json_data)

    return array

def tournmentGraph(graph, pokemons): #Retorna o grafo de torneio (todos contra todos) e o vencedor
    
    graph = populate(graph,pokemons)
    
    w = 0

    # for i in range(0, 151):
    #     for j in range(0,151):
    #         if(i != j):
    #             graph.AddEdge({pokemons[i][1],pokemons[j][1]})
    #     if(pokemons[i][2] >= pokemons[w][2]):
    #       w = i

    for i in range(0, 151):
        if(pokemons[w][2] != pokemons[i][2]):
            print(pokemons[w][1] + ' x ' + pokemons[i][1])
            if(pokemons[i][2] >= pokemons[w][2]):
                w = i
            print('vencedor: ' + pokemons[w][1] + '\n')

    return graph, pokemons[w][1]

def tournment(pokemons, graph, opponent): #Dado um pokémon retorna todos os pokémons que perdem para ele

    graph = populate(graph,pokemons)
    
    for i in range(0, 151):
        if(opponent == pokemons[i][1]):
            n_opponent = i

    print('\nBatalhas ganhas por: ' + pokemons[n_opponent][1] + '\n')
    for i in range(0, 151):
        if(pokemons[n_opponent][2]>pokemons[i][2]):
            print(str(pokemons[n_opponent][1]) + ' x ' + str(pokemons[i][1]))
            graph.AddEdge({pokemons[n_opponent][1],pokemons[i][1]})

    print('\nBatalhas perdidas por: ' + pokemons[n_opponent][1] + '\n')
    for i in range(0, 151):
        if(pokemons[i][2]>pokemons[n_opponent][2]):
            print(str(pokemons[n_opponent][1]) + ' x ' + str(pokemons[i][1]))
            graph.AddEdge({pokemons[n_opponent][1],pokemons[i][1]})

    return graph

def stronglyConnectedComponents(graph, pokemons): #Retorna os componentes fortemente conexos

    graph = populate(graph,pokemons)

    for i in range(0, 151):
        for j in range(0, 151):
            if(pokemons[i][1] != pokemons[j][1]):
                if(pokemons[i][2] == pokemons[j][2]):
                    graph.AddEdge({pokemons[i][1],pokemons[j][1]})

    return graph

pokemons = readFile('data.json')

graph_elements = {}
g = graph(graph_elements)


#g, winner = tournmentGraph(g,pokemons)
#print('vencedor final: ' + winner)

stronglyConnectedComponents(g,pokemons)
#g = tournment(pokemons, g, 'bulbasaur')
#print(g.getVertices())
print(g.edges())