# Just like a pie chart, a doughnut chart shows the relationship of parts to a whole, but a doughnut chart can contain more than one data series. Each data series that you plot in a doughnut chart adds a ring to the chart. The first data series is displayed in the center of the chart.
# Importing the python libraries.
import matplotlib.pyplot as plt

Company=["Apple","Samsung","Vivo","Realme",'Nokia']
Sales_Increase=[45,34,56,67,34]
Profit=[56,78,34,23,78]

plt.pie(Sales_Increase,labels=Company,radius=2)
plt.pie([1],colors="white",radius=1)
plt.title("DoughNut-Chart")
plt.axis("equal") # It will help to adjust the chat in the frame.
plt.show()