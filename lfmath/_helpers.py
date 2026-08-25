def helper_entry_multiple_numbers(*x: int | float):
  if len(x) == 1 and isinstance(x[0], (list, tuple)):
    x = x[0]
  return x