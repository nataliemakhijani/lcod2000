import glob
import sys

scraped = ""

for filename in glob.iglob(sys.argv[1] + '**/**/*.md', recursive=True):
    print("Scraping", filename)
    text = open(filename, "r").read().split('---')[2]
    scraped += text
    
ns_data = open('natalie.txt', 'w')
ns_data.write(scraped)
ns_data.close()

# python3 scrape-file.py ~/Projects/the-natalie-zone/content
# scrapes all content from my website
