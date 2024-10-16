import markovify


natalie = open('natalie.txt', 'r').read()

chain = markovify.Text(natalie)

print(chain.make_short_sentence(280))

# Without knowing it, they showed me just how much less toxic the housing discourse is here.