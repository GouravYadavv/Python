# Box and whisker plots, sometimes known as box plots, are a great chart to use when showing the distribution of data points across a selected measure. These charts display ranges within variables measured. This includes the outliers, the median, the mode, and where the majority of the data points lie in the “box”.
# Importing required python libraries.
import matplotlib.pyplot as plt
import numpy as np

# Creating 3 arrays to plot a box plot.
a=[1,2,3,4,5,6,7]
b=[3,4,5,2,2,1,2]
c=[3,4,5,6,2]

x=list([a,b,c])

plt.boxplot(x)
plt.title("Box Plot")

# The prpocedure will be same for violin plot as of box plot and we will have to use the syntax written below.
#plt.violinplot(x,showmedians=True)

plt.grid(True)
plt.show()