from graph import Graph
from agent import Agent
from letter import Letter

def test_bfs_and_dfs():
  graph = Graph()

  n1 = graph.add_node("m")
  n2 = graph.add_node("mi")
  n3 = graph.add_node("mik")

  graph.add_edge(n1.id, n2.id, "i")
  graph.add_edge(n2.id, n3.id, "k")


  there_is_path1 = graph.has_path_dfs(n1, n3)
  there_is_path2 = graph.has_path_bfs(n1, n3)

  print(f"there_is_path: {there_is_path1}")
  print(f"there_is_path: {there_is_path2}")

def test_best_first_search():
  states_space = Graph[Letter]()

  # Insert nodes
  s = states_space.add_node(Letter("S"))
  a = states_space.add_node(Letter("A"))
  b = states_space.add_node(Letter("B"))
  c = states_space.add_node(Letter("C"))
  d = states_space.add_node(Letter("D"))
  e = states_space.add_node(Letter("E"))
  f = states_space.add_node(Letter("F"))
  g = states_space.add_node(Letter("G"))
  h = states_space.add_node(Letter("H"))
  i = states_space.add_node(Letter("I"))
  j = states_space.add_node(Letter("J"))
  k = states_space.add_node(Letter("K"))
  l = states_space.add_node(Letter("L"))

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

  agent = Agent(states_space)
  there_is_path = agent.state_exists(Letter('E'))

  print(f"there_is_path: {there_is_path}")

test_best_first_search()

"""
The heuristic function handling using OOP:

- Type    Override: ==
- Node	  Override: < and >
- Queue   Uses: 
- Graph
- Agent
"""


