from abc import ABCMeta, abstractmethod
from typing import List, TypeVar

T = TypeVar('T')

class Structure(object, metaclass=ABCMeta):
  def __init__(self):
    self.__data: List[T] = []

  @property
  def data(self) -> List[T]:
    return self.__data

  def __contains__(self, element) -> bool:
    return element in self.queue

  def __len__(self) -> int:
    return len(self.queue)

  def is_empty(self) -> bool:
    print("self.data: ", self.data)
    return False if len(self.data) else True

  def add(self, element: T) -> None:
    self.data.append(element)
