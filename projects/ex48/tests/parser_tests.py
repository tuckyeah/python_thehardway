from nose.tools import *
from ex48.parser import *

def test_peek():
	assert_equal(peek([('verb', 'go')]), 'verb')
	assert_equal(peek([]), None)
	result = peek([('direction', 'north')])
	assert_equal(result, 'direction')

def test_match():
    assert_equal(match([('noun', 'bear')], 'noun'), ('noun', 'bear'))
    assert_equal(match([('verb', 'go')], 'noun'), None)
    result = match([('noun', 'princess')], 'noun')
    assert_equal(result, ('noun', 'princess'))
	
def test_skip():
    assert_equal(skip([('stop', 'the')], 'stop'), None)
    result = [('stop', 'in'), ('direction', 'west')]
    skip(result, 'stop')
    assert_equal(result, [('direction', 'west')])
	
def test_parse_verb():
    assert_equal(parse_verb([('verb', 'go')]), ('verb', 'go'))
    assert_raises(ParserError, parse_verb, ('noun', 'bear'))
    result = parse_verb([('stop', 'of'), ('verb', 'stop')])
    assert_equal(result, ('verb', 'stop'))
	
def test_parse_object():
    assert_equal(parse_object([('noun', 'door')]), ('noun', 'door'))
    assert_raises(ParserError, parse_object, ('verb', 'go'))
    result = parse_object([('stop', 'in'),('noun', 'princess')])
    assert_equal(result, ('noun', 'princess'))
	
def test_parse_subject():
    assert_equal(parse_subject([('noun', 'princess')]), ('noun', 'princess'))
    assert_equal(parse_subject([('verb', 'go')]), ('noun', 'player'))
    assert_raises(ParserError, parse_subject, ('direction', 'east'))
    result = parse_subject([('stop', 'the'),('verb', 'stop')])
    assert_equal(result, ('noun', 'player'))
	
def test_parse_sentence():
    sentence = parse_sentence([('noun', 'bear'), ('verb', 'go'), ('direction', 'east')])
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'go')
    assert_equal(sentence.object, 'east')
    sentence = parse_sentence([('verb', 'stop'), ('stop', 'the'), ('noun', 'bear')])
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'stop')
    assert_equal(sentence.object, 'bear')
    word_list = [('direction', 'east'), ('noun', 'bear')]
    assert_raises(ParserError, parse_subject, word_list)