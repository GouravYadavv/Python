# Let's first make a dictionary by the name "City_map" and then we will be adding the cities of particular country as their values.

# So here we have 2 ways to initialize a dictionary.

City_map = {}

CityMap = dict()

# You can choose either way you want to...

# Now let's add some countries name to the dictionary and add some famous cities of those country as their values.

Cities_of_India = ["Delhi", "Gurugram", "Rewari"]

Cities_of_Pakistan = ["Islamabad", "Karachi", "Lahore"]

Cities_of_USA = ["New York City", "Austin", "Seattle"]

# Above are some lists of cities of different countries.

CityMap["India"] = []
CityMap["Pakistan"] = []
CityMap["USA"] = []

# Now above we have to initialize each country's key in the hashmap before assigning values to it, and it is much time consuming every time especially when we have to deal with a large data, so to deal with this situation we a special type of dictionary known as defaultdict.

from collections import defaultdict  # Here we have imported our special dictionary.

# Now we can directly add cities into the keys of their country names.

CityMap["India"] += Cities_of_India
CityMap["Pakistan"] += Cities_of_Pakistan
CityMap["USA"] += Cities_of_USA

print(CityMap)
print(CityMap.keys())
print(CityMap.values())
print(CityMap.items())
# So here we are all set to use our Hashmap.
