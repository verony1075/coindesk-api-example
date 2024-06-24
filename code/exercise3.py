def swap(d):
  try:
    return {v: k for k, v in d.items()}
  except TypeError:
    return "Cannot swap the keys and values for this dictionary"

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  swapped = swap(example_dict)
  print(swapped)

def swap(d):
  try:
    return {v: k for k, v in d.items()}
  except TypeError:
    return "Cannot swap the keys and values for this dictionary"

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : [2, 3],
    4 : 'four',
    5 : 'five'
  }

  swapped = swap(example_dict)
  print(swapped)
def swap(d):
  try:
    return {v: k for k, v in d.items()}
  except TypeError:
    return "Cannot swap the keys and values for this dictionary"

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : {3 : 4},
    5 : 'five'
  }

  swapped = swap(example_dict)
  print(swapped)

def swap(d):
  try:
    return {v: k for k, v in d.items()}
  except TypeError:
    return "Cannot swap the keys and values for this dictionary"

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : (4, 5)
  }

  swapped = swap(example_dict)
  print(swapped)