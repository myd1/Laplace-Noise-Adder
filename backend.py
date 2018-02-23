import networkx as nx
import matplotlib.pyplot as plt
from numpy import exp
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
  mainstring += "Global Sensitivity : "+str(globalSensitivity(graph))
  return mainstring , globalSensitivity(graph)

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


def noise(x, mean, epsilon, glblSenstvt):
   return (epsilon/2*glblSenstvt)*exp(-abs(x-mean)*epsilon/glblSenstvt)


def scaleValues( arr ):
   u = []
   if max(arr) >= 10 :
      for t in range(1,6):
         u.append(round(max(arr)*t/5))
      return u
   else :
      return arr


def drawHistogram(arr,fileName):

   # fig = plt.figure(figsize=(13, 7), dpi=100, tight_layout=True)
   #  360 × 270 pix ==  4 × 3 inc , 100 dpi
   # 1280 × 720 pix ==  13 × 7 inc , 100 dpi
   n = len(arr)
   x = range(n)
   plt.bar(x,arr,align='center',width=0.95)
   x = scaleValues(x)
   plt.xticks(x)
   arr = scaleValues(arr)
   plt.yticks(arr)
   plt.xlabel('Degree')
   plt.ylabel('number of node')
   plt.savefig("images/"+fileName+".png",figsize=(6,4.5),dpi=57)
   plt.gcf().clear()
   

def anonimizer(graph,epsilon):
   degreeSeq = nx.degree_histogram(graph)
   mean = sum(degreeSeq)/len(degreeSeq)
   glblSenstvt = globalSensitivity(graph)
   for x in range(len(degreeSeq)):
      degreeSeq[x] += noise(x, mean, epsilon, glblSenstvt)
      degreeSeq[x] = round(degreeSeq[x])
   return degreeSeq   