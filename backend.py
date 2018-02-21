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

def manhattan_distance(x,y):
   return sum(abs(a-b) for a,b in zip(x,y))

def globalSensitivity(graph):
   gs = 0
   graph1 = graph.copy()
   nodes = graph.nodes()
   vectors = []
   vectors.append(nx.degree_histogram(graph1))
   for node in nodes:
      graph1 = graph.copy()
      graph1.remove_node(node)
      temp = nx.degree_histogram(graph1)
      while(len(temp) < len(vectors[0])):
         temp.append(0)
      vectors.append(temp)
      temp1 = manhattan_distance(vectors[0],vectors[len(vectors)-1])
      if(temp1 > gs):
         gs = temp1        
   return gs      

def noise(x, u, e, f):
   return (e/2*f)*exp(-abs(x-u)*e/F)