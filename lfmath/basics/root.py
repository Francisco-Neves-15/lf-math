import math
import abs

# Root using: num ^ ( 1 / rad )
def root(x, rad):

  if not isinstance(x, (int, float)):
    raise TypeError("x must be numeric")

  if not isinstance(rad, int):
    raise TypeError("rad must be integer")

  if rad == 0:
    raise ValueError("rad cannot be zero")

  if not math.isfinite(x):
    raise ValueError("x must be finite")

  if x == 0 and rad < 0:
    raise ZeroDivisionError("0 cannot have negative root")

  if rad < 0:
    return 1 / root(x, -rad)

  if x < 0 and rad % 2 == 0:
    return complex(0, (-x)**(1/rad))

  if x < 0:
    return -((-x)**(1/rad))

  return x ** (1/rad)

# Newtown formula to square root
def sqrt_newton(x, epsilon=1e-10, max_iter=1000):

  if not isinstance(x, (int, float)):
    raise TypeError("x must be numeric")

  if not math.isfinite(x):
    raise ValueError("x must be finite")

  if x < 0:
    raise ValueError("sqrt_newton only supports real numbers")

  if epsilon <= 0:
    raise ValueError("epsilon must be positive")

  if x == 0:
    return 0

  y = x if x >= 1 else 1

  for _ in range(max_iter):

    if abs.abs(y*y - x) <= epsilon:
      return y

    y = (y + x/y) / 2

  raise RuntimeError("Newton method did not converge")

# Simple use to square root
def sqrt(x: int | float):
  return root(x , 2)
