# zip_longest is a function that works like zip, except that it goes on until the longest iterable is exhausted, filling in None for missing values:

import itertools

data = ["Ram", "Shyam", "Hari", "Sita", "Gita"]

data1 = itertools.zip_longest(range(10), data)
print(list(data1))
# Here is a more complex example:

data2 = itertools.zip_longest(range(10), data, fillvalue="Missing")
print(list(data2))
# The fillvalue argument is optional, and defaults to None.

# The zip_longest() function is new in Python 3.1. In Python 2, it was called izip_longest() in the itertools module.
