from packages.data_structures import Graph
from letters_agent import LettersAgent

def test_best_first_search():
  agent = LettersAgent()
  there_is_path = agent.state_exists('E')

  print(f"there_is_path: {there_is_path}")

test_best_first_search()
