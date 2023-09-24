# For reading a file, displaying content written in a file we use read function.

# Same procedure will be followed as we have followed for creating the file, that is open file, work on it and close file.

f = open("ram.txt", "r")
s = f.read()
# print(s)
f.close()

# For reading a file line wise.

f = open("ram.txt", "r")
s = f.readline()
# print(s)
f.close()

# Reading an entire file using readline function.

f = open("ram.txt", "r")
while True:
    s = f.readline()
    if s == "":
        break

    else:
        print(s, end="")

# Using with() function, which helps to automatically close the file. That's why we don't have to use close() function in the end.

# Context managers are objects that can be used in Python's with statements. You'll often see with statements used when working with files in Python. This code opens a file, uses the f variable to point to the file object, reads from the file, and then closes the file.


def ram():
    with open("ram.txt", "r") as a:
        s = a.read()
        return s


print(ram())

# With can also be used with write and append mode in file handling with the same procedure and rules.


"""
    ---------------*** IMPORTANT NOTE ***-------------------
    1. We close files after using in python to free up the space it occupies in the memory.
    2. If we don't close it, garbage collector would close it. But it will keep using our memory until it gets closed.
    3. That's why we use "with" keyword as it closes the file as soon as the usage is over.
"""
