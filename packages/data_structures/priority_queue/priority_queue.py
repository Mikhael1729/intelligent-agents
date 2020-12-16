from typing import TypeVar, Generic, Callable, Any, List

T = TypeVar('T')

class PriorityQueue(Generic[T]):
  def __init__(
    self, 
    init_elements: List[T]=None,
    ascending: bool=True,
    map_value: Callable[[T], Any]=None
  ):
    self.queue = init_elements if init_elements else []
    self.__ascending = ascending
    self.__heuristic_function = map_value

  def __str__(self) -> str:
    separator = ', '
    elements_in_string_list = [str(element) for element in self.queue]

    return f"[{separator.join(elements_in_string_list)}]"

  def __contains__(self, element) -> bool:
    return element in self.queue

  def __len__(self) -> int:
    return len(self.queue)

  @property
  def ascending(self) -> bool:
    return self.__ascending

  def enqueue(self, element) -> T:
    self.queue.append(element)

  def dequeue(self) -> T:
    try:
      highest_priority = 0 # The element with the greatest value in ascending order or viceversa.

      for i in range(0, len(self.queue)):
        if not self.__heuristic_function:
          current_value = self.queue[i]
          highest_priority_value = self.queue[highest_priority]
        else:
          current_value = self.__heuristic_function(self.queue[i])
          highest_priority_value = self.__heuristic_function(self.queue[highest_priority])

        if self.ascending:
          if current_value < highest_priority_value:
            highest_priority = i
        else:
          if current_value > highest_priority_value:
            highest_priority = i

      return self.queue.pop(highest_priority)
    except IndexError:
      print()
      exit()
