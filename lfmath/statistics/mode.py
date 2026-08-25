from lfmath._helpers import helper_entry_multiple_numbers

def mode(*x: int | float | str):
  x = helper_entry_multiple_numbers(*x)
  info = {}

  for y in x:
    if y in info:
      info[y] += 1
    else:
      info[y] = 1

  freq = max(info.values())

  if freq == 1:
    return False

  modes = tuple(y for y in info if info[y] == freq)

  if len(modes) == 1:
    return modes[0]

  return modes

# Classification by number of modes
# - Amodal: The set has no mode (no value repeats).
# - Unimodal: The set has only one mode.
# - Bimodal: The set has two modes.
# - Multimodal: The set has three or more modes.
