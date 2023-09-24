# Let's try to implement these graphs on real life data, and let's plot a hinstogram for it.
# Importing required python libraries.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Loading file for read.
pf=pd.read_csv('cardata.csv')

# Printing the first 5 lines of the data to check it is load in the memory or not.
print(pf.head())

# Plotting histogram of the column "Selling_Price" from the csv file and settinf bins limit to 30 to normalise the data and color to red. 
plt.hist(pf["Selling_Price"],bins=30,color="red")
plt.show()