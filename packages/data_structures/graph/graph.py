import numbers
from .node import Node
from .edge import Edge
from typing import Generic, TypeVar

T = TypeVar('T')

class Graph(Generic[T]):
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

  def add_node(self, value):
    new_id = self.__generate_next_node_id()
    new_node = Node[T](new_id, value=value)
    self.nodes[new_id] = new_node

    return new_node

  def __generate_next_node_id(self):
    new_id = len(self.nodes)
    return new_id

  def add_edge(self, source, destination, value):
    self.__process_inputs(source, destination, self.__add_edge, value)

  def __add_edge(self, source_node, destination_node, value=None):
    new_edge = Edge(
      id = self.__generate_next_edge_id(),
      value = value,
      source = source_node,
      destination = destination_node
    )

    self.edges.append(new_edge)

    self.nodes[source_node.id].adjacents.append(new_edge)

    if not self.directed:
      self.nodes[destination_node.id].adjacents.append(new_edge)

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

  """
  Process source and destination inputs.
  """
  def __process_inputs(self, source, destination, method, *args):
    if isinstance(source, Node) and isinstance(destination, Node):
      return method(source, destination, *args)
    elif isinstance(source, numbers.Number) and isinstance(destination, numbers.Number):
      source_node = self.get_node(source)
      destination_node = self.get_node(destination)

      return method(source_node, destination_node, *args)

