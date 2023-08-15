import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")
elements = soup.select(".titleline > a")
print(elements)

def get_data(elements):
    hn = []
    for element in elements:
        title = element.getText()
        href = element.get("href")
        upvote = element.find_next(class_="score")
        points = upvote.getText()

        hn.append({"title": title, "href": href, "points": points})
    return hn


print(get_data(elements))