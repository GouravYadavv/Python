# Filter() is a built-in function in Python. The filter function can be applied to an iterable such as a list or a dictionary and create a new iterator. This new iterator can filter out certain specific elements based on the condition that you provide very efficiently.

# Let's take a list (L) and filter some items of it.
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]

print(list(filter(lambda x: 9 >= x >= 2, L)))
# In filter also just like map we have to convert filter object into list.

"""
    Let's take another example of filter function.
    Let's take list consists of fruits name and we will filter the list by returning the name of only those fruits which are having letter "e" in there name.
"""
Fruits = ["Apple", "Bananna", "Mango", "Grapes", "Orange"]

print(list(filter(lambda x: "e" in x, Fruits)))
