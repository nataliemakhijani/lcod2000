import requests
from bs4 import BeautifulSoup

response = requests.get("https://natalie.zone/about")

soup = BeautifulSoup(response.text, "html.parser")
all_the_text = soup.get_text()

ns_data = open('natalie.txt', 'w')
ns_data.write(all_the_text)
ns_data.close()