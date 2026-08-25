from lfmath._helpers import helper_entry_multiple_numbers

def mean(*x: int | float):
  x = helper_entry_multiple_numbers(*x)
  return sum(x) / len(x)