WORD_TYPES = {
'verb': ['take', 'throw', 'place', 'shoot', 'dodge', 'tell', 'enter', 'try'],
'noun': ['bomb', 'joke', 'gun', 'bullet'],
'stop': ['the', 'a', 'it', 'from', 'at', 'of']
}

VOCABULARY  = {word: word_type for word_type, words in WORD_TYPES.items() for word in words}

def scan(sentence):
	"""scans given sentence and splits into tuples of wordtype/word
	based on given lexicon"""
	tokens = []
	wordlist = sentence.split()

	for word in wordlist:
		try:
		    word_type = VOCABULARY[word.lower()]
		except KeyError:
			try:
				word = int(word)
				word_type = 'number'
			except ValueError:
				word_type = 'error'

		tokens.append( (word_type, word) )

	return tokens