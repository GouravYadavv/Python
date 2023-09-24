# Let's create a file "ram.txt" and write some text inside it.

# By open function python loads the file you have mentioned and loads it to the buffer memory, where it will be read character by character. The file stays in the buffer memory until it is closed.

# We use CRUD operaitons for file handling, that is create, read, update and delete.


f = open(
    "ram.txt", "w"
)  # "w" is used for writing into the file or creating a new file, and if a file already contains items then it will overwrite that file.
f.write("Hii, I am Ram")
f.close()  # A file must closed to prevent any changes to it in future. And prevent it to take extra space in the memory or unwanted access.

# To prevent overwriting and add text along with the text already present in the file we use append "a" mode.
f = open("ram.txt", "a")
f.write(
    "\nHii, I am Sita"
)  # It only take string arguments so it is effective to add each statements at time.
f.close()

# Now to add multiple lines at same time we use writelines() function, let's take a list "L" and add it line by line to our "ram.txt" file.

L = ["\nHello!\n", "I am Ram.\n", "How are you?\n", "I am fine.\n"]

f = open("ram.txt", "a")
f.writelines(
    L
)  # It is effective to add list in a file. With the help of which multiple lines can be inserted at a same time.
f.close()
