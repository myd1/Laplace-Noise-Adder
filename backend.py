import networkx as nx
import matplotlib.pyplot as plt

def nodeReader(fileName , nodes):
   try:
      with open(fileName,"r") as file:
         for line in file:
            try:
               nodes.append(int(line))
            except ValueError as v:
               print ("file found an invalid node : ", v)
               continue
      return nodes
   except FileNotFoundError as e :
      print("file was not found : ", e)

def edgeReader(fileName,edges):
   try:
      with open(fileName, "r") as file:
         for line in file:
            try:
               v1,v2 = line.split(' ')
               edges.append((int(v1),int(v2)))
            except ValueError as v:
               print("file has an invalid edge : ",v)
               continue
      return edges
   except FileNotFoundError as e :
      print("file was not found : ", e)

def drawGraph(graph):
   nx.draw(graph,node_size=100)
   plt.savefig("images/network.png",figsize=(5.333,4),dpi=50)
   plt.gcf().clear()

def clearNetwork(graph):
   graph.clear()
   drawGraph(graph)
   return graph

def generateNetwork(nodes,edges,graph):
   graph.add_nodes_from(nodes)
   graph.add_edges_from(edges)
   drawGraph(graph)
   return graph

def getstats(graph):
  mainstring = "Stats:\n"
  mainstring += "No of Nodes : "+str(len(graph))+"\n"
  mainstring += "No of Edges : "+str(graph.number_of_edges())+"\n"
  return mainstring