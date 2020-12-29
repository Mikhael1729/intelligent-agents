from typing import List, TypeVar, Tuple, Callable

T = TypeVar('T')
Transform = Callable[[List, int, int], any]

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

def _permute_iterably2(
    elements: List,
    permutations: List,
    i: int,
    actions: Tuple[int, int],
    transform: Transform = None
):
  if i == 1:
    new_permutation = elements.copy()
    if transform:
      new_permutation = transform(new_permutation, actions[0], actions[1])

    permutations.append(new_permutation)
    return

  _permute_iterably2(elements, permutations, i - 1, actions, transform)

  for j in range(i - 1):
    k = 0 if i % 2 == 1 else j
    elements[k], elements[i - 1] = elements[i - 1], elements[k]

    actions[0] = k
    actions[1] = i - 1

    _permute_iterably2(elements, permutations, i - 1, actions, transform)

def permutations(elements, transform: Transform = None):
  """
  Compute all distinct permutations of elements list using the
  Heap's algorithm.
  """
  permutations = []
  size = len(elements)
  actions = [-1, -1]

  _permute_iterably2(elements, permutations, size, actions, transform)
  return permutations

def generate_permutations(elements):
  return _permute_generetably(elements, len(elements))
