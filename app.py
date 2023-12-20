from flask import Flask, render_template, request
from bot import ask_question

app = Flask(__name__)

answer="Hello!"

@app.route('/')
def index():
	#answer = ask_question(new_question)
	return render_template("index.html", bot_response=answer)

@app.route('/', methods = ['POST'])
def index_post():

	new_question = request.form['my_question']
	new_character = request.form['name']
	print(new_question)
	answer = ask_question(new_character, new_question)
	return render_template("index.html", bot_response=answer)
