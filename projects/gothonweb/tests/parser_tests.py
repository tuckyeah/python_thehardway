from nose.tools import *
from gothonweb.parser import *

WORD_TYPES = {
'verb': ['take', 'throw', 'place', 'shoot', 'dodge', 'tell'],
'noun': ['bomb', 'joke'],
'stop': ['the', 'a', 'it', 'from', 'at', 'of']
}

def test_parse_verb():
	assert_equal(parse_verb([('verb', 'take')]), ('verb', 'take'))
	assert_raises(ParserError, parse_verb, ('noun', 'bear'))
	result = parse_verb([('stop', 'the'), ('verb', 'throw')])
	assert_equal(result, ('verb', 'throw'))
	result = parse_verb([('number', '1234')])
	assert_equal(result, ('number', '1234'))

def test_parse_object():
	assert_equal(parse_object([('noun', 'bomb')]), ('noun', 'bomb'))
	assert_raises(ParserError, parse_object, ('verb', 'dodge'))
	result = parse_object([('noun', 'joke'), ('stop', 'the')])
	assert_equal(result, ('noun', 'joke'))

def test_parse_sentence():
	sentence = parse_sentence([('verb', 'throw'), ('noun', 'bomb')])
	assert_equal(sentence.subject, 'player')
	assert_equal(sentence.verb, 'throw')
	assert_equal(sentence.object, 'bomb')
	sentence = parse_sentence([('verb', 'tell'), ('stop', 'a'), ('noun', 'joke')])
	assert_equal(sentence.subject, 'player')
	assert_equal(sentence.verb, 'tell')
	assert_equal(sentence.object, 'joke')

def test_scan_sentence():
	sentence = scan_sentence('throw bomb')
	assert_equal(sentence.verb, 'throw')
	assert_equal(sentence.object, 'bomb')

	sentence = scan_sentence('1234')
	assert_equal(sentence.verb, 'enter')
	assert_equal(sentence.object, '1234')
