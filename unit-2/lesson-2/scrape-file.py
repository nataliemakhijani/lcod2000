import glob
import sys

scraped = ""

files = glob.iglob(sys.argv[1] + '**/**/*.md', recursive=True)

print("scraping", sum(1 for _ in files), "files")

for filename in files:
    # print("Scraping", filename)
    text = open(filename, "r").read().split('---')[2]
    scraped += text
    
ns_data = open('natalie.txt', 'w')
ns_data.write(scraped)
ns_data.close()

# python3 scrape-file.py ~/Projects/the-natalie-zone/content
# scrapes all content from my website
