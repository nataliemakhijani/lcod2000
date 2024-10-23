# mission
1. generate my own onion articles

# steps
1. scraping onion RSS feed (RSS over html so I can get more content per page)
1. convince beautiful soup to parse rss (or dont use bs) OR ditch rss and scrape multiple pages, maybe every story on today's homepage?
1. build the probability map
1. generate some stuff

# issues
1. BS doesn't like things that appear as psuedotags (ie `content:encoded` in xml), so need to get it to accept that as a selector
1. onion doesn't have that much on each page of results
    - use xml
