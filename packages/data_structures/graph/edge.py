from .node import Node
from typing import TypeVar, Generic

T = TypeVar('T')
U = TypeVar('U')

class Edge(Generic[T, U]):
  def __init__(
    self,
    id: int,
    source: Node[T],
    destination: Node[T],
    value: U = None
  ):
    self.id = id
    self.source = source
    self.destination = destination
    self.value = value

  def __str__(self):
    return f"Edge(id: {self.id}, value: {self.value}, source: {self.source}, destination: {self.destination})"
