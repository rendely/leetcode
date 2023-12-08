import pdb
initial_graph = [
  ['a','b','c'],
  ['d','e','f'],
  ['g','h','i']
]

class Node:
  def __init__(self, value, position=None, connected=[]):
    self.value = value
    self.position = position
    self.connected = connected
  
  def __repr__(self):
    return f'\nNode(value={self.value}, position={self.position}, connected={",".join([c.value for c in self.connected if c != None])})'


class Graph:
  def __init__(self, nodes=[]):
    self.nodes = nodes
  
  def create_nodes(self, graph_string):
    self.height = len(graph_string)
    self.width = len(graph_string[0])
    #create nodes
    for y, row in enumerate(graph_string):
      for x,col in enumerate(row):
        self.nodes.append(Node(value=col, position={'x': x, 'y': y}, connected=[]))

  def get_node(self,x,y):
    for node in self.nodes:
      if node.position == {'x': x, 'y': y}:
        return node
    return None

  def connect_nodes(self):
    for node in self.nodes:
      x = node.position['x']
      y = node.position['y']
      #above
      if y > 0:
        node.connected.append(self.get_node(x,y-1))      
      #below
      if y < self.height-1:
        node.connected.append(self.get_node(x,y+1))   
      #left
      if x > 0:
        node.connected.append(self.get_node(x-1,y))   
      #right
      if x < self.width-1:
        node.connected.append(self.get_node(x+1,y))   

  def get_path(self, node_a, node_b, seen=None, longest=True):
    if seen is None:
        seen = []
    if node_a.position == node_b.position:
        return [node_a.value]

    seen = seen + [node_a]

    paths = []
    for connection in node_a.connected:
        if connection not in seen:
            paths.append(self.get_path(connection, node_b, seen, longest))

    sorted_paths = sorted([path for path in paths if path !=None], key=len, reverse=longest)
    if len(sorted_paths) > 0:
        return [node_a.value] + sorted_paths[0]

    return None


  def __repr__(self):
    return f"Graph(nodes={self.nodes})"

graph = Graph()
graph.create_nodes(initial_graph)
graph.connect_nodes()
# print(graph.nodes)
# print(graph.get_path(graph.nodes[0], graph.nodes[2]))

for i in range(0,8):
  for j in range(0,8):
    if i != j:
      print(i,j)
      print(graph.get_path(graph.nodes[i], graph.nodes[j], longest=True))
# pdb.set_trace()