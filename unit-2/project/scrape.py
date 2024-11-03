# I'm not actually web-scraping my blog because I don't want to mess up my analytics, so I'm just scraping the source repo!
import glob
import sys

scraped = ""

files = glob.glob(sys.argv[1] + '**/**/*.md', recursive=True) # pass in dir to scrape
# alternatively, could use bs to scrape generated build files, might be slightly higher quality? not actually scraping my website over http because i have some antiscraping stuff, and don't want to mess with my analytics

print("scraping", sum(1 for _ in files), "files")

for filename in files:
    text = open(filename, "r").read().split('---')[2] # ignore the frontmatter (markdown metadata stuff)
    scraped += text # add the text to the corpus
    
ns_data = open('natalie.txt', 'w') # open the file
ns_data.write(scraped) # write the file
ns_data.close() # close the file

# we're done

# python3 scrape.py ~/Projects/the-natalie-zone/content