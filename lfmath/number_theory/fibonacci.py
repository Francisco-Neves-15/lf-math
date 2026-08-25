from typing import Literal

def fibonacci(
  x: int,
  return_type: Literal["result"] | Literal["sequence"] | Literal["both"] = "result"
):
  """
  x:
    Fibonacci sequence index.

  return_type:
    "result"   -> return the requested value.
    "sequence" -> return the Fibonacci sequence up to x.
    "both"     -> return both the requested value and the sequence in tuple (result, sequence).
  """

  if x < 0:
    raise ValueError("Fibonacci index cannot be negative.")

  if return_type not in ("result", "sequence", "both"):
    raise ValueError(
      'return_type must be "result", "sequence", or "both".'
    )

  a, b = 0, 1
  sequence = []

  for _ in range(x + 1):
    sequence.append(a)
    a, b = b, a + b

  result = sequence[x]

  if return_type == "both":
    return result, tuple(sequence)

  if return_type == "sequence":
    return tuple(sequence)

  return result

print(fibonacci(11))
print(fibonacci(11, return_type="result"))
print(fibonacci(11, return_type="sequence"))
print(fibonacci(11, return_type="both"))
