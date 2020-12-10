from packages.agent import Agent

class LettersAgent(Agent):
  def __init__(self):
    super().__init__()

  def _Agent__heuristic_function(self, node):
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


  def _Agent__create_states_space(self):
    # Insert nodes
    s = self.states_space.add_node("S")
    a = self.states_space.add_node("A")
    b = self.states_space.add_node("B")
    c = self.states_space.add_node("C")
    d = self.states_space.add_node("D")
    e = self.states_space.add_node("E")
    f = self.states_space.add_node("F")
    g = self.states_space.add_node("G")
    h = self.states_space.add_node("H")
    i = self.states_space.add_node("I")
    j = self.states_space.add_node("J")
    k = self.states_space.add_node("K")
    l = self.states_space.add_node("L")

    # Connect them
    self.states_space.add_edge(s, a, 7)
    self.states_space.add_edge(s, b, 2)
    self.states_space.add_edge(s, c, 3)

    self.states_space.add_edge(a, d, 4)
    self.states_space.add_edge(a, b, 3)
    self.states_space.add_edge(d, f, 5)

    self.states_space.add_edge(b, d, 4)
    self.states_space.add_edge(b, h, 1)
    self.states_space.add_edge(h, f, 3)
    self.states_space.add_edge(h, g, 2)
    self.states_space.add_edge(g, e, 2)

    self.states_space.add_edge(c, l, 2)
    self.states_space.add_edge(l, i, 4)
    self.states_space.add_edge(l, j, 4)
    self.states_space.add_edge(i, k, 4)
    self.states_space.add_edge(j, k, 4)
    self.states_space.add_edge(k, e, 5)
