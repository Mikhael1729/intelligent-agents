from packages.data_structures import Graph, Queue, Stack
from letters_agent import LettersAgent
from colors_agent import ColorsAgent

agent = ColorsAgent()
exists = agent.state_exists_asearch(['R', 'B', 'G', 'Y', 'R°'])

# Print the path in console.
print("exists: ", exists[0])
print("path: ")

for path in exists[1]:
 print("  - ", path.destination.value)

# Show an image of the generated graph and the path taken.
agent.print_states_space()
