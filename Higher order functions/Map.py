# Map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.).


# For example, we have a list (L) and we want to perform square of all the items of that list so we will do it as:

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(
    list(map(lambda x: x**2, L))
)  # We have to convert type from map object to list.

# Let's take another example of map.

# Let's take a dictonary by the name students and store some keys and values into it.

students = [
    {"name": "Ram", "Address": "Haryana"},
    {"name": "Sham", "Address": "Delhi"},
    {"name": "John", "Address": "USA"},
]

# So here we have a dictonary of the students and we want to extract the names of all the students with the help of map fucntion:

print(list(map(lambda students: students["name"], students)))
