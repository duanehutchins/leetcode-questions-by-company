from bs4 import BeautifulSoup
import requests

response = requests.get("https://leetcode.com/problemset/all/")
website_content = response.text

soup = BeautifulSoup(website_content, "html.parser")
print(soup.find_all(role="table")[0].div.div.div.div)

class Line:
    def __init__(self, line) -> None:
        list = [i.strip() for i in line.split('|') if i]
        self.solved
        self.number


with open("README.md") as file:
    data = file.readlines()
    file.close()
# print(data[0])

line = "| 717 | 1-bit and 2-bit Characters |  Easy | Google |"
print( [i.strip() for i in line.split('|') if i])
