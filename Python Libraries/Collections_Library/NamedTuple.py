# It is like a hybrid between a dictionary and a tuple. In this case, you can access the values by their names instead of their indexes. It is a good way to make your code more readable and less error prone.

# First we have to import the module
from collections import NamedTuple


# Here we define the structure of the data we want to store
class Person(NamedTuple):
    name: str
    age: int
    country: str


person = Person("John", 36, "Norway")
