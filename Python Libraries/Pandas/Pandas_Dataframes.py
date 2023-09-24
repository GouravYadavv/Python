# Now let's come to the dataframe, it is a 2-d labelled data sructure
# The dataframe comprises of rows and columns
# Importing the library pandas
import pandas as pd
import numpy as np

D1=pd.DataFrame({"Name":["Ram","Sam","Jam"],"Marks":[98,76,89]})
print(D1) # In the output the dictonary's Keys become the column names and the values become the records

print(type(D1)) #<class 'pandas.core.frame.DataFrame'>

# DataFrame have 4 in-built functions head(), tail(), describe() and shape()
# Let's just implement all of these one by one
# To implement these we need a sample csv(comma seperated value) file whivh you can easily download online
# So i have downloaded a sample file of car data so let's load it and apply functions

pf=pd.read_csv('cardata.csv')
print(pf.head()) # This will print first 5 lines of your dataset or if you will give any value inside head() it will print that no. of following rows

print(pf.tail()) # It is same as head but it will print from the bottom by default it is also 5 and can be set up manually

print(pf.shape) # It will print the size of the data, that is the no. of rows and columns it contains.

print(pf.describe()) # It will help to describe each column and the value distribution, min and max value and lot more

# Now to extract only the limited or required rows and columns we have a function called iloc[]

print(pf.iloc[0:4,0:3]) # It will extract the data from row index 0 to 3 as 4 is not included and columns from 0 to 3

# We can use loc function with the name of the column to print only the neened columns by their names respectively
print(pf.loc[0:11,("Car_Name","Selling_Price")])

# We can drop a column by using drop() function
print(pf.drop("Owner",axis=1)) # Owner column is dropped 
#---------------Important--------------#
# axis is set to 1 because we are dropping column, for dropping row we have to give axis=0.

# Some more basic panda functions
# Mean(), Median(),min() and max()

print(pf.mean())
print(pf.median())
print(pf.min())
print(pf.max())

