WORD_TYPES = {
    'verb' : ['go', 'stop', 'kill', 'eat'],
    'direction' : ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
    'noun' : ['bear', 'princess', 'door', 'cabinet'],
    'stop' : ['the', 'in', 'of', 'from', 'at', 'it']
}
# invert the dictionary
#             value: key      for key,  list value in WORD_TYPES key/values for each value in list
VOCABULARY = {word: word_type for word_type, words in WORD_TYPES.items() for word in words}
# taken from http://codereview.stackexchange.com/questions/14238/learn-python-the-hard-way-48-lexicon-exercise


# get sentence from user
def scan(sentence):
    """scans given sentence and splits the sentence into tuples 
    of word type/word, based on given lexicon"""
    tokens = []
    wordlist = sentence.split()

    for word in wordlist:
        try:
            word_type = VOCABULARY[word.lower()] # makes  sure it can handle all cases
        except KeyError: # tries to treat it as an integer
            try:
                word = int(word)
                word_type = 'number'
            except ValueError: # if it's not an integer, assume not found in lexicon; return error.
                word_type = 'error'
        tokens.append( (word_type, word) )

    return tokens
