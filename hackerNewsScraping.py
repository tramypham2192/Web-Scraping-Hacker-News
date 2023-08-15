import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")
elements = soup.select(".titleline > a")
print(elements)

fileName = 'hackerNewsData.csv'
f = open(fileName, "w")
headers = "Title, Link, Upvotes \n"
f.write(headers)

def get_data(elements):
    for element in elements:
        title = element.getText()
        href = element.get("href")
        upvote = element.find_next(class_="score")
        points = upvote.getText()
        f.write(title.replace(",", "|") + "," + href + "," + points + "\n")
get_data(elements)
f.close()
