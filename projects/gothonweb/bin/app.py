#imports web.py module
import web

# this is our URL model
# the first part is a regex that matches a url (/, /help/faq, /item(\d+) etc)
# the second part is the name of the class to send the request to (eg index, view, welcomes.hello (hello class of welcomes module)

urls = (
  '/hello', 'index'
 )

# create an application with URLS listed above, looking up classes in global namespace
# then run that app. 
app = web.application(urls, globals())

# create variable 'render,' which is a web.template.render object
# it knows to take html files from 'templates/' directory because we gave it as a parameter
render = web.template.render('templates/')

class index(object):
#GET functions can be passed around and indexed
#POST functions submit a request that DOES something (eg charge a credit card)
    def GET(self):
	    # web.input gets data from the browser.
		# it takes key=value set as a default, parses '?name=Frank' part of the URL
		# and returns an object
        form = web.input(name="Nobody", greet=None)

        if form.greet:
            greeting = "%s, %s" % (form.greet, form.name)
            return render.index(greeting = greeting)
        else:
            return "ERROR: greet is required."
        
	
if __name__ == "__main__":
    app.run()