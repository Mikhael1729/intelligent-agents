from packages.data_structures import Graph, Queue, Stack
from examples.letters_agent import LettersAgent
from examples.colors_agent import ColorsAgent

agent = ColorsAgent()
exists = agent.state_exists_asearch(['R', 'B', 'G', 'Y', 'R'])

# Print the path in console.
print("exists: ", exists)
print("path: ")

for key, value in agent.solution.items():
  print(value)

# Show an image of the generated graph and the path taken.
agent.print_states_space()

"""
agent = LettersAgent()
agent.state_exists_asearch('E')

agent.print_states_space()
"""
