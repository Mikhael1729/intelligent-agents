import math
from ..data_structures.priority_queue import PriorityQueue 
from ..data_structures.graph.graph import Graph, Edge
from abc import abstractmethod, ABCMeta
from typing import TypeVar, List, Generic, Callable, Generic
from graphviz import Digraph as VizDigraph, Graph as VizGraph
import numbers

T = TypeVar("T")
U = TypeVar("U")

"""
It can navigate intelligently through a states space graph.
"""
class Agent(Generic[T], metaclass=ABCMeta):
  def __init__(self):
    self.__states_space: Graph[T] = self.create_states_space()
    self.__actions: List[Edge[T, U]] = []

  @property
  def states_space(self) -> Graph[T]:
    return self.__states_space

  @property
  def actions(self):
    return self.__actions

  def state_exists_gbfs(self, goal_state: T) -> (int, List[Edge[T, U]]):
    return self.__state_exists(goal_state, self.heuristic_function)

  def state_exists_asearch(self, goal_state: T) -> (int, List[Edge[T, U]]):
    evaluation_function: Callable[[Edge[T, U]], int] = lambda edge: (
      self.heuristic_function(edge) + self.distance_function(edge, self.actions)
    )

    return self.__state_exists(goal_state, evaluation_function)

  def __state_exists(self, goal_state: T, evaluation_function: Callable[[Edge[T, U]], int]):
    if len(self.__states_space.nodes) == 0:
      return False

    self.__actions = []

    edge = Edge[T, U](
      id = -1,
      source = None,
      destination = self.__states_space.get_node(0),
      value = 0
    )

    path: List[Edge[T, U]] = []
    opened: PriorityQueue[T] = PriorityQueue[Edge[T, U]](
      init_elements=[edge],
      map_value=evaluation_function
    )

    closed: List[Edge[T, U]] = []

    while len(opened) != 0:
      most_promising_path: Edge[T, U] = opened.dequeue()
      path.append(most_promising_path)
      closed.append(most_promising_path)

      self.__actions.append(most_promising_path.id)

      goal_is_found = most_promising_path.destination.value == goal_state
      if goal_is_found:
        closed.append(most_promising_path)
        return (True, path)

      for edge in most_promising_path.destination.adjacents:
        if edge not in closed and edge not in opened:
          opened.enqueue(edge)

    return (False, path)

  @abstractmethod
  def heuristic_function(self, edge: Edge[T, U]) -> int:
    raise NotImplementedError

  def distance_function(self, edge: Edge[T, U], actions: List[Edge[T, U]]) -> int:
    return 0

  @abstractmethod
  def create_states_space(self) -> Graph[T]:
    raise NotImplementedError

  def print_states_space(self) -> None:
    g = VizDigraph('G', filename='./test_output/states_space.gv')

    states_space: Graph[T]= self.states_space

    edge: Edge[T, U]
    for i, edge in enumerate(states_space.edges):
      source_value = str(edge.source.value) 
      destination_value = str(edge.destination.value)
      label = str(edge.value)

      color = None
      if edge.id in self.__actions:
        if self.__actions[-1] == edge.id:
          color = 'red'
        else: 
          color = 'blue'

      g.edge(source_value, destination_value, label=label, color=color )

    g.view()
