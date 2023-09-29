# this is a list - an array of anything
array_variable = [“5”, 6, int_variable]

# a list can be empty
array_empty = []

# this is how you add an element to list
array_empty.append(5)
print(array_empty)

# this is how you get a length of a list
print(len(array_variable))

# access element
print(array_variable[1])

# this is a dictionary - a unordered collection of data, where each piece of data 
# is stored as a key-value pair. Keys are unique and used to access their 
# associated values. Think of a 
# dictionary like a real-world dictionary: you look up a word (the key), and you find its
# definition (the value).
dictionary = {“key0”: 1, 8: “something”, “array_key”: [1, 2, 3]}
print(dictionary)

# this is how you get an element from a dictionary
element = dictionary[“array_key”]
print(element)

# this is how you assign a new element to the dictionary
dictionary[“some_new_key”] = 0.5
print(dictionary)

# this is a set - a unordered collection of data, where each piece of data 
# is unique
some_new_set = {2, 3, 1}
print(some_new_set)

# adding to set
some_new_set.add(2)
print(some_new_set)

# removing from set
some_new_set.remove(3)
print(some_new_set)

# finding common elements of 2 sets (intersection)
print(set([1, 2, 0]) & set([2, 3, 4]))

# finding a union of 2 sets
print(set([1, 2, 0]) | set([2, 3, 4]))

# finding elements which are present in one set, but not in another
print(set([1, 2, 0]) - set([2, 3, 4]))


