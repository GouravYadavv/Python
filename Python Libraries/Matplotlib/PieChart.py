# Importing required python library.
import matplotlib.pyplot as plt

# Creating 2 arrays of which 1 contains comapny and another contains the market share of that company.
Company=["Apple","Samsung","Nokia","Realme","OnePlus"]
Market_Share=[45,34,67,89,23]

# Pie chart syntax
plt.pie(Market_Share,labels=Company,colors=["blue","green","red","purple","skyblue"],autopct="%0.1f%%",radius=1) # We can use differet radius as per the requirements.
# auropct represents the value after the decimal, if it is keept 0.2 instead of 0.1 it would have shown the decimal values upto 2 digits.
# Colors should be in the same manner as the company written in the array.
# Color at each index represents the array at the same index respectively.

plt.title("Pie Chart")
plt.show()