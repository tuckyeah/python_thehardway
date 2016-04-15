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



class Parser(object):

	def parse_verb(self, word_list):
		skip(word_list, 'stop')
		next_word = peek(word_list)

		if next_word == 'verb':
			return match(word_list, 'verb')
		elif next_word == 'error':
			problem_word = word_list[0]
			get_user_input(problem_word)
		else:
			raise ParserError("Expected a verb next.")

	def parse_object(self, word_list):
		skip(word_list, 'stop')
		next_word = peek(word_list)

		if next_word == 'noun':
			return match(word_list, 'noun')
		elif next_word == 'number':
			return match(word_list, 'number')
		elif next_word == 'error':
			problem_word = word_list[0]
			get_user_input(problem_word)
		else:
			raise ParserError("Expected a noun next.")

	def parse_subject(self, word_list):
		skip(word_list, 'stop')
		next_word = peek(word_list)

		if next_word == 'noun':
			return match(word_list, 'noun')
		elif next_word == 'verb':
			return ('noun', 'player')
		elif next_word == 'error':
			problem_word = word_list[0]
			get_user_input(problem_word)
		else:
			raise ParserError("expected a verb next.")

	def parse_sentence(self, word_list):
		subj = self.parse_subject(word_list)
		verb = self.parse_verb(word_list)
		obj = self.parse_object(word_list)

		return Sentence(subj, verb, obj)

def scan_sentence(ans):
	scanned_phrase = lexicon.scan(ans)

	parsed_phrase = Parser()
	sentence = parsed_phrase.parse_sentence(scanned_phrase)

# so, we need to scan the sentence from the user 
# and in the returned sentence object, confirm that the returned
# verb/obj matches what we're expecting 