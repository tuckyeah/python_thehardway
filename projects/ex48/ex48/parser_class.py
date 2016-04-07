import lexicon
from sys import exit 
import parser_class

class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, obj):
	    # remember we are taking tuples of (word_type, word) and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = obj[1]
		

def peek(word_list):
    #checks if we have given it a variable
    #does NOT check for no variable 
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None
			
    
def match(word_list, expecting):
    # pops the tuple and then works with that
	# this is basically a way to remove the tuple from the sentence
	# so we can keep moving forward
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None
			
    
def skip(word_list, word_type):
# skips all words in a given category (usually 'stop')
# this does not RETURN anything - it just alters the Sentence tuple list
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
        elif next_word == 'direction':
            return match(word_list, 'direction')
        elif next_word == 'number':
            return match(word_list, 'number')
        elif next_word == 'error':
            problem_word = word_list[0]
            get_user_input(problem_word)		
        else:
            raise ParserError("Expected a noun or direction next.")


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
            raise ParserError("Expected a verb next.")
	
	
    def parse_sentence(self, word_list):
        subj = self.parse_subject(word_list)
        verb = self.parse_verb(word_list)
        obj = self.parse_object(word_list)

        return Sentence(subj, verb, obj)    

		
def scan_sentence(ans):
    scanned_phrase = lexicon.scan(ans)
    
    if len(scanned_phrase) <= 1:
       print "Not enough words! Try again"
       get_user_input()
    
    parsed_phrase = Parser()
    sentence = parsed_phrase.parse_sentence(scanned_phrase)
    
    print sentence.subject
    print sentence.verb
    print sentence.object
    exit(1)


def get_user_input(*arg):
    if arg:
        print "I don't understand %s, try again" % arg
    
    ans =  raw_input("Type a sentence > ")
    scan_sentence(ans)
