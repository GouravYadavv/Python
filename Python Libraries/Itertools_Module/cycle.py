# cycle is a function that cycles through a list endlessly. It is useful for creating infinite loops. Here is an example:

import itertools

data = ["Ram", "Shyam", "Hari", "Sita", "Gita"]

data1 = itertools.cycle(data)

# data1 contains the elements of the data list repeatedly that is it cycles through the list endlessly.

for _ in range(10):
    print(next(data1))

# When the end of the list is reached, it starts over at the beginning. This is useful for creating infinite loops.

# We can also use cycle() to cycle through a string:

data2 = itertools.cycle(("Python", "Java", "C++"))

for _ in range(10):
    print(next(data2))

# We have to use next keyword to print the elements of the list data2 as if we use print(data2) then it will print the object of the list data2. data2 is a generator object.
