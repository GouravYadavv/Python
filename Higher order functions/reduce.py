# Python's reduce() is a function that implements a mathematical technique called folding or reduction. reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value.

# Reduce is a method of the library funtools, so we have to import a library for this.
import functools


# Let's take a list (L):


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = functools.reduce(lambda x, y: x + y, L)
print(a)

# For maximum value:
b = functools.reduce(lambda x, y: x if x > y else y, L)
print(b)

# This can also be done using numpy as:
import numpy as np

print(np.sum(L))
