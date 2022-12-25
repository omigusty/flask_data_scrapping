from bs4 import BeautifulSoup
import requests

datas = []

urlTarget = requests.get("https://quotes.toscrape.com/")
beautify = BeautifulSoup(urlTarget.content, "html.parser")
quotes = beautify.find_all("div", class_="quote")

for quote in quotes:
    getQuote = quote.find("span", class_="text").text
    getAuthor = quote.find("small", class_="author").text
    dictionary = {"quote": getQuote, "author": getAuthor}

    datas.append(dictionary)

for data in datas:
    print(data["quote"])
