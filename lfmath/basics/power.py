def power(x: int | float, y: int | float):
  z = 1
  for _ in range(y):
    z *= x
  return float(z)