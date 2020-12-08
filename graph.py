import numbers

"""
Represent a node in a graph.
"""
class Node:
  """
  id: identificator of the node. It allows differentiate it from others.
  value: Any static data you want to store.
  adjacents: List of edges. Indicate the connection between this node and others.
  """
  def __init__(self, id, value=None, adjacents=None):
    self.id = id
    self.value = value 
    self.adjacents = adjacents if adjacents else []

  def __str__(self):
    return f"Node(id: {self.id}, value: {self.value})"

  def __eq__(self, other):
    if isinstance(other, Node):
      return self.id == other.id

    return False

class Edge:
  """
  value: Symbol of the transition
  source: Node source
  destination Node destination
  """
  def __init__(self, id, source, destination, value=None):
    self.id = id
    self.source = source
    self.destination = destination
    self.value = value

  def __str__(self):
    return f"Edge(id: {self.id}, value: {self.value}, source: {self.source}, destination: {self.destination})"

class Graph:
  def __init__(self, is_directed=True):
    self.nodes = {} # Nodes dictionary.
    self.edges = [] # List of edges.
    self.directed = is_directed
  
  """
  DFS
  """
  def has_path_dfs(self, source, destination):
    visited_nodes = set()
    return self.__process_inputs(source, destination, self.__has_path_dfs, visited_nodes)

  def __has_path_dfs(self, source, destination, visited_nodes):
    if source.id in visited_nodes:
      return False

    visited_nodes.add(source.id)

    if source == destination:
      return True

    for adjacent_edge in source.adjacents:
      there_is_path = self.__has_path_dfs(adjacent_edge.destination, destination, visited_nodes)
      if there_is_path:
        return True

    return False

  """
  BFS
  """
  def has_path_bfs(self, source, destination):
    return self.__process_inputs(source, destination, self.__has_path_bfs)

  def __has_path_bfs(self, source, destination):
    visited_nodes = set()
    unvisited_adjacent_nodes = [source]

    while len(unvisited_adjacent_nodes):
      node = unvisited_adjacent_nodes.pop(0)

      destination_node_is_found = node == destination
      if destination_node_is_found:
        return True

      has_been_visited = node.id in visited_nodes
      if has_been_visited:
        continue

      visited_nodes.add(node.id)

      for child_edge in node.adjacents:
        unvisited_adjacent_nodes.append(child_edge.destination)

    return False

  """
  Process source and destination inputs.
  """
  def __process_inputs(self, source, destination, method, *args):
    if isinstance(source, Node) and isinstance(destination, Node):
      return method(source, destination, *args)
    elif isinstance(source, numbers.Number):
      source_node = self.get_node(source)
      destination_node = self.get_node(destination)

      return method(source_node, destination_node, *args)

  def add_node(self, value):
    new_id = self.__generate_next_node_id()
    new_node = Node(new_id, value=value)
    self.nodes[new_id] = new_node

    return new_node

  def __generate_next_node_id(self):
    new_id = len(self.nodes)
    return new_id

  def add_edge(self, source_id, destination_id, value=None):
    new_edge = Edge(
      id = self.__generate_next_edge_id(),
      value = value,
      source = self.get_node(source_id),
      destination = self.get_node(destination_id)
    )

    self.edges.append(new_edge)

    self.nodes[source_id].adjacents.append(new_edge)

    if not self.directed:
      self.nodes[destination_id].adjacents.append(new_edge)

    return new_edge

  def __generate_next_edge_id(self):
    last_edge = self.edges[-1] if self.edges else None
    return last_edge.id + 1 if last_edge else 0

  def get_node(self, id):
    node_exists = True if id >= 0 and id < len(self.nodes) else False
    if node_exists:
      return self.nodes[id]
    else:
      print("NODE DOESN'T EXISTS")
      return None

