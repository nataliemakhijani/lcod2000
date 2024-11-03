def buildDictionary(corpus):
    wc = len(corpus)

    markovDictionary = {}

    for word in corpus:
        if not word in markovDictionary: # if this word isn't in the dictionary...
            markovDictionary[word] = [] # initialize it

        if corpus.index(word) == (wc - 1): break # get out of here, we're at the end.

        nextPossibleWordsAmount = len(markovDictionary[word]) 
        corpusIndex = getIndexForWord(word, nextPossibleWordsAmount)
