integer_hash_value = hash(749)
float_hash_value = hash(3.14)
string_hash_value = hash('hello world')
tuple_hash_value = hash(('blah', 42))

print(integer_hash_value)
print(float_hash_value)
print(string_hash_value)
print(tuple_hash_value)


class example:
  def __str__(self):
    return 'I am a user-defined object'

my_obj = example()
obj_hash_value = hash(my_obj)

print(my_obj)
print(obj_hash_value)
my_list = [1, 2, 3, 4]
my_dict = {my_list : 'value'}

print(my_dict)
dict_key = ('key', 'value')
my_dict = {dict_key : 'value'}

print(my_dict)
str_1 = 'Hello world!'
str_2 = 'Hello world!'

print(hash(str_1) == hash(str_2))