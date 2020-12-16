from packages.agent import Agent
from packages.data_structures import Graph
from typing import List
from permutations import generate_permutations

class ColorsAgent(Agent):
  def heuristic_function(self, node):
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
    colors = ['red', 'blue', 'green', 'yellow']
    permutations = generate_permutations(colors)

    # Generate states
    states_space = Graph[List[str]]()
    for perm in permutations:
      nodes = []
  
      current_state = [None] * 4
      for i in range(0, len(perm)):
        color = perm[i]
        current_state[i] = color
        new_state = current_state.copy()
        nodes.append(states_space.add_node(new_state))
  
      nodes[-1].value[-1] = nodes[0].value[0]
  
      # Generate connections
      for i in range(1, len(perm)):
        states_space.add_edge(nodes[i-1], nodes[i], perm[i])

    return states_space
