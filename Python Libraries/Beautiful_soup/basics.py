from bs4 import BeautifulSoup as bs
import requests

with open("sample.html") as html_file:
    soup = bs(html_file, "lxml")

# Now extracting the html content of the page and printing it.
# print(soup.prettify()) # here we have used prettify to make the html content more readable.

# Now we can extract the title of the page.
print(
    soup.title
)  # So here we are also getting the title tag along with the title. So we can use the text attribute to get only the title.

print(soup.title.text)  # So here we are getting only the title of the page.

# Now let's get the first div tag of the page.
print(soup.div)

# Now let's get the div tag of the page of footer class.
print(
    soup.find("div", class_="Footer")
)  # Here we are using the find method to get the div tag of the page of footer class. And we are also using underscore after class because class is a keyword in python.

# We should inspect the page first to get the class name of the div tag. And we can also use the id to get the div tag.

# Now let's use for loop to get all the div tags of the page.
for div in soup.find_all("div"):
    print(
        div.text
    )  # Here we are using the text attribute to get only the text of the div tag.
