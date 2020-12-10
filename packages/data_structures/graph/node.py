from abc import abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
  """
  Represent a node in a graph.

  id: identificator of the node. It allows differentiate it from others.
  value: Any static data you want to store.
  adjacents: List of edges. Indicate the connection between this node and others.
  """
  def __init__(self, id, value=None, adjacents=None):
    self.id: int = id
    self.value: T = value 
    self.adjacents: List[Node[T]] = adjacents if adjacents else []

  def __str__(self):
    return f"Node(id: {self.id}, value: {self.value})"

  def __gt__(self, other):
    if isinstance(other, Node):
      return self.value > other.value

    return False

  def __lt__(self, other):
    if isinstance(other, Node):
      return self.value < other.value

    return False

