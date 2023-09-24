# The histogram is a popular graphing tool. It is used to summarize discrete or continuous data that are measured on an interval scale. It is often used to illustrate the major features of the distribution of the data in a convenient form.
# Importing the required python library.
import matplotlib.pyplot as plt

# Taking an array to represent the histogram.
x=[1,1,1,2,3,4,5,3,4,3,2,5,6,7,5,9,2,0]

plt.hist(x,color="orange",bins=4) # Bins is used to limit the number of bins in histogram.
plt.show()