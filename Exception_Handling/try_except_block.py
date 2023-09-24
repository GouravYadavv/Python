# try catch example

# Let's try to open a file which doesn't exist in our directory, which will give us file not found error but we will handle this exception using try except block.

try:
    with open("ram.txt", "r") as o:
        o.read()
except:
    print("File not found, recheck the name you have entered.")

# Here instead of showing an exception here out program will return this print statement.
