from nose.tools import *
from ex48.parser_class import *

test = Parser()

def test_parse_verb():
    assert_equal(test.parse_verb([('verb', 'go')]), ('verb', 'go'))
    assert_raises(ParserError, test.parse_verb, ('noun', 'bear'))
    result = test.parse_verb([('stop', 'of'), ('verb', 'stop')])
    assert_equal(result, ('verb', 'stop'))
	
def test_parse_object():
    assert_equal(test.parse_object([('noun', 'door')]), ('noun', 'door'))
    assert_raises(ParserError, test.parse_object, ('verb', 'go'))
    result = test.parse_object([('stop', 'in'),('noun', 'princess')])
    assert_equal(result, ('noun', 'princess'))
	
def test_parse_subject():
    assert_equal(test.parse_subject([('noun', 'princess')]), ('noun', 'princess'))
    assert_equal(test.parse_subject([('verb', 'go')]), ('noun', 'player'))
    assert_raises(ParserError, test.parse_subject, ('direction', 'east'))
    result = test.parse_subject([('stop', 'the'),('verb', 'stop')])
    assert_equal(result, ('noun', 'player'))

def test_parse_sentence():
    sentence = test.parse_sentence([('noun', 'bear'), ('verb', 'go'), ('direction', 'east')])
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'go')
    assert_equal(sentence.object, 'east')
    sentence = test.parse_sentence([('verb', 'stop'), ('stop', 'the'), ('noun', 'bear')])
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'stop')
    assert_equal(sentence.object, 'bear')
    word_list = [('direction', 'east'), ('noun', 'bear')]
    assert_raises(ParserError, test.parse_subject, word_list)