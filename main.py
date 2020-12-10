from graph import Graph
from letters_agent import LettersAgent

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
  agent = LettersAgent()
  there_is_path = agent.state_exists('E')

  print(f"there_is_path: {there_is_path}")

test_best_first_search()
