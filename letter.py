class Letter:
  def __init__(self, letter):
    self.letter = letter

  def __str__(self):
    return f"{self.letter} | {self.goal_difference}"

  def __eq__(self, other):
    if isinstance(other, Letter):
      return self.letter == other.letter

    return False

  def __gt__(self, other):
    if isinstance(other, Letter):
      return self.goal_difference > other.goal_difference

    return False

  def __lt__(self, other):
    if isinstance(other, Letter):
      return self.goal_difference < other.goal_difference

    return False

  """
  Heuristic function. It returns the stimated value of how much
  takes to go from given letter to the goal (E)
  """
  @property
  def goal_difference(self):
    if self.letter == "S":
      return 10
    elif self.letter == "A":
      return 9
    elif self.letter == "B":
      return 7
    elif self.letter == "C":
      return 8
    elif self.letter == "D":
      return 8
    elif self.letter == "E":
      return 0 
    elif self.letter == "F":
      return 6
    elif self.letter == "G":
      return 3
    elif self.letter == "H":
      return 6
    elif self.letter == "I":
      return 4
    elif self.letter == "J":
      return 4
    elif self.letter == "K":
      return 3
    elif self.letter == "L":
      return 4

    raise ValueError(f"Given node with value {self.letter} is not a valid one")
