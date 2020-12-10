import math
from ..data_structures.priority_queue import PriorityQueue 
from ..data_structures.graph.graph import Graph
from ..data_structures.graph.node import Node
from abc import abstractmethod, ABCMeta

"""
It can navigate intelligently through a states space graph.
"""
class Agent(object, metaclass=ABCMeta):
  def __init__(self):
    self.__states_space = Graph()
    self.__create_states_space()

  def state_exists(self, goal_state):
    opened = PriorityQueue(
      init_elements=[self.__states_space.get_node(0)],
      map_value=self.__heuristic_function
    )

    closed: List[Node] = []

    while len(opened) != 0:
      most_promising_node = opened.dequeue()
      closed.append(most_promising_node)

      goal_is_found = most_promising_node.value == goal_state
      if goal_is_found:
        closed.append(most_promising_node)
        return True

      for edge in most_promising_node.adjacents:
        adjacent_node = edge.destination
        if adjacent_node not in closed and adjacent_node not in opened:
          opened.enqueue(adjacent_node)

    return False

  @property
  def states_space(self):
    return self.__states_space

  @abstractmethod
  def __heuristic_function(self, node):
    raise NotImplementedError

  @abstractmethod
  def __create_states_space(self):
    raise NotImplementedError
