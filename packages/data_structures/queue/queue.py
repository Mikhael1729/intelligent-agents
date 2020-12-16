from ..structure import Structure, T

class Queue(Structure):
  def remove(self) -> T:
    if self.is_empty():
      return None

    return self.data.pop(0)

