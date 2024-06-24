def move_to_bottom(d, key):
  if key in d:
    value = d.pop(key)
    d[key] = value
    return d
  else:
    return "The key is not in the dictionary"

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  move_to_bottom(example_dict, 1)
  print(example_dict)


def move_to_bottom(d, key):
  if key in d:
    value = d.pop(key)
    new_dict = {k: v for k, v in d.items()}
    new_dict[key] = value
    return new_dict
  else:
    return "The key is not in the dictionary"

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  print(move_to_bottom(example_dict, 2))
def move_to_bottom(d, k):
  if k not in d:
    return 'The key is not in the dictionary'
  else:
    value = d.pop(k)
    d[k] = value
    return d
# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  print(move_to_bottom(example_dict, 4))