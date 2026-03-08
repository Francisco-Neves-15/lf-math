import math

def power(x, y):
  z = 1
  for _ in range(y):
    z *= x
  return float(z)
