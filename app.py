from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import pandas as pd

app = Flask(__name__)

datas = []


@app.route("/")
def index():
    try:
        for pages in range(1, 11):
            urlTarget = requests.get(
                "https://quotes.toscrape.com/page/"+str(pages))
            beautify = BeautifulSoup(urlTarget.content, "html.parser")
            quotes = beautify.find_all("div", class_="quote")

            for quote in quotes:
                getQuote = quote.find("span", class_="text").text
                getAuthor = quote.find("small", class_="author").text

                datas.append({"quote": getQuote, "author": getAuthor})

            # saveFile = pd.DataFrame(datas)
            # saveFile.to_csv("data_quote.csv", encoding="utf-8")

        return render_template("index.html", datas=datas)
    except Exception as err:
        print("error", err)


def download():
    index.data


if __name__ == "__main__":
    app.run(debug=True)
