from lfmath._helpers import helper_entry_multiple_numbers

def median(*x: int | float):
  x = helper_entry_multiple_numbers(*x)
  x = sorted(x)

  if len(x) % 2 != 0:
    return x[len(x) // 2]
  else:
    return (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
