import itertools

# count(start, step) is the same as range(start, inf, step)
# enumerate(iterable, start) is the same as zip(count(start), iterable)

data = [100, 200, 300, 400]
data_1 = list(zip(itertools.count(start=5, step=2), data))
data_2 = list((enumerate(data, 5)))
print(data_1)
print(data_2)

# Note: count() and enumerate() are infinite iterators, so they can be used in loops like while True or for i in count() or for i in enumerate() without worrying about them ending.
