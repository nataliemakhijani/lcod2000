# I'm not actually web-scraping my blog because I don't want to mess up my analytics, so I'm just scraping the source repo!
import glob
import sys

from bs4 import BeautifulSoup

def getContent(soupdata):
    outcon = []
    con = soupdata.select(".content")
    if con:
        for c in con:
            outcon.append(c.get_text())
    return outcon

scraped = ""

files = glob.glob(sys.argv[1] + '**/**/*.html', recursive=True) # pass in eleventy build dir to scrape

print("scraping", sum(1 for _ in files), "files")

for filename in files:
    text = open(filename, "r").read() # ignore the frontmatter (markdown metadata stuff)
    soup = BeautifulSoup(text, features="xml")
    content = getContent(soup)
    scraped += "\n\n\n".join(content) # add the text to the corpus

# Save it
ns_data = open('natalie_html.txt', 'w') # open the file
ns_data.write(scraped) # write the file
ns_data.close() # close the file
# we're done

# python3 scrape.py ~/Projects/the-natalie-zone/_site
