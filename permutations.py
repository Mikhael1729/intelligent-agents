from typing import List, TypeVar
T = TypeVar('T')

def _permute_generetably(elements: List[T], i: int):
  """
  Heaps algorithm to compute a list elements with n elements
  """
  if i == 1:
    yield elements
  else:
    for j in range(i - 1):
      for permutation in _permute_generetably(elements, i - 1):
        yield permutation

      k = 0 if i % 2 == 1 else j

      elements[k], elements[i - 1] = elements[i - 1], elements[k]

    for permutation in _permute_generetably(elements, i - 1):
      yield permutation

def _permute_iterably(elements: List[T], permutations: List[T], i: int):
  if i == 1:
    permutations.append(elements.copy())
    return

  _permute_iterably(elements, permutations, i - 1)

  for j in range(i - 1):
    k = 0 if i % 2 == 1 else j
    elements[k], elements[i - 1] = elements[i - 1], elements[k]

    _permute_iterably(elements, permutations, i - 1)

def permutations(elements):
  """
  Compute all distinct permutations of elements list using the
  Heap's algorithm.
  """
  permutations = []
  _permute_iterably(elements, permutations, len(elements))
  return permutations

def generate_permutations(elements):
  return _permute_generetably(elements, len(elements))
