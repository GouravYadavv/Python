# for copying a complete list to another list common method
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# using list comprehensions
my_list = [n for n in nums]
print(my_list)

# For squaring the nums list's elements and storing them into a new list
my_list = []
for n in nums:
    my_list.append(n * n)
print(my_list)

# Doing the same thing with the help of list comprehensions
my_list = [n * n for n in nums]
print(my_list)

# or another method is map which is as follows
my_list = list(map(lambda x: x * x, nums))
print(my_list)

# Let's print all even number of the list nums
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# Doing the same thing using filter function
my_list = list(filter(lambda n: n % 2 == 0, nums))
print(my_list)

# -----------------------------------Nested For Loop-----------------------------#
# We have a string "abcd"
# Expected output = [("a",0)("a",1)........("d",3)]

# Without list comprehension code:
my_list = []
for letter in "abcd":
    for number in range(4):
        my_list.append((letter, number))
print(my_list)

# Using List comprehension:
my_list = [(letter, number) for letter in "abcd" for number in range(4)]
print(my_list)
