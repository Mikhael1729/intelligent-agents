import math
from priority_queue import PriorityQueue
from graph import Graph

class Agent:
  """
  Handles the given states space.

  states_space is an array of Graph.
  """
  def __init__(self, states_space):
    self.__states_space: Graph = states_space

  @property
  def states_space(self):
    return self.__states_space

  def state_exists(self, goal_state):
    opened = PriorityQueue([self.__states_space.get_node(0)], ascending=True)
    closed = []

    while len(opened) != 0:
      most_promising_node = opened.dequeue()
      closed.append(most_promising_node)

      most_promising_node_is_goal = most_promising_node.value == goal_state
      if most_promising_node_is_goal:
        closed.append(most_promising_node)
        return True

      for edge in most_promising_node.adjacents:
        adjacent_node = edge.destination
        if adjacent_node not in closed and adjacent_node not in opened:
          opened.enqueue(adjacent_node)

    return False
