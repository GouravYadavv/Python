# Then we have another way to repeat the elements in a list, which is to use the itertools module. The itertools module contains a function called repeat() that does exactly what we want. Here is an example:

import itertools

data = itertools.repeat("Ram", 100)

for _ in range(10):
    print(next(data))

squares = map(
    pow, range(10), itertools.repeat(2)
)  # This can also be written as [2]* 10
print(list(squares))

# Here we have used the repeat() function to repeat the string "Ram" 100 times. Then we have used the map() function to calculate the squares of the numbers from 0 to 9. The map() function takes two arguments. The first argument is the function that we want to apply to the elements of the list. The second argument is the list of elements. The map() function applies the function to each element of the list and returns a map object. We have converted the map object to a list using the list() function. The map object contains the squares of the numbers from 0 to 9.

# The repeat() function can also be used to repeat the elements of a list. Here is an example:

import itertools

data = itertools.repeat([1, 2, 3], 3)

for _ in range(3):
    print(next(data))

# mapstar is a function that takes a function and a list as arguments and returns the result of applying the function to each element of the list. Here is an example:

import itertools

squares = itertools.starmap(
    pow,
    [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2)],
)

print(list(squares))
