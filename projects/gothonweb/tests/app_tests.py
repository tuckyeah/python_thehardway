from nose.tools import *
from bin.app import *
from tests.tools import assert_response

def test_index():
    #check that Index redirects to 'Game'
    resp = app.request("/")
    assert_response(resp, status = "303 See Other")
	
	#check first GET request to /game
    resp = app.request("/game")
    assert_response(resp)
	