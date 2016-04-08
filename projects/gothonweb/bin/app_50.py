#imports web.py module
import web

# this is our URL model
# the first part is a regex that matches a url (/, /help/faq, /item(\d+) etc)
# the second part is the name of the class to send the request to (eg index, view, welcomes.hello (hello class of welcomes module)

urls = (
  '/', 'index'
 )

# create an application with URLS listed above, looking up classes in global namespace
# then run that app. 
app = web.application(urls, globals())

# create variable 'render,' which is a web.template.render object
# it knows to take html files from 'templates/' directory because we gave it as a parameter
render = web.template.render('templates/')

class index:
#GET functions can be passed around and indexed
#POST functions submit a request that DOES something (eg charge a credit card)
    def GET(self):
        greeting = "Hello World"
        foo = "Foo Bar"
        return render.index(greeting = greeting)
		# remember, the function called on render is just the name of the html page
		# return render.foo(foo)
	
if __name__ == "__main__":
    app.run()