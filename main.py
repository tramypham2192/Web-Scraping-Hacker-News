from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

#if using html.parser shows error, may use lxml instead, then have to import lxml
soup = BeautifulSoup(contents, "lxml")
soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)
# print(soup.prettify())
print(soup.a)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="h1id")
print(heading)
section_heading = soup.find(name="h3", class_ = "heading")
print(section_heading)
# print(section_heading.get("class"))

# get a specific element => have to use css selector
#select using tag name
company_url = soup.select_one(selector="p a")
print("select using css selector" , company_url)
#select using id
name = soup.select_one(selector="#h1id")
print("select using css selector and id of the element", name)
#select using class
print("select using css selector and class name of the element", soup.select(".heading"))