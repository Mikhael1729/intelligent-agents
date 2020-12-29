from packages.agent import Agent, Action
from packages.data_structures import Graph, Edge
from typing import List, Tuple, Dict
from permutations import permutations

EdgeType = Edge[List[str], Tuple[int, int]]

class ColorsAgent(Agent):
  def heuristic_function(self, edge: EdgeType):
    colors = edge.destination.value
    size = len(colors)

    i = 0
    for color in colors:
      if color == 'R':
        break
      i += 1

    if colors[-1] == 'R':
      return i

    for j in range(i + 1, size):
      color = colors[j]
      if color == 'R':
        distance_to_last = (size - 1) - j
        return distance_to_last + i

    return 0

  def distance_function(self, edge: EdgeType, distance: int):
    return distance

  def create_states_space(self):
    initial_state_value = ['B', 'G', 'Y', 'R', 'R']
    colors_permutations = permutations(initial_state_value, self.__permutation)
    states_space = Graph[List[str]](allow_node_repetition=False, allow_edge_duplicates=False, allow_self_loops=False)

    # Connect each permutation
    for i in range(0, len(colors_permutations) - 1):
      source = states_space.add_node(colors_permutations[i][0])
      destination = states_space.add_node(colors_permutations[i + 1][0])
      states_space.add_edge(source, destination, colors_permutations[i + 1][1])

    # Add the rest of connections.
    edge: Edge[List[str], Tuple[int, int]]
    size = len(states_space.edges)

    for i in range(0, size):
      edge = states_space.edges[i]

      for j in range(0, len(initial_state_value) - 1):
        action = (j, j + 1)

        if edge.value != action:
          transformed_source_state = states_space.add_node(self.__transform_state(edge.source.value, action))
          new_edge = states_space.add_edge(edge.source, transformed_source_state, action)

    return states_space

  def __transform_state(self, state: List[str], action: Tuple[int, int]):
    transformed: List[str] = state.copy()
    i, j = action[0], action[1]
    transformed[i], transformed[j] = transformed[j], transformed[i]

    return transformed

  def __permutation(self, permutation: List, i: int, j: int):
    return (permutation, (i, j))
