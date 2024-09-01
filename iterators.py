# Example 1:

# define a list
my_list = [6, 9, 0, 3]  # 4 elements

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

print(next(my_iter))       # Output: 6
print(next(my_iter))       # Output: 9

# next(obj) is same as obj.__next__()

print(my_iter.__next__())  # Output: 0
print(my_iter.__next__())  # Output: 3

# This will raise error, no items left
next(my_iter)