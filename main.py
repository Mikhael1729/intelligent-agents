from packages.data_structures import Graph, Queue, Stack
from letters_agent import LettersAgent
from colors_agent import ColorsAgent

agent = ColorsAgent()
exists = agent.state_exists_asearch(['red', 'blue', 'green', 'yellow', 'red'])

print("exists: ", exists[0])
print("path: ")

for path in exists[1]:
	print("  - ", path.destination)

