import lexicon
from sys import exit

class ParserError(Exception):
	pass

class Sentence(object):

	def __init__(self, subject, verb, obj):
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = obj[1]


def peek(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None

def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)

		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None

def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)


def parse_verb(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)

	if next_word == 'verb':
		return match(word_list, 'verb')
	elif next_word == 'number':
		return match(str(word_list), 'number')
	elif next_word == 'error':
		problem_word = word_list[0]
		return problem_word
	else:
		raise ParserError("Expected a verb next.")

def parse_object(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'number':
		return match(str(word_list), 'number')
	elif next_word == 'error':
		problem_word = word_list[0]
		return problem_word
	else:
		raise ParserError("Expected a noun next.")

def parse_subject(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'verb' or next_word == 'number':
		return ('noun', 'player')
	elif next_word == 'error':
		problem_word = word_list[0]
		return problem_word
	else:
		raise ParserError("expected a verb next.")

def parse_sentence(word_list):
	subj = parse_subject(word_list)
	verb = parse_verb(word_list)
	obj =  parse_object(word_list)

	return Sentence(subj, verb, obj)

# we need a way to handle words not in the keys
# if we add an object in the Room class that holds the errors...
# then we can check if there are errors?

def scan_sentence(ans):
	scanned_phrase = lexicon.scan(ans)

	# if it's a one word answer, check if it's a verb or a number and treat
	# it accordingly
	if len(scanned_phrase) == 1:
		word_type = scanned_phrase.pop(0)
		if word_type[0] == 'number':
			return Sentence(('noun', 'player'), ('verb', 'enter'), str(word_type))
		elif word_type[0] == 'verb':
			return Sentence(('noun', 'player'), word_type, ('object', 'object'))
	else:
		return parse_sentence(scanned_phrase)




# so, we need to scan the sentence from the user 
# and in the returned sentence object, confirm that the returned
# verb/obj matches what we're expecting 