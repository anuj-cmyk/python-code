# Creating a list, dictionary, and set
my_list = [1, 2, 3]
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_set = {1, 2, 3}

# Operations on the list ..............

# Adding an element to the list
my_list.append(4)
print("List after adding 4:", my_list)

# Removing an element from the list
my_list.remove(2)
print("List after removing 2:", my_list)

# Modifying an element in the list
my_list[1] = 5
print("List after modifying second element to 5:", my_list)

# Operations on the dictionary................

# Adding a new key-value pair
my_dict['d'] = 4
print("Dictionary after adding key 'd' with value 4:", my_dict)

# Removing a key-value pair
del my_dict['b']
print("Dictionary after removing key 'b':", my_dict)

# Modifying a value in the dictionary
my_dict['a'] = 10
print("Dictionary after modifying value of key 'a' to 10:", my_dict)

# Operations on the set..............

# Adding an element to the set
my_set.add(4)
print("Set after adding 4:", my_set)

# Removing an element from the set
my_set.remove(2)
print("Set after removing 2:", my_set)

# Adding a duplicate (won't change the set)
my_set.add(3)
print("Set after trying to add duplicate 3:", my_set)

# Final output after operations ...............
print("\nFinal List:", my_list)
print("Final Dictionary:", my_dict)
print("Final Set:", my_set)
