# Importing required libraries.
import matplotlib.pyplot as plt

# Let's create 3 arrays to plot a scatter plot graph between them.
x=[1,2,6,5,3,7,4,9]
y1=[2,3,4,1,5,8,6,5]
y2=[5,4,3,6,1,7,2,9] # If you will try to plot an array between arrays of different size it will shoe ValueError, so they must be of same size.

# Plotting the graph
plt.scatter(x,y1,color="green",marker="*",s=100) 
plt.scatter(x,y2,color="skyblue",marker=".",s=200)# Instead of writting colours we can use c="skyblue".
# Marker is used to give the symbol of representation and s is used for the size of the marker.
plt.title("Scatter Plot")
plt.grid(True)
# We can use subplot to display both of these scatter graph seperately.

# To display the graph.
plt.show()