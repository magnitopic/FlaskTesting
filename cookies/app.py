from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"

@app.route("/cookie/set")
def set_cookie():
	resp = make_response(render_template("index.html"))
	resp.set_cookie("username", "Alex")
	return resp

@app.route("/cookie/read")
def read_cookie():
	name = request.cookies.get('username', None)
	if name == None:
    		return "The cookie doesn't exist."
	return '<h1>welcome ' + name + '</h1>'


if __name__ == "__main__":
	app.run(debug=True)
