import math
from ..data_structures.priority_queue import PriorityQueue 
from ..data_structures.graph.graph import Graph, Edge
from abc import abstractmethod, ABCMeta
from typing import TypeVar, List, Generic, Callable, Generic
import numbers

T = TypeVar("T")

"""
It can navigate intelligently through a states space graph.
"""
class Agent(Generic[T], metaclass=ABCMeta):
  def __init__(self):
    self.__states_space: Graph[T] = self.create_states_space()

  def state_exists_gbfs(self, goal_state: T) -> (int, List[Edge[T]]):
    return self.__state_exists(goal_state, self.heuristic_function)

  def state_exists_asearch(self, goal_state: T) -> (int, List[Edge[T]]):
    evaluation_function: Callable[[Edge[T]], int] = lambda edge: (
      self.heuristic_function(edge) + self.distance_function(edge)
    )

    return self.__state_exists(goal_state, evaluation_function)

  def __state_exists(self, goal_state: T, evaluation_function: Callable[[Edge[T]], int]):
    edge = Edge[T](
      id = -1,
      source = None,
      destination = self.__states_space.get_node(0),
      value = 0
    )

    path: List[Edge[T]] = []
    opened: PriorityQueue[T] = PriorityQueue[Edge[T]](
      init_elements=[edge],
      map_value=evaluation_function
    )

    closed: List[Edge[T]] = []

    while len(opened) != 0:
      most_promising_path: Edge[T] = opened.dequeue()
      path.append(most_promising_path)
      closed.append(most_promising_path)

      goal_is_found = most_promising_path.destination.value == goal_state
      if goal_is_found:
        closed.append(most_promising_path)
        return (True, path)

      for edge in most_promising_path.destination.adjacents:
        if edge not in closed and edge not in opened:
          opened.enqueue(edge)

    return (False, path)

  @property
  def states_space(self) -> Graph[T]:
    return self.__states_space

  @abstractmethod
  def heuristic_function(self, edge: Edge[T]) -> int:
    raise NotImplementedError

  def distance_function(self, edge: Edge[T]) -> int:
    return 0

  @abstractmethod
  def create_states_space(self) -> Graph[T]:
    raise NotImplementedError
