class Edge:
  """
  value: Symbol of the transition
  source: Node source
  destination Node destination
  """
  def __init__(self, id, source, destination, value=None):
    self.id = id
    self.source = source
    self.destination = destination
    self.value = value

  def __str__(self):
    return f"Edge(id: {self.id}, value: {self.value}, source: {self.source}, destination: {self.destination})"

