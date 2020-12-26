from packages.data_structures import Graph, Queue, Stack
from letters_agent import LettersAgent
from colors_agent import ColorsAgent

agent = ColorsAgent()
exists = agent.state_exists_asearch(['R', 'B', 'G', 'Y', 'R'])

agent.print_states_space()



print("exists: ", exists[0])
print("path: ")

for path in exists[1]:
	print("  - ", path.destination)

