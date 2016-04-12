from nose.tools import *
from bin.app import *
from tests.tools import *

def test_index():
    #check that Index redirects to 'Game'
    resp = app.request("/")
    assert_response(resp, status = "303 See Other")
	
	#check first GET request to /game
    resp = app.request("/game")
    assert_response(resp)

    data = {'action': 'shoot!'}
    resp = app.request("/game", method="POST", data=data)
    assert_response(resp, status = '303 See Other')
	
def test_session():
    resp = app.request('/')
    session_id = get_session_id(resp)
	
    resp1 = app.request('/game', headers={'Cookie':session_id})
    assert_response(resp1, status='200', contains='Central Corridor')
	
