from nose.tools import *
from gothonweb.parser import *

WORD_TYPES = {
'verb': ['take', 'throw', 'place', 'shoot', 'dodge', 'tell'],
'noun': ['bomb', 'joke'],
'stop': ['the', 'a', 'it', 'from', 'at', 'of']
}

test = Parser()

def test_parse_verb():
	assert_equal(test.parse_verb([('verb', 'take')]), ('verb', 'take'))
