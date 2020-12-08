from graph import Graph

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
  graph = Graph()

  # Insert nodes
  s = graph.add_node("S")
  a = graph.add_node("A")
  b = graph.add_node("B")
  c = graph.add_node("C")
  d = graph.add_node("D")
  e = graph.add_node("E")
  f = graph.add_node("F")
  g = graph.add_node("G")
  h = graph.add_node("H")
  i = graph.add_node("I")
  j = graph.add_node("J")
  k = graph.add_node("K")
  l = graph.add_node("L")

  # Connect them
  graph.add_edge(s, a, 7)
  graph.add_edge(s, b, 2)
  graph.add_edge(s, c, 3)

  graph.add_edge(a, d, 4)
  graph.add_edge(a, b, 3)
  graph.add_edge(d, f, 5)

  graph.add_edge(b, d, 4)
  graph.add_edge(b, h, 1)
  graph.add_edge(h, f, 3)
  graph.add_edge(h, g, 2)
  graph.add_edge(g, e, 2)

  graph.add_edge(c, l, 2)
  graph.add_edge(l, i, 4)
  graph.add_edge(l, j, 4)
  graph.add_edge(i, k, 4)
  graph.add_edge(j, k, 4)
  graph.add_edge(k, e, 5)

  # there_is_path = graph.has_path_best_first_search(s, e)
  # print(f"there_is_path: {there_is_path}")
