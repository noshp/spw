from flask import render_template, request

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/guesser', methods=['POST', 'GET'])
def guesser():
	print("foo")
	return request.args.get('entries', 'default', type=str)