import math
from priority_queue import PriorityQueue
from graph import Graph
from node import Node

"""
It can navigate intelligently through a states space graph.
"""
class Agent:
  def __init__(self, states_space):
    self.__states_space: Graph = states_space

  @property
  def states_space(self):
    return self.__states_space

  def state_exists(self, goal_state):
    opened = PriorityQueue([self.__states_space.get_node(0)], ascending=True)
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
