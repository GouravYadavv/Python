# importing the required python libraries.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Seaborn have it's own example datasets which we can get by using sns.get_dataset_names.
frmi=sns.load_dataset("fmri")
# We are using frmi one of the seaborn dataset for this program.
frmi.head() # Checkout either your dataset is loaded properly or not by using head() which will print first 5 lines of the dataset.

# Let's displat a lineplot between any two columns of the dataset.
sns.lineplot(x="timepoint",y="signal",data=frmi,hue="event") # 'hue' is used to visualize the data of different categories in one plot.
plt.show() # We use show to display the graph.