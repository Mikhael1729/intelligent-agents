from abc import abstractmethod

class Graph:
  def __init__(self):
    self.property1 = 1
    self.property2 = 2

  @abstractmethod
  def override(self):
    raise NotImplementedError("Method hasn't been overriden")

class IncGraph(Graph):
  def override(self):
    return "overritten"



