import markovify
import sys

corpus = open(sys.argv[1]).read() # open the corpus

generator = markovify.Text(corpus, state_size=3) #

text = ""

for i in range(4): # we want 4 sections
    section_title = str(generator.make_short_sentence(50, 25)) # for some reason, this doesn't reliably work
    section = "# " + section_title + "\n\n"

    for j in range(5): # 5 paras per section
        paragraph = ""
        for k in range(10):
            paragraph += str(generator.make_short_sentence(100, 25)) # min 25 chars, max 100 chars
            paragraph += " "

        section += paragraph + "\n\n"

    text += section + "\n\n" # add it w/ a trailing new line

ns_data = open('blog-post.md', 'w') # open the file
ns_data.write(text) # write the file
ns_data.close() # close the file