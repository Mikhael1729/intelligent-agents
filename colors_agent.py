from packages.agent import Agent
from packages.data_structures import Graph, Edge
from typing import List, Tuple
from permutations import generate_permutations

class ColorsAgent(Agent):
  def heuristic_function(self, edge: Edge[List[str]]):
    node = edge.destination
    colors = node.value
    size = len(colors)

    differences = 4
    for i in range(0, size):
      for j in range(0, size - 1):
        if colors[i] != colors[j]:
          differences -= 1

      if colors[i] == colors[-1]:
        differences -= 1

    return differences

  def create_states_space(self):
    colors = ['R', 'B', 'G', 'Y']
    permutations = generate_permutations(colors)

    states_space = Graph[List[str]]()
    for colors_distribution in permutations:
      colors_distribution.append(colors_distribution[0])

      last_parent = None
      for i in range(0, 3):
        parent_action = (0 + i, 1 + i)
        parent_value = self.__transform_state(last_parent if last_parent else colors_distribution, parent_action)
        parent_state = states_space.add_node(parent_value)

        ancestor_action = (parent_action[0] + 1, parent_action[1] + 1)

        for j in range(0, 3):
          child_action = (j, j + 1)

          action_is_allowed = child_action != ancestor_action
          if action_is_allowed:
            child_value = self.__transform_state(parent_value, child_action)
            child_state = states_space.add_node(child_value)

            connection = states_space.add_edge(parent_state, child_state, child_action)

        last_parent = parent_value

    return states_space


  def __transform_state(self, state: List[str], action: Tuple[int, int]):
    transformed: List[str] = state.copy()

    i, j = action[0], action[1]
    transformed[i], transformed[j] = transformed[j], transformed[i]

    return transformed

