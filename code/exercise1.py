# WRITE YOUR CODE HERE
def find_key(dictionary, value):
  for key, dict_value in dictionary.items():
    if dict_value == value:
      return key
   

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : ['red', 'blue', 'green'],
    'Josh Jung' : (9, 10),
    3 : {0 : 0},
    9000 : 'impale mat a'
  }

  key = find_key(example_dict, (9, 10))
  print(key)

if __name__ == "__main__":
    example_dict = {
        1: ['red', 'blue', 'green'],
        'Josh Jung': (9, 10),
        3: {0: 0},
        9000: 'impale mat a'
    }

    key = find_key(example_dict, {0: 0})
    print(key)  
# test code below
if __name__ == "__main__":
  example_dict = {
    1 : ['red', 'blue', 'green'],
    'Josh Jung' : (9, 10),
    3 : {0 : 0},
    9000 : 'impale mat a'
  }

  key = find_key(example_dict, 'impale mat a')
  print(key)

