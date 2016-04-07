from nose.tools import *
from ex48.parser import *

def test_peek():
	assert_equal(peek([('verb', 'go')]), 'verb')
	assert_equal(peek([]), None)
	result = peek([('direction', 'north')])
	assert_equal(result, 'direction')

def match_test():
	assert_equal(
		match([('noun', 'bear') 'noun'), 
		'noun')