#printing array of 2X2 with zeros
import numpy as np
#imported numpy before using it
array1=np.zeros((2,2))
print(array1)

#printing 3X3 array of same integer=1
#we don't have to import the numpy again as we have already did above
array2=np.full((3,3),1)
print(array2)

#to find maximum value in an array
array3=np.amax([1,2,4,3])
print(array3)

#to find minimum value in an array
array4=np.amin([2,3,4,1,5])
print(array4)

#to print an array within a range
array5=np.arange(1,11)
#add a value after 11 followed by a coma "," to skip between the range
print(array5)

#for getting an array of random numbers between a fixed range
import random
array6=np.random.randint(1,100,10)
#1 and 100 represent the range while 10 represent how many values you want in an array
print(array6)

#to check the shape of an array
print(array2.shape)
# shape can also be used to change the shape of an array

#some more methods which can be used between to 2 arrays are vstack(), hstack(), column_stack()
"""
vstack() is used to stack the sequence of NumPy arrays vertically and return the single array.
hstack() is used to stack or concatenate arrays in sequence horizontally (column-wise).
column_stacK() takes a sequence of 1-D or 2-D arrays and stacks them as columns into a 2-D array.
"""
array7=[1,2,3]
array8=[4,5,6]

array9=np.vstack((array7,array8))
print(array9)

array10=np.hstack((array7,array8))
print(array10)

array11=np.column_stack((array7,array8))
print(array11)

#for finding the intersection between 2 arrays or common elements of 2 arrays we have intersection() method
arrayA=[1,2,3,4,5]
arrayB=[4,5,6,7,8]
# As we are having 4 and 5 common to how to find out these common elements between large arrays
print(np.intersect1d(arrayA,arrayB))

#find out the different elements of 2 arrays as we are having 1,2,3 in arrayA only and 6,7,8 in arrayB only
print(np.setdiff1d(arrayA,arrayB)) #for arrayA unique values 
print(np.setdiff1d(arrayB,arrayA)) #for arrayB unique values

#adding of 2 or more NumPy arrays
#Let's take 2 new arrays
ArrayC=np.array([3,4])
ArrayD=np.array([5,6])
print(np.sum((ArrayC,ArrayD)))

# now we a new attribute called as axis which is used to add in row and column
print(np.sum([ArrayC,ArrayD],axis=0))
print(np.sum([ArrayC,ArrayD],axis=1))

#now we have operations like subtracting, adding , multiplying and dividing complete array by a integer

#for adding 1 in all the elements of an array
ArrayC+=1
print(ArrayC)

#for subtracting 1 from all the elements of an array
ArrayD-=1
print(ArrayD)

#for multiplying 2 to all the elements of an array
ArrayC*=2
print(ArrayC)

#for dividing 2 from all the elements of an array
ArrayC=ArrayC/2
print(ArrayC)

# Now we are going to calculate the mean, median and standard deviation of an array using NumPy

#for calculating mean let's take a new array
ArrayE=np.array([1,2,3,4,5])
print(np.mean(ArrayE))

#for calculating median  of an array
print(np.median(ArrayE))

#for calculating standard deviation  of an array
print(np.std(ArrayE))

#we can also print dimensions of as array and elements of it by using index of an array
#let's consider a new array
A1=np.array([[1,2,3],[3,4,5],[5,6,7]])
#index value of an array starts with 0
print(A1[0])
print(A1)

# to find the transpose of a number we have a transpose
print(np.transpose(A1))

# Now, let's come to the matrix multiplication
# let's consider 2 new arrays
A2=np.array([[1,2,3],[4,5,6],[7,8,9]]) 
A3=np.array([[9,8,7],[6,5,4],[3,2,1]])
# For multiplication
print(A2.dot(A3))