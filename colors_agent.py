from packages.agent import Agent
from packages.data_structures import Graph, Edge
from typing import List, Tuple
from permutations import permutations

class ColorsAgent(Agent):
  def heuristic_function(self, edge: Edge[List[str], Tuple[int, int]]):
    colors = edge.destination.value
    size = len(colors)

    differences = 4
    for i in range(0, size):
      for j in range(0, size - 1):
        if i != j and colors[i] != colors[j]:
          differences -= 1

      if colors[i] == colors[-1]:
        differences -= 1

    return differences

  def create_states_space(self):
    initial_state_value = ['B', 'G', 'Y', 'R', 'R°']
    colors_permutations = permutations(initial_state_value, self.__permutation)

    states_space = Graph[List[str]](allow_node_repetition=False)

    # Connect each permutation
    for i in range(0, len(colors_permutations) - 1):
      source_value = colors_permutations[i]
      destination_value = colors_permutations[i + 1]

      source = states_space.add_node(source_value[0])
      destination = states_space.add_node(destination_value[0])

      states_space.add_edge(source, destination, destination_value[1])

    # Add the rest of connections.
    edge: Edge[List[str], Tuple[int, int]]
    size = len(states_space.edges)

    for i in range(0, size):
      edge = states_space.edges[i]

      for j in range(0, len(initial_state_value) - 1):
        action = (j, j + 1)

        if edge.value != action:
          transformed_source_state = states_space.add_node(self.__transform_state(edge.source.value, action))

          # Disable source destination loop.
          there_is_loop = False

          for transformed_edge in transformed_source_state.adjacents:
            if transformed_edge.value == action:
              there_is_loop = True
              break

          if not there_is_loop:
            new_edge = states_space.add_edge(edge.source, transformed_source_state, action)

    return states_space

  def __transform_state(self, state: List[str], action: Tuple[int, int]):
    transformed: List[str] = state.copy()
    i, j = action[0], action[1]
    transformed[i], transformed[j] = transformed[j], transformed[i]

    return transformed

  def __permutation(self, permutation: List, i: int, j: int):
    return (permutation, (i, j))
