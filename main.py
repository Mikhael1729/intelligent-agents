from packages.data_structures import Graph, Queue, Stack
from letters_agent import LettersAgent
from colors_agent import ColorsAgent

agent = ColorsAgent()
agent.print_states_space()

exists = agent.state_exists_asearch(['Y', 'G', 'B', 'R', 'R'])


print("exists: ", exists[0])
print("path: ")

for path in exists[1]:
	print("  - ", path.destination)

