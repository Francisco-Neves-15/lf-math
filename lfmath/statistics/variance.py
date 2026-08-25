from lfmath._helpers import helper_entry_multiple_numbers
from mean import mean

# x: list of values ​​– mm: mean of the values
def variance(*x: int | float):
  x = helper_entry_multiple_numbers(*x)

  _sum = 0
  mx = mean(x)

  for i in x:
    _sum += (i - mx) ** 2

  return _sum / len(x)
