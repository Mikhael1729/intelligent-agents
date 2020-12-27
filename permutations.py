from typing import List, TypeVar
T = TypeVar('T')

def _permute(elements: List[T], i: int):
  """
  Heaps algorithm to compute a list elements with n elements
  """
  if i == 1:
    yield elements
  else:
    for j in range(i - 1):
      for permutation in _permute(elements, i - 1):
        yield permutation

      k = 0 if i % 2 == 1 else j

      elements[k], elements[i - 1] = elements[i - 1], elements[k]

    for permutation in _permute(elements, i - 1):
      yield permutation

def permutations(elements):
  """
  Compute all distinct permutations of elements list using the
  Heap's algorithm.
  """
  return _permute(elements, len(elements))
