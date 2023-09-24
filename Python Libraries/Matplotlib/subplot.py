# Now let's come to the sub plot
# A major function of subplot is to help develop secondary characters or other main characters aside from the main protagonist more fully.
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,11)
print(x)
y1=2*x
y2=3*x

# Subplot is like dividing a plot into subparts, by which instead of showing 2 lines in one graph it distributes them into two, which helps us to analyze them better.
plt.subplot(1,2,1) # Syntax: subplot("no. of rows", "no. of columns", "index no. of subplot")
plt.plot(x,y1,color="r",linestyle="--",linewidth="3")
plt.title("First plot")

plt.subplot(1,2,2)
plt.plot(x,y2,color="b",linestyle=":",linewidth="4")
plt.title("Second plot")

plt.show()