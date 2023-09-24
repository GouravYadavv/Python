# Importing required libraries
import matplotlib.pyplot as plt
import numpy as np

# Let's create a dictonary to plot bar graph
x={"Ram":15,"Sham":14,"Geeta":16}
# It is a dictonary containing the name of the students with their age.

# Let's convert the elements of the dictonary into list.
name=list(x.keys())
age=list(x.values())

# Let's check wheather the keys and values of the dictonary are converted to two different lists or not
print(name,"\n",age)

# For ploting bar graph we use bar().
plt.bar(name,age,color="skyblue",   )
plt.title("Age distribution of students")
plt.xlabel("Names")
plt.ylabel("Age")
plt.grid(True)

# For printing the bar graph horizontally use h after bar as plt.barh()

# To show the graph
plt.show()