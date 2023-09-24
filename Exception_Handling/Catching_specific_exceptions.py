# In this program we will be studying how to catch specific exceptions, which are needed when a code can have multiple exceptions.

# This is really useful to identify a specific expection occuring instead of displaying a same message for all types of example.

# Let's take an example to understand this concept more.

# Let's take a code containing more than one exceptions, so how it will run without catching specific exception.

try:
    with open("ram.txt", "r") as r:
        r.read()
        print(ram)
except:
    print("An unsual exception occured.")

"""
    What will happen in the code is,
    1. It will show show first error for the file not found as there is no file named "ram.txt" in our directory.
    2. If this file were there so the second error would for "ram" variable because it couldn't be found

    But for both the exceptions out program will be displaying the same message which will confuse the user why actually the error is occuring and will be difficult to find out.
    So, to resolve this type of problems we have catching specific exceptions.
"""

# To tackle multiple exceptions the code should be written as

try:
    m = 5
    L = [1, 2, 3, 4, 5]
    with open("ram.txt", "r") as r:
        r.read()
    print(m / 0)
    print(L[100])
except FileNotFoundError:
    print("File not found, please recheck the name you have entered.")
except ZeroDivisionError:
    print("Can't be divided by 0.")
except (
    Exception
) as e:  # Here we will be hacing an index error but we are not defining it to catch it.
    print(
        e.with_traceback
    )  # This will return any unspecified exception which will occur while compiling.

# So in this code block we have specified most of the exceptions which were having a chances to occur, in our knowledge and also if there is any other error it will be printed.


# This is how you can code to catch specific exceptions.
