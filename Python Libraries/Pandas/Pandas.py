# Starting with pandas 
# Checkout NumPy repository before pandas
# Importing pandas and NumPy to use them together
import pandas as pd
import numpy as np

# Pandas series object
s1=pd.Series([1,2,3])
print(s1)

# For giving index value manually
s1=pd.Series([1,2,3],index=["a","b","c"])
print(s1)
print(type(s1)) # <class 'pandas.core.series.Series'>

# Using pandas to give indexing to dictonary
# Let's take a dictonary d1
d1={"a":"ram","b":"sam","c":"kam"}
print(pd.Series(d1))

# We can also use this technique with indexing to sort them in a particular manner
print(pd.Series(d1,index=["b","c","a","d"])) # If we will give any extra index here like d so it will give value NaN

# Other techniques to extract individual element or selected elements

A=pd.Series([1,2,3,4,5,6,7])
# Extracting a single element
print(A[1])

# Extracting a sequence of elements
print(A[2:5:2])

# Extracting elements from back
print(A[-3::-1])

# Adding elements of 2 series
# Let's take another series
A2=pd.Series([2,3,4,5,6,7,8])
print(A+A2) #By same way we can add any fixed numbers of integers to all the elements of series
