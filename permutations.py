def generate_permutations(elements):
  if len(elements) <= 1:
    yield elements
  else:
    for perm in generate_permutations(elements[1:]):
      for i in range(len(elements)):
        yield perm[:i] + elements[0:1] + perm[i:]
