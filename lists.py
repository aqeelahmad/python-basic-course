"""Working with lists

Some quick Facts about Python Lists
List index starts at 0
You can access indexes from the end by adding a negative sign, e.g. -1 index
gives you second last element of the list. 
"""

my_list = [1, 2, 3, 4, 5]


# Slicing
# Syntex list[start:end]
# We use : to slice a list, by supplying no value after the colon, we tell Python
# to take the slice till end of the list.

# Example 1: Getting index 2 to end of the list

print(my_list[2:])
# Output: [3, 4, 5]


# Example 2: Getting everything until the 3rd index
# We just need to leave the starting part empty and have 3 in the ending part

print(my_list[:3])
# Output: [1, 2, 3]

# Example 3: Get all elements until second last element

print(my_list[:-1])
# Output: [1, 2, 3, 4]


# One note that a slice creates a complete new list with no references
# to the original list. Which means if you store slice in a variable
# and modify it, the original list will stay as it is.
