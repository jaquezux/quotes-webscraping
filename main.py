from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("span", class_="text")                    
authors = soup.findAll("small", class_="author")

for quote, author in zip(quotes[2], authors[2]):
    print(quote.text + " - " + author.text)
    
# Output
# “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.” - Albert Einstein
