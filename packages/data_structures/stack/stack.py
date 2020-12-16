from ..structure import Structure, T

class Stack(Structure):
  def remove(self) -> T:
    if self.is_empty():
      return None

    return self.data.pop(-1)


