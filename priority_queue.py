class PriorityQueue:
  def __init__(self, init_elements=None, ascending=True):
    self.queue = init_elements if init_elements else []
    self.__ascending = ascending

  def __str__(self):
    separator = ', '
    elements_in_string_list = [str(element) for element in self.queue]

    return f"[{separator.join(elements_in_string_list)}]"

  def __contains__(self, element):
    return element in self.queue

  def __len__(self):
    return len(self.queue)

  @property
  def ascending(self):
    return self.__ascending

  def enqueue(self, element):
    self.queue.append(element)

  """
  This is the heuristic function
  """
  def dequeue(self):
    try:
      highest_priority = 0 # The element with the greatest value in ascending order or viceversa.

      for i in range(0, len(self.queue)):
        if self.ascending:
          if self.queue[i] < self.queue[highest_priority]:
            highest_priority = i
        else:
          if self.queue[i] > self.queue[highest_priority]:
            highest_priority = i

      return self.queue.pop(highest_priority)
    except IndexError:
      print()
      exit()
