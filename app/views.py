
from flask import render_template, url_for, request
from app import app
from PyDictionary import PyDictionary

dictionary=PyDictionary()



@app.route('/', methods=['GET'])
def get_scrabble():
	return render_template("input.html")

@app.route('/', methods=['POST'])
def post_scrabble():
	letters=request.form['letters']
	definition=(dictionary.meaning(letters))	
	return render_template("holder.html", definition=definition)


