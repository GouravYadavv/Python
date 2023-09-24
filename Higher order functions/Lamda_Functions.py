""" 
    Lambda functions are also known as anonymous functions.
    These are the type of functions which are written in a single line.
    Syntax for lambda function is as follows:
        Lambda input: expression
"""

# Let's start by taking a simple example of squaring a number by the lambda function.

x = lambda x: x**2
# We have stored this function in a variable x, it will be used as:
print(x(5))
print(x(9))

# Example 2: for addition of 2 numbers.
y = lambda x, y: x + y
print(y(2, 4))

# Example 3: for checking odd and even number.
z = lambda x: "Even" if x % 2 == 0 else "Odd"
print(z(5))

# Example 4: check if the first letter of a string is "a" or not.
w = lambda x: x[0] == "a"
print(w("apple"))


# More examples of lambda function.
# Lambda function is maily used with higher order functions, these are the function which contains more functions.


def return_sum(func, L):
    result = 0
    for i in L:
        if func(i):
            result += 1

    return result


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = lambda x: x % 2 == 0
y = lambda x: x % 2 != 0

print(return_sum(x, L))
print(return_sum(y, L))


""" 
    Python basically have 3 higher order functions-
    1. Maps
    2. Filter
    3. Reduce
"""
