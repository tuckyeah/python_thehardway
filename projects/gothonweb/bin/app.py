import web
from gothonweb import map

web.config.debug = False

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
    '/count', 'count',
    '/reset', 'reset'
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room':None, 'count': 0})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")


class Index(object):
    def GET(self):
        #this is used to 'setup' the session with starting values
        session.room = map.START
        # sends HTTP code 303 with new location, browser performs GET on location
        web.seeother("/game")


class GameEngine(object):

    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
        #why is this here? do you need it?
            return render.you_died()
		
    def POST(self):
        form = web.input(action=None)

        #there is a bug here, can you fix it?
        # if we enter a wrong solution, it returns us to the you_died page
        # rather than sending us to the appropriate death page
        # but i think this fixed it
        if session.room and form.action:
            transition = session.room.go(form.action)
            if transition == None:
                transition = session.room.go('*')
            if transition != None:
                session.room = transition
            else: 
                session.room = None

        web.seeother("/game")

class count(object):
    def GET(self):
        session.count += 1
        return str(session.count)


class reset(object):
    def GET(self):
        session.kill()
        return ""
		
if __name__ == "__main__":
    app.run()