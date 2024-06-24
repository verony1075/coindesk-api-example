def is_nested(d):
  for v in d.values():
    if isinstance(v, (list, tuple, dict)):
      return True
  return False

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  print(is_nested(example_dict))


def is_nested(d):
  for v in d.values():
    if isinstance(v, (list, tuple, dict)):
      return True
  return False

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : (2, 3),
    4 : 'four',
    5 : 'five'
  }

  print(is_nested(example_dict))

def is_nested(d):
    for v in d.values():
        if isinstance(v, (list, tuple, dict)):
            return True
    return False

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : {3 : 4},
    5 : 'five'
  }

  print(is_nested(example_dict))