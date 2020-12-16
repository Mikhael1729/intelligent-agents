from packages.data_structures import Graph, Queue, Stack
from letters_agent import LettersAgent
from colors_agent import ColorsAgent

agent = LettersAgent()
exists = agent.state_exists_asearch('E')

print("exists: ", exists[0])
print("path: ")

for node in exists[1]:
	print("  - ", node)

