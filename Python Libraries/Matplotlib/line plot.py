# Importing libraries
import numpy as np
from matplotlib import pyplot as plt # you can also use import matplotlib.pyplot as plt

# Let's creat an array
x=np.arange(0,11)
print(x)

# Creating another arrays to plot a 2-D graph
y1=2*x
print(y1)

y2=3*x
print(y2)

#plotting a graph and displaying it
plt.plot(x,y1,color="red",linestyle=":",linewidth="4") # We can customise out line of plot here
plt.plot(x,y2,color="blue",linestyle="--",linewidth="2")
# now we can also add labels as
plt.title("Line Plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.show()
