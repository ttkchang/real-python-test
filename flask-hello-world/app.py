# ---- Flask Hello World ---- #
# 
# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)
#
# error handling
app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")
@app.route("/jomama")

# define the view using a function which returns a string
# 
def hello_world():
	return "Hello World!???"

@app.route("/maybe")
def maybe_world():
	return "Maybe World!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/integervalue/<int:value>")
def int_type(value):
	print "this is in the terminal :" +value + 1
	return "Correct Integer"

@app.route("/floatvalue/<float:value>")
def float_type(value):
	print "this is in the terminal :" +value + 1
	return "Correct Float"

@app.route("/pathvalue/<path:value>")
def path_type(value):
	print "this is in the terminal :" +value
	return "Correct Path"

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name), 200
	else :
		return "Not Found", 404



#start the development server using the run() method
if __name__ == "__main__":
	app.run()