dictionary ={'one' : 'two', 'three' : 'one', 'two' : 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
  v = dictionary[v]

print(v)

"""
k = 0
v = dictionary[two] -> three

k = 1
v = dictionary[three] -> one

k = 2
v = dictionary[one] -> two
"""
