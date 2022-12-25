from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route("/")
def index():
    try:
        datas = []

        urlTarget = requests.get("https://quotes.toscrape.com/")
        beautify = BeautifulSoup(urlTarget.content, "html.parser")
        quotes = beautify.find_all("div", class_="quote")

        for quote in quotes:
            getQuote = quote.find("span", class_="text").text
            getAuthor = quote.find("small", class_="author").text

            datas.append({"quote": getQuote, "author": getAuthor})

        return render_template("index.html", datas=datas)
    except Exception as err:
        print("error", err)


if __name__ == "__main__":
    app.run(debug=True)
