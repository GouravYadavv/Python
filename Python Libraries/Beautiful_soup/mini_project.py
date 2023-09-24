from bs4 import BeautifulSoup as bs
import requests

source = requests.get("https://quotes.toscrape.com/").text

soup = bs(source, "lxml")

# print(soup.prettify()) # We can first print the complete webpage to analyze it's content.


# Printing the title of the page

print(soup.title.text)

# Whenever we don't specify the class of the tag we are given the first tag which appears first while searching.

print(
    soup.find("span", class_="text").text
)  # Instead of going div by div we can also directly search for the required tag by specifying it's class.


# Now let's print all the quotes on the page number 1

all_quotes = soup.find_all("span", class_="text")

for i in all_quotes:
    print(i.text)


# We can access a specific value from an attribute of tag just like a dictionary.
