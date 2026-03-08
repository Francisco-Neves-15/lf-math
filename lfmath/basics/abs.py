def abs(x):
  if not isinstance(x, (int, float)):
    raise TypeError("x must be numeric")

  if x < 0:
    return float(-x)
  else:
    return float(x)
