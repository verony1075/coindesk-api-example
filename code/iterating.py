print(dir({}))
hero = {
  'name' : 'Moira',
  'role' : 'support',
  'health' : 200
}

for item in hero:
  print(item)

hero = {
  'name' : 'Moira',
  'role' : 'support',
  'health' : 200
}

for key in hero:
  print(f'Key: {key}, Value: {hero[key]}')

hero = {
  'name' : 'Moira',
  'role' : 'support',
  'health' : 200
}

for key in hero:
  print(f'Key: {key}, Value: {hero['key']}')