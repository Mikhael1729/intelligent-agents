from packages.agent import Agent
from packages.data_structures import Graph

class LettersAgent(Agent):
  def __init__(self):
    super().__init__()

  def heuristic_function(self, node):
    value = node.value

    if value == "S":
      return 10
    elif value == "A":
      return 9
    elif value == "B":
      return 7
    elif value == "C":
      return 8
    elif value == "D":
      return 8
    elif value == "E":
      return 0 
    elif value == "F":
      return 6
    elif value == "G":
      return 3
    elif value == "H":
      return 6
    elif value == "I":
      return 4
    elif value == "J":
      return 4
    elif value == "K":
      return 3
    elif value == "L":
      return 4

    raise ValueError(f"Given node with value {self.letter} is not a valid one")


  def create_states_space(self):
    states_space = Graph()

    # Insert nodes
    s = states_space.add_node("S")
    a = states_space.add_node("A")
    b = states_space.add_node("B")
    c = states_space.add_node("C")
    d = states_space.add_node("D")
    e = states_space.add_node("E")
    f = states_space.add_node("F")
    g = states_space.add_node("G")
    h = states_space.add_node("H")
    i = states_space.add_node("I")
    j = states_space.add_node("J")
    k = states_space.add_node("K")
    l = states_space.add_node("L")

    # Connect them
    states_space.add_edge(s, a, 7)
    states_space.add_edge(s, b, 2)
    states_space.add_edge(s, c, 3)

    states_space.add_edge(a, d, 4)
    states_space.add_edge(a, b, 3)
    states_space.add_edge(d, f, 5)

    states_space.add_edge(b, d, 4)
    states_space.add_edge(b, h, 1)
    states_space.add_edge(h, f, 3)
    states_space.add_edge(h, g, 2)
    states_space.add_edge(g, e, 2)

    states_space.add_edge(c, l, 2)
    states_space.add_edge(l, i, 4)
    states_space.add_edge(l, j, 4)
    states_space.add_edge(i, k, 4)
    states_space.add_edge(j, k, 4)
    states_space.add_edge(k, e, 5)

    return states_space
