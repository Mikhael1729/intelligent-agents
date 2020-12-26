from packages.agent import Agent
from packages.data_structures import Graph, Edge
from typing import List, Tuple
from permutations import generate_permutations

class ColorsAgent(Agent):
  def heuristic_function(self, edge: Edge[List[str], Tuple[int, int]]):
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

    states_space = Graph[List[str]](allow_node_repetition=False)
    initial_state = states_space.add_node([""])
    depth = 3
    
    initial_state_candidate = None
    for colors_distribution in permutations:
      colors_distribution.append(colors_distribution[0])
      last_parent = None

      for i in range(0, depth):
        parent_action = (i, i + 1)
        parent_value = self.__transform_state(last_parent if last_parent else colors_distribution, parent_action)
        ancestor_action = (parent_action[0] + 1, parent_action[1] + 1)

        count = 0
        for j in range(0, depth):
          child_action = (j, j + 1)

          action_is_allowed = child_action != ancestor_action # If child_state will no be the same as its parent_state.
          if action_is_allowed:
            child_value = self.__transform_state(parent_value, child_action)
            parent_state = states_space.add_node(parent_value)
            child_state = states_space.add_node(child_value)

            connection_exists = child_state.connection_with_value_exists(child_action)

            if not connection_exists:
              connection = states_space.add_edge(parent_state, child_state, child_action)

              count += 1
              if count == depth:
                initial_state_candidate = parent_state

        # Connect parent node of each component of states space with the initial state.
        if initial_state_candidate:
          states_space.add_edge(initial_state, initial_state_candidate, (0, 0))
          initial_state_candidate = None

        last_parent = parent_value

    return states_space

  def __transform_state(self, state: List[str], action: Tuple[int, int]):
    transformed: List[str] = state.copy()

    i, j = action[0], action[1]
    transformed[i], transformed[j] = transformed[j], transformed[i]

    return transformed
