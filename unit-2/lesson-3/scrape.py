import requests
from bs4 import BeautifulSoup

onion_response = requests.get("https://theonion.com/feed/")

# french_onion_soup = BeautifulSoup(onion_response.text, "html.parser")
french_onion_soup = BeautifulSoup(onion_response.text, features="xml")

french_onion_text = french_onion_soup.get_text()

articles = []

def getTitles(soupdata):
    titles = soupdata.find_all("content:encoded") # this gives me html, so now run thru BS again?
    if titles:
        for t in titles:
            articles.append(t.get_text())

getTitles(french_onion_soup)

articleText = " ".join(articles)

onion_data = open('onion.txt', 'w')
onion_data.write(articleText)
onion_data.close()